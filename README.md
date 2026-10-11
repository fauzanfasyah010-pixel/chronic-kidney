# 🩺 Chronic Kidney Disease (CKD) Risk Prediction

## 📌 Deskripsi Proyek
Proyek ini bertujuan untuk melakukan analisis data kesehatan dan membangun model *Machine Learning* untuk memprediksi tingkat risiko penyakit ginjal kronis (*Chronic Kidney Disease* / CKD) berdasarkan fitur klinis, demografi, dan gaya hidup pasien. 

Target prediksi dibagi menjadi tiga kategori risiko: **Low (Rendah)**, **Moderate (Sedang)**, dan **High (Tinggi)**. Proyek ini tidak hanya berfokus pada pembangunan model klasifikasi utama, tetapi juga melakukan eksperimen komparatif dengan model regresi untuk melihat pendekatan mana yang paling optimal. Seluruh proses dirancang dengan penekanan kuat pada **integritas data** (pencegahan *data leakage*) dan **penanganan *overfitting***.

## 🧠 Algoritma yang Digunakan
Tiga algoritma *Machine Learning* diimplementasikan dan dibandingkan dalam proyek ini:
1. **Random Forest Classifier** (Model Utama): Digunakan untuk tugas klasifikasi multi-kelas. Diterapkan dengan regularisasi ketat (*hyperparameter tuning*) untuk mencegah *overfitting* dan penanganan *class imbalance*.
2. **Linear Regression** (Model Pembanding): Digunakan sebagai *baseline* regresi untuk memprediksi nilai target ordinal (0, 1, 2).
3. **Random Forest Regressor** (Model Pembanding): Digunakan untuk mempelajari hubungan nonlinier pada target ordinal melalui kumpulan pohon keputusan.

## 📊 Dataset
Dataset yang digunakan adalah **Chronic Kidney Disease Risk Prediction Dataset** (bersumber dari Kaggle).
- **Ukuran Data:** ±50.000 baris dan 40 kolom (sebelum *cleaning*).
- **Target Prediksi:** `CKD_Risk` (Kategori: Low, Moderate, High).
- **Fitur Utama:** Meliputi indikator klinis (seperti `eGFR`, `Blood_Pressure`, `Serum_Creatinine`, `Blood_Glucose`), demografi (`Age`, `BMI`), dan gaya hidup (`Smoking_Status`, `Diet_Quality`).

> **Catatan Penting (Target Leakage Prevention):** 
> Kolom seperti `Patient_ID`, `CKD_Risk_Score`, `AI_Health_Recommendation`, dan `Doctor_Consultation_Needed` **sengaja dihapus** sebelum pemodelan. Kolom-kolom tersebut merupakan turunan langsung dari target dan akan menyebabkan *data leakage* (model "menyontek") jika ikut dilatih.

## 🛠️ Tahapan Pengerjaan
1. **Import Library & Data Loading:** Memuat dataset menggunakan Pandas.
2. **Data Cleaning:** Menghapus kolom identitas dan kolom "penyontek" (*leakage*).
3. **Exploratory Data Analysis (EDA):** Visualisasi distribusi data mentah dan matriks korelasi fitur numerik.
4. **Outlier Handling:** Mendeteksi dan membuang nilai ekstrem yang tidak masuk akal secara medis menggunakan metode **IQR (Interquartile Range)**.
5. **Data Splitting:** Membagi data menjadi 80% Training dan 20% Testing menggunakan `stratify=y` untuk menjaga proporsi kelas minoritas.
6. **Preprocessing (Anti-Leakage):** 
   - Imputasi *missing values* (Median untuk numerik, Modus untuk kategorikal) **hanya di-fit pada data training**.
   - *One-Hot Encoding* untuk fitur kategorikal.
   - *Standard Scaling* untuk fitur numerik.
7. **Modeling:** Melatih model Klasifikasi (dengan regularisasi) dan model Regresi.
8. **Evaluation & Comparison:** Mengevaluasi performa dan membandingkan metrik antar model.
9. **Model Saving:** Menyimpan model terbaik menggunakan `joblib`.

## 📈 Evaluasi Model
Metrik evaluasi dibagi berdasarkan jenis tugas model:

**Untuk Model Klasifikasi (Random Forest Classifier):**
- **Accuracy:** Proporsi prediksi benar secara keseluruhan.
- **Precision, Recall, & F1-Score (Macro):** Metrik utama untuk menilai performa model, terutama karena dataset memiliki ketidakseimbangan kelas (*class imbalance*) pada kategori 'Low'.
- **Confusion Matrix:** Memvisualisasikan detail kesalahan klasifikasi antar kategori.

**Untuk Model Regresi (Linear & RF Regressor):**
- **MAE (Mean Absolute Error):** Rata-rata kesalahan absolut prediksi.
- **MSE (Mean Squared Error):** Kesalahan prediksi dengan penalti lebih besar untuk error yang besar.
- **R² (Coefficient of Determination):** Kemampuan model menjelaskan variasi data.

## 🌟 Highlight & Challenges Solved
- 🛡️ **Anti-Data Leakage:** Memastikan parameter *imputasi* dan *scaling* hanya dipelajari dari data latih (*training*), mencegah informasi data uji bocor ke model.
- ⚖️ **Class Imbalance Handling:** Menggunakan `class_weight='balanced'` agar model tidak bias terhadap kelas mayoritas ('High') dan tetap peduli pada kelas minoritas ('Low').
- 🚧 **Overfitting Prevention:** Menerapkan *hyperparameter tuning* (`max_depth`, `min_samples_split`, `min_samples_leaf`) pada Random Forest untuk menghentikan model "menghafal" data latih, sehingga akurasi *training* dan *testing* menjadi seimbang (generalization).

## 📂 Struktur Repository
```text
ckd-risk-prediction/
├── Dataset chronic kidney.ipynb      # File Jupyter Notebook utama
├── chronic_kidney_disease...csv      # Dataset mentah
├── rf_classifier_ckd.joblib          # Model Random Forest Classifier tersimpan
├── scaler_ckd.joblib                 # Scaler untuk preprocessing data baru
├── linear_regression_ckd.joblib      # Model Regresi (Pembanding)
├── rf_regressor_ckd.joblib           # Model Regresi (Pembanding)
└── README.md                         # Dokumentasi proyek
