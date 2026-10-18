# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np

# ==========================================
# 1. MEMUAT MODEL (DEPLOYMENT BUNDLE)
# ==========================================
try:
    bundle = joblib.load("ckd_deployment_bundle.joblib")
    model = bundle['model']
    scaler = bundle['scaler']
    imputer_num = bundle['imputer_num']
    encoded_columns = bundle['encoded_columns'] # Daftar kolom final hasil get_dummies
except Exception as e:
    print(f"Error saat memuat model: {e}")

# Inisialisasi FastAPI
app = FastAPI(
    title="CKD Risk Prediction API",
    description="API untuk memprediksi risiko Chronic Kidney Disease berdasarkan data pasien.",
    version="1.0.0"
)

# ==========================================
# 2. MENDIFINISIKAN SCHEMA INPUT (PYDANTIC)
# ==========================================
# Ini adalah "formulir" data yang harus dikirim oleh pengguna API.
# (Saya contohkan 6 fitur utama, kamu tinggal tambahkan sisanya sesuai datasetmu)
class PatientData(BaseModel):
    Age: float
    BMI: float
    Blood_Pressure_Systolic: float
    Blood_Glucose: float
    Serum_Creatinine: float
    eGFR: float
    # ... Tambahkan sisa fitur numerik & kategorikal kamu di sini ...
    # Contoh: Gender: str, Diabetes: str, dll.

# ==========================================
# 3. MEMBUAT ENDPOINT PREDIKSI
# ==========================================
@app.post("/predict")
def predict_ckd_risk(data: PatientData):
    try:
        # A. Ubah data JSON yang masuk menjadi Pandas DataFrame (1 baris)
        input_df = pd.DataFrame([data.dict()])
        
        # B. Preprocessing (Sesuaikan dengan alur training kamu)
        # 1. Imputasi Numerik (jika ada yang kosong)
        num_cols = input_df.select_dtypes(include=['number']).columns
        input_df[num_cols] = imputer_num.transform(input_df[num_cols])
        
        # 2. One-Hot Encoding untuk kategorikal (jika ada)
        # cat_cols = input_df.select_dtypes(include=['object']).columns
        # input_df = pd.get_dummies(input_df, columns=cat_cols, drop_first=True)
        
        # 3. Sinkronisasi Kolom (Sangat Penting!)
        # Pastikan kolom data input sama persis dengan kolom saat training
        input_df = input_df.reindex(columns=encoded_columns, fill_value=0)
        
        # 4. Scaling
        input_scaled = scaler.transform(input_df)
        
        # C. Lakukan Prediksi
        prediction = model.predict(input_scaled)[0]
        probabilities = model.predict_proba(input_scaled)[0]
        
        # Mapping hasil (0: Low, 1: Moderate, 2: High)
        risk_mapping = {0: "Low", 1: "Moderate", 2: "High"}
        risk_level = risk_mapping[prediction]
        
        # D. Kembalikan hasil dalam format JSON
        return {
            "status": "success",
            "prediction": risk_level,
            "confidence_score": {
                "Low": round(float(probabilities[0]) * 100, 2),
                "Moderate": round(float(probabilities[1]) * 100, 2),
                "High": round(float(probabilities[2]) * 100, 2)
            }
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint untuk cek apakah API hidup
@app.get("/")
def read_root():
    return {"message": "CKD Risk Prediction API is running smoothly!"}