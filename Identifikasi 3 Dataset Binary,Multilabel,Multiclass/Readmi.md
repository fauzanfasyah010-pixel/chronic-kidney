# Identifikasi 9 Dataset Classification

## Pendahuluan

Pada tugas ini dilakukan pencarian dan identifikasi terhadap 9 dataset yang berasal dari Kaggle. Dataset dikelompokkan menjadi tiga jenis, yaitu Binary Classification, Multiclass Classification, dan Multilabel Classification.

Tujuan identifikasi ini adalah mengetahui apakah suatu dataset termasuk permasalahan klasifikasi atau regresi, kemudian menentukan jenis klasifikasi berdasarkan karakteristik target atau label yang dimiliki.

---

# 1. Binary Classification

Binary Classification merupakan metode klasifikasi yang digunakan untuk memprediksi suatu data ke dalam dua kelas atau kategori yang berbeda.

### 1.1 Breast Cancer Wisconsin

**Sumber:** Kaggle – Breast Cancer Wisconsin

**Mengapa termasuk Classification?**

Dataset ini termasuk Classification karena digunakan untuk menentukan apakah suatu sampel memiliki kondisi kanker payudara jinak (benign) atau ganas (malignant). Hasil yang diprediksi berupa kategori, bukan nilai angka yang berkelanjutan. Oleh karena itu, dataset ini bukan termasuk regresi.

**Jenis Klasifikasi: Binary Classification**

Dataset ini termasuk Binary Classification karena hanya memiliki dua kemungkinan kelas target, yaitu:

- Benign (jinak).
- Malignant (ganas).

Model akan mempelajari karakteristik data untuk menentukan salah satu dari kedua kategori tersebut.

### 1.2 Heart Disease

**Sumber:** Kaggle – Heart Disease

**Mengapa termasuk Classification?**

Dataset ini termasuk Classification karena digunakan untuk memprediksi apakah seseorang memiliki penyakit jantung atau tidak berdasarkan beberapa karakteristik, seperti usia, tekanan darah, dan hasil pemeriksaan kesehatan.

Target yang diprediksi berupa kategori sehingga termasuk permasalahan klasifikasi, bukan regresi.

**Jenis Klasifikasi: Binary Classification**

Dataset ini termasuk Binary Classification karena hasil prediksinya terdiri dari dua kelas:

- 0 = Tidak memiliki penyakit jantung.
- 1 = Memiliki penyakit jantung.

Dengan demikian, model hanya perlu menentukan salah satu dari dua kemungkinan tersebut.

### 1.3 Loan Status

**Sumber:** Kaggle – Loan Status

**Mengapa termasuk Classification?**

Dataset ini termasuk Classification karena digunakan untuk menentukan status pengajuan pinjaman berdasarkan informasi pemohon, seperti pendapatan, jumlah pinjaman, dan riwayat keuangan.

Hasil prediksi berupa status atau kategori pengajuan pinjaman, bukan angka yang harus diperkirakan secara berkelanjutan.

**Jenis Klasifikasi: Binary Classification**

Dataset ini termasuk Binary Classification karena memiliki dua kemungkinan hasil:

- Approved = Pinjaman disetujui.
- Rejected = Pinjaman ditolak.

Model bertugas menentukan apakah pengajuan pinjaman diterima atau ditolak.

---

# 2. Multiclass Classification

Multiclass Classification merupakan metode klasifikasi yang digunakan untuk memprediksi data ke dalam lebih dari dua kelas yang berbeda. Setiap data hanya memiliki satu kelas target utama.

### 2.1 Iris Dataset

**Sumber:** Kaggle – Iris Flower Dataset

**Mengapa termasuk Classification?**

Dataset ini termasuk Classification karena digunakan untuk mengidentifikasi jenis bunga Iris berdasarkan karakteristik fisiknya, seperti panjang dan lebar kelopak serta mahkota bunga.

Hasil prediksi berupa nama atau kategori spesies bunga, bukan nilai numerik yang berkelanjutan.

**Jenis Klasifikasi: Multiclass Classification**

Dataset ini termasuk Multiclass Classification karena memiliki tiga kelas spesies bunga:

- Iris Setosa.
- Iris Versicolor.
- Iris Virginica.

Setiap bunga hanya dikategorikan ke dalam satu spesies dari tiga pilihan tersebut.

### 2.2 Wine Dataset

**Sumber:** Kaggle – Wine Dataset

**Mengapa termasuk Classification?**

Dataset ini termasuk Classification karena digunakan untuk mengelompokkan atau memprediksi jenis wine berdasarkan karakteristik kandungan kimia, seperti alkohol, kadar asam, dan karakteristik lainnya.

