#  Support Vector Machine (SVM) — Klasifikasi & Regresi

Kumpulan notebook latihan **Machine Learning** menggunakan algoritma **Support Vector Machine (SVM)** dengan library **scikit-learn**.

1. **Klasifikasi** — Prediksi penyakit diabetes menggunakan `SVC`
2. **Regresi** — Prediksi gaji berdasarkan pengalaman kerja menggunakan `SVR`
3. **Latihan Konsep** — Visualisasi *decision boundary* (hyperplane) dan *margin* SVM secara manual maupun dengan scikit-learn

---

## 📁 Struktur Repository

```
├── diabetes.csv                      # Dataset Pima Indians Diabetes
├── Indian diebetes Klasification.ipynb   # Klasifikasi diabetes dengan SVC
├── Indian Diabetes Regresion.ipynb       # Regresi gaji dengan SVR
├── Latihan SVM Sklearn.ipynb             # Latihan SVM linear kernel (scikit-learn)
├── Latihan SVM py .ipynb                 # Latihan SVM: hyperplane & margin manual
└── README.md

## 📊 Dataset

### 1. Pima Indians Diabetes (`diabetes.csv`)
- **Jumlah data:** 768 baris, 9 kolom (tidak ada missing value)
- **Target:** `Outcome` (0 = tidak diabetes, 1 = diabetes)

| Fitur | Keterangan |
|---|---|
| Pregnancies | Jumlah kehamilan |
| Glucose | Kadar glukosa |
| BloodPressure | Tekanan darah diastolik (mm Hg) |
| SkinThickness | Ketebalan lipatan kulit (mm) |
| Insulin | Kadar insulin (mu U/ml) |
| BMI | Indeks massa tubuh |
| DiabetesPedigreeFunction | Riwayat diabetes keluarga |
| Age | Usia (tahun) |

### 2. Salary Data (`Salary_Data.csv`)
- **Jumlah data:** 30 baris, 2 kolom
- **Fitur:** `YearsExperience` → **Target:** `Salary`

### 3. Dataset Latihan (dibuat manual di notebook)
- 8 titik data: jam belajar (`x1`) & jam tidur (`x2`)
- Label: `1` = lulus ujian, `-1` = tidak lulus

---

## Penjelasan Notebook

### 1️⃣ Indian diebetes Klasification.ipynb — Klasifikasi Diabetes (SVC)
Alur pengerjaan:
1. Load dataset dengan `pandas`, eksplorasi via `df.head()` & `df.info()`
2. Pisahkan fitur (8 kolom pertama) dan label (`Outcome`)
3. **Standarisasi fitur** dengan `StandardScaler` (SVM sensitif terhadap skala fitur)
4. Split data **80% latih / 20% uji** (`random_state=42`) → 614 data latih, 154 data uji
5. Latih model `SVC()` (kernel `rbf`, `C=1.0`, `gamma='scale'`)
6. Evaluasi dengan `clf.score(X_test, y_test)`

**Hasil:** Akurasi **72.73%** pada data uji, dengan 357 support vectors.

### 2️⃣ Indian Diabetes Regresion.ipynb — Regresi Gaji (SVR)
Alur pengerjaan:
1. Load `Salary_Data.csv`
2. Ubah fitur `YearsExperience` menjadi array 2D (`np.newaxis`) sesuai format input scikit-learn
3. Latih model `SVR(C=1000, gamma=0.05, kernel='rbf')`
4. Visualisasi: scatter data asli + garis hasil prediksi model

**Catatan:** Model dilatih pada seluruh data (tanpa train-test split) karena tujuannya
memvisualisasikan kemampuan SVR menangkap pola non-linear, bukan evaluasi generalisasi.

### 3️⃣ Latihan SVM Sklearn.ipynb — Decision Boundary dengan scikit-learn
- Melatih `SVC(kernel='linear')` pada dataset latihan 8 titik
- Mengambil koefisien hyperplane dari `clf.coef_` dan `clf.intercept_`
- Menghitung garis batas keputusan: `x2 = -(w1·x1 + b) / w2`
- Memvisualisasikan titik data (biru = lulus, merah = tidak lulus) beserta garis pemisahnya

###  Latihan SVM py .ipynb — Hyperplane & Margin Manual
- Menggunakan dataset latihan yang sama, tetapi hyperplane **didefinisikan manual**:
  - Hyperplane: `x2 = -x1 + 8.5`
  - Margin positif: `x2 = -x1 + 9`
  - Margin negatif: `x2 = -x1 + 8`
- Visualisasi lengkap: titik data + decision boundary + kedua garis margin
- Tujuan: memahami konsep **maximum margin** yang menjadi inti algoritma SVM

---

## Ringkasan Hasil

| Model | Dataset | Konfigurasi | Hasil |
|---|---|---|---|
| SVC | Diabetes | kernel=rbf, C=1.0, gamma=scale | Akurasi **72.73%** (data uji) |
| SVR | Salary Data | kernel=rbf, C=1000, gamma=0.05 | Kurva prediksi mengikuti tren data |
| SVC | Dataset latihan | kernel=linear | Hyperplane memisahkan kedua kelas dengan sempurna |

---

## Teknologi

- Python 3.12
- pandas
- numpy
- scikit-learn
- matplotlib
- Jupyter Notebook

## Cara Menjalankan

```bash
# 1. Clone repository
git clone https://github.com/<username>/<nama-repo>.git
cd <nama-repo>

# 2. (Opsional) buat virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

# 3. Install dependencies
pip install pandas numpy scikit-learn matplotlib jupyter

# 4. Jalankan Jupyter
jupyter notebook
```

Buka notebook yang diinginkan, lalu jalankan semua cell secara berurutan (**Run All**).

---

## Poin Pembelajaran

- SVM mencari **hyperplane dengan margin terbesar** untuk memisahkan kelas.
- **Kernel trick** (`rbf`) memungkinkan SVM menangani data yang tidak terpisah secara linear.
- **Standarisasi fitur** (`StandardScaler`) penting untuk SVM karena berbasis jarak.
- Parameter `C` mengontrol trade-off antara margin lebar dan kesalahan klasifikasi;
  `gamma` mengontrol seberapa jauh pengaruh satu titik data (kernel RBF).
- `SVC` untuk klasifikasi (label diskrit), `SVR` untuk regresi (nilai kontinu).
