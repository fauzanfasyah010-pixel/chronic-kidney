# Classification Dataset

Folder ini disiapkan untuk tugas identifikasi dataset Machine Learning dari Kaggle.

Terdapat tiga kategori:
- **Binary Classification**: target memiliki tepat dua kelas.
- **Multiclass Classification**: target memiliki lebih dari dua kelas, dan setiap baris hanya memiliki satu kelas.
- **Multilabel Classification**: satu baris data dapat memiliki lebih dari satu label aktif.

## Ketentuan Dataset
- Setiap kategori berisi 3 dataset.
- Ukuran setiap file dataset harus kurang dari 3 MB.
- Dataset harus benar-benar merupakan masalah klasifikasi, bukan regresi.
- Penentuan kategori didasarkan pada struktur kolom target/label, bukan hanya judul dataset.

## Struktur Folder
```text
Classification 3 Dataset Binary,Multilabel,Multiclass/
├── README.md
├── Binary/
├── Multiclass/
└── Multilabel/
```

## Catatan
Folder kategori sudah dibuat. File dataset dan identifikasi final akan dimasukkan setelah ukuran file serta kolom target dari masing-masing dataset diverifikasi. Ini untuk menghindari salah klasifikasi, terutama membedakan multiclass dan multilabel.