Hasil yang diprediksi berupa kelas atau kategori wine sehingga termasuk klasifikasi.

**Jenis Klasifikasi: Multiclass Classification**

Dataset ini termasuk Multiclass Classification karena memiliki lebih dari dua kategori wine. Pada dataset Wine yang umum digunakan terdapat tiga kelas:

- Class 1.
- Class 2.
- Class 3.

Setiap sampel wine memiliki satu kelas yang menjadi target prediksi.

### 2.3 Birds' Bones and Living Habits

**Sumber:** Kaggle – Birds' Bones and Living Habits

**Mengapa termasuk Classification?**

Dataset ini termasuk Classification karena digunakan untuk mengidentifikasi atau mengelompokkan burung berdasarkan karakteristik tulang dan kebiasaan hidupnya.

Hasil identifikasi berupa kategori atau kelompok burung, bukan nilai numerik kontinu.

**Jenis Klasifikasi: Multiclass Classification**

Dataset ini termasuk Multiclass Classification karena memiliki beberapa kategori kelas burung. Setiap sampel burung dimasukkan ke dalam satu kategori berdasarkan label yang tersedia pada dataset.

---

# 3. Multilabel Classification

Multilabel Classification merupakan metode klasifikasi yang memungkinkan satu data memiliki lebih dari satu label sekaligus. Berbeda dengan Multiclass, satu data tidak hanya dibatasi pada satu kategori.

### 3.1 Emotions Dataset

**Sumber:** Kaggle – Emotions Dataset

**Mengapa termasuk Classification?**

Dataset ini termasuk Classification karena digunakan untuk mengidentifikasi emosi yang terkandung dalam sebuah lagu berdasarkan karakteristik musiknya.

Hasil prediksi berupa kategori emosi yang dapat dikenali dari data lagu, bukan nilai numerik kontinu.

**Jenis Klasifikasi: Multilabel Classification**

Dataset ini termasuk Multilabel Classification karena satu lagu dapat memiliki beberapa label emosi sekaligus.

Contohnya, satu lagu dapat memiliki label:

- Happy.
- Relaxed.
- Sad.

Artinya, satu sampel lagu memungkinkan memiliki lebih dari satu kategori emosi secara bersamaan.

### 3.2 NLP-Based Multi Label Classification

**Sumber:** Kaggle – NLP-Based Multi Label Classification

**Mengapa termasuk Classification?**

Dataset ini termasuk Classification karena digunakan untuk mengelompokkan teks berdasarkan kategori atau label tertentu melalui analisis Natural Language Processing (NLP).

Hasil prediksi berupa kategori teks sehingga termasuk klasifikasi, bukan regresi.

**Jenis Klasifikasi: Multilabel Classification**

Dataset ini termasuk Multilabel Classification karena satu teks dapat memiliki beberapa label kategori sekaligus.

Model dapat memprediksi beberapa kategori yang sesuai dengan isi teks, sehingga tidak hanya terbatas pada satu label.

### 3.3 Flags Dataset

**Sumber:** Kaggle – Flags Dataset

**Mengapa termasuk Classification?**

Dataset ini berisi informasi mengenai bendera dari berbagai negara beserta karakteristiknya. Data tersebut dapat digunakan untuk memprediksi atau mengelompokkan atribut bendera berdasarkan informasi yang tersedia.

Hasil prediksi berupa kategori atau atribut, bukan nilai numerik kontinu.

**Jenis Klasifikasi: Multilabel Classification**

Dataset ini dapat digunakan untuk Multilabel Classification apabila beberapa atribut bendera ditetapkan sebagai label target secara bersamaan.

Contohnya, satu bendera dapat memiliki beberapa karakteristik sekaligus, seperti warna merah, putih, dan biru.

Dengan demikian, satu sampel dapat memiliki lebih dari satu label target.

---

## Kesimpulan

Berdasarkan identifikasi terhadap sembilan dataset, seluruh dataset yang dipilih ditujukan untuk permasalahan klasifikasi karena hasil yang ingin diprediksi berupa kelas atau kategori.

Pembagian dataset berdasarkan jenis klasifikasinya adalah sebagai berikut:

| Jenis Klasifikasi         | Jumlah |
| ------------------------- | -----: |
| Binary Classification     |      3 |
| Multiclass Classification |      3 |
| Multilabel Classification |      3 |
| **Total**                 |  **9** |

Binary Classification memiliki dua kelas target, Multiclass Classification memiliki lebih dari dua kelas dengan satu label untuk setiap data, sedangkan Multilabel Classification memungkinkan satu data mempunyai beberapa label sekaligus.

Dengan demikian, identifikasi ini menunjukkan perbedaan karakteristik dari ketiga jenis klasifikasi tersebut.
