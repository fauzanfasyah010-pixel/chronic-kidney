
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
from datetime import datetime
import json

st.set_page_config(
    page_title="Prediksi Risiko CKD",
    page_icon="🩺",
    layout="wide"
)

st.title("Prediksi Risiko Penyakit Ginjal Kronis (CKD)")
st.write(
    "Masukkan data sesuai kolom dataset untuk melihat hasil prediksi model."
)
st.warning(
    "Aplikasi ini hanya untuk demonstrasi akademik, bukan alat diagnosis medis."
)

MODEL_PATH = Path(__file__).parent / "ckd_deployment_bundle.joblib"
LOG_PATH = Path(__file__).parent / "prediction_logs.csv"

@st.cache_resource
def load_bundle():
    return joblib.load(MODEL_PATH)

try:
    bundle = load_bundle()
except Exception as e:
    st.error(f"Model gagal dimuat: {e}")
    st.stop()

input_columns = bundle["input_columns"]
numeric_columns = bundle["numeric_columns"]
categorical_columns = bundle["categorical_columns"]
encoded_columns = bundle["encoded_columns"]

st.subheader("Masukkan Data")

with st.form("ckd_form"):
    values = {}

    col1, col2 = st.columns(2)

    for i, column in enumerate(input_columns):
        container = col1 if i % 2 == 0 else col2

        with container:
            if column in numeric_columns:
                values[column] = st.number_input(
                    column,
                    value=0.0,
                    format="%.2f"
                )
            elif column in categorical_columns:
                options = bundle.get("categorical_options", {}).get(
                    column, []
                )

                if options:
                    values[column] = st.selectbox(
                        column,
                        options=options
                    )
                else:
                    values[column] = st.text_input(column)

    submitted = st.form_submit_button("Prediksi Risiko")

if submitted:
    sample = pd.DataFrame([values], columns=input_columns)

    try:
        sample[numeric_columns] = bundle["imputer_num"].transform(
            sample[numeric_columns]
        )

        sample_encoded = pd.get_dummies(
            sample,
            columns=categorical_columns,
            drop_first=True
        )

        sample_encoded = sample_encoded.reindex(
            columns=encoded_columns,
            fill_value=0
        )

        sample_scaled = pd.DataFrame(
            bundle["scaler"].transform(sample_encoded),
            columns=encoded_columns
        )

        prediction = int(bundle["model"].predict(sample_scaled)[0])
        result = bundle["target_labels"][prediction]

        st.subheader("Hasil Prediksi")

        if result == "High":
            st.error(f"Kategori risiko model: {result}")
        elif result == "Moderate":
            st.warning(f"Kategori risiko model: {result}")
        else:
            st.success(f"Kategori risiko model: {result}")

        st.caption(
            "Kategori ini merupakan keluaran model berdasarkan dataset, "
            "bukan diagnosis atau kepastian kondisi kesehatan."
        )

        log_entry = {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "prediction": result,
            **values
        }

        log_df = pd.DataFrame([log_entry])

        if LOG_PATH.exists():
            log_df.to_csv(
                LOG_PATH,
                mode="a",
                header=False,
                index=False
            )
        else:
            log_df.to_csv(LOG_PATH, index=False)

        st.info("Prediksi dicatat untuk keperluan monitoring.")

    except Exception as e:
        st.error(f"Prediksi gagal diproses: {e}")
