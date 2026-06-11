# 🛒 E-Commerce Catalog Manager

> Implementasi **General Tree** sebagai struktur data utama untuk manajemen katalog produk e-commerce berbasis web menggunakan Python & Streamlit.

---

## 📌 Deskripsi Proyek

Aplikasi ini mensimulasikan sistem manajemen katalog produk sebuah toko online (e-commerce). Setiap kategori dan produk direpresentasikan sebagai **node dalam General Tree**, sehingga memungkinkan hierarki kategori yang fleksibel dan tidak terbatas kedalamannya.

**Contoh hierarki:**
```
TokoPusat (Root)
├── Elektronik (Kategori)
│   ├── Komputer (Kategori)
│   │   ├── Laptop Asus (Produk)
│   │   └── Desktop Gaming (Produk)
│   └── Mobile (Kategori)
│       ├── Smartphone (Produk)
│       └── Tablet (Produk)
└── Pakaian (Kategori)
    ├── Pria (Kategori)
    │   └── Kemeja (Produk)
    └── Wanita (Kategori)
        └── Dress (Produk)
```

---

## 🏗️ Arsitektur Proyek

Proyek ini menerapkan prinsip **Separation of Concerns** dengan pemisahan berkas yang tegas:

```
project/
├── logic.py        # Backend: Definisi struktur data (TreeNode, GeneralTree)
├── ecommerce.py    # Domain Logic: Operasi katalog (EcommerceCatalog)
├── app.py          # Frontend: Antarmuka Streamlit
└── README.md
```

| Berkas         | Tanggung Jawab                                                                |
|----------------|-------------------------------------------------------------------------------|
| `logic.py`     | Class `TreeNode` & `GeneralTree` — **murni struktur data**, tidak ada kode UI |
| `ecommerce.py` | Class `EcommerceCatalog` — logika bisnis e-commerce, mewarisi `GeneralTree`   |
| `app.py`       | Tampilan Streamlit, form input, visualisasi, session state                    |

---

## 🧠 Struktur Data: General Tree

### Mengapa General Tree?

Katalog e-commerce memiliki hierarki kategori yang **tidak terbatas** dan **tidak teratur** — satu kategori bisa memiliki 2 atau 20 sub-kategori. Binary Tree tidak cocok karena membatasi maksimal 2 anak. **General Tree** adalah solusi paling tepat karena setiap node boleh memiliki jumlah anak yang bebas.

### Komponen Utama (`logic.py`)

#### `TreeNode`
Merepresentasikan satu simpul dalam pohon.

```python
class TreeNode:
    def __init__(self, name, node_type="Kategori", data=None):
        self.name      # Nama node
        self.node_type # "Root" | "Kategori" | "Produk"
        self.data      # Dict tambahan (harga, stok) untuk produk
        self.children  # List anak-anak node (itulah "General" Tree)
```

#### `GeneralTree`
Kelas utama yang menyimpan root dan menyediakan operasi-operasi dasar:

| Method               | Algoritma                | Fungsi                                                  |
|----------------------|--------------------------|---------------------------------------------------------|
| `find_node()`        | DFS (Depth-First Search) | Mencari node berdasarkan nama                           |
| `find_parent_node()` | DFS                      | Mencari parent dari suatu node (untuk operasi hapus)    |
| `insert_node()`      | -                        | Menambahkan node baru sebagai anak dari parent tertentu |
| `remove_node()`      | -                        | Menghapus node beserta seluruh sub-tree-nya             |
| `count_nodes()`      | Rekursif                 | Menghitung total node dalam pohon                       |
| `get_tree_height()`  | Rekursif                 | Menghitung kedalaman/tinggi pohon                       |
| `get_all_nodes()`    | DFS                      | Mengumpulkan seluruh node sebagai list                  |

---

## 🚀 Cara Menjalankan

### 1. Prasyarat

Pastikan Python sudah terinstal (Python 3.8+). Cek dengan:
```bash
python --version
```

### 2. Instalasi Dependensi

```bash
pip install streamlit graphviz
```

> **Catatan:** Untuk visualisasi Graphviz, instal juga program Graphviz di sistem:
> - **Windows:** Download dari https://graphviz.org/download/ lalu tambahkan ke PATH
> - **macOS:** `brew install graphviz`
> - **Linux (Ubuntu/Debian):** `sudo apt-get install graphviz`

### 3. Jalankan Aplikasi

```bash
streamlit run app.py
```

Aplikasi akan terbuka otomatis di browser pada alamat:
```
http://localhost:8501
```

## 🛠️ Alur Pengembangan dan Kolaborasi (Git Workflow)
Sesuai dengan standar pengembangan perangkat lunak di industri, proyek ini dikelola menggunakan Git dengan mekanisme kolaborasi berbasis repositori. Berikut adalah panduan teknis untuk menyalin proyek dan ikut serta berkontribusi:

## 📥 1. Cara Menyalin Proyek (Clone)
Bagi Anda yang ingin menguji, menjalankan, atau meninjau seluruh baris kode aplikasi ini di perangkat lokal masing-masing, ikuti perintah berikut pada terminal atau Git Bash:

### 1. Melakukan clone repositori proyek
```bash
git clone https://github.com/kaIhsan/e-commerce.git
 ```

### 2. Masuk ke dalam direktori/folder proyek yang telah di-clone

```bash
cd e-commerce
```

### 3. Pastikan dependensi sudah terinstall, lalu jalankan program

```bash
streamlit run app.py
```

## 🤝 2. Cara Berkontribusi (Contribute)
Kami menerapkan alur kerja Fork & Pull Request Workflow untuk memastikan setiap kode baru divalidasi dan diuji terlebih dahulu sebelum digabungkan ke kode utama. Jika Anda ingin berkontribusi memperbaiki bug atau menambahkan fitur baru:

### 1. Fork Repositori proyek ini ke akun GitHub Anda masing-masing melalui tombol Fork di pojok kanan atas halaman GitHub.

### 2. Clone hasil fork Anda ke perangkat lokal.

### 3. Buat Branch Baru yang spesifik untuk fitur atau perbaikan yang akan Anda kerjakan agar tidak mengganggu branch utama (main):

```Bash
git checkout -b fitur-baru-anda
```

### 4. **Lakukan Perubahan** pada file kode program Anda secara rapi (terapkan prinsip OOP dan *Separation of Concerns*).
### 5. **Simpan dan Commit** perubahan kode Anda dengan menyertakan pesan commit yang jelas dan deskriptif:
```bash
git add . 
git commit -m "feat: menambahkan validasi dinamis input produk pada app.py"
```

### Push Branch tersebut ke repositori fork di akun GitHub Anda:

```Bash
git push origin fitur-baru-anda
```

### 7. **Buat Pull Request (PR)** melalui antarmuka GitHub dari branch repositori Anda ke branch `main` repositori utama kami. Tim kami akan meninjau (*code review*) kontribusi Anda sebelum melakukan *merge*.

---
## ✨ Fitur Aplikasi

### ➕ Tab Tambah
- Menambah **kategori baru** di bawah kategori mana pun yang ada
- Menambah **produk baru** (dengan harga & stok) ke dalam kategori
- Validasi input: nama kosong, nama duplikat, harga/stok negatif, dan mencegah penambahan produk ke dalam produk

### 🗑️ Tab Hapus
- Menghapus kategori atau produk mana pun (kecuali Root)
- Menghapus kategori otomatis menghapus semua anak di dalamnya (**cascade delete**)
- Konfirmasi checkbox sebelum penghapusan

### 📊 Tab Visualisasi
- Menampilkan **tree secara visual** menggunakan Graphviz
- Warna berbeda untuk Root 🏠, Kategori 📁, dan Produk 🟢
- Setiap node produk menampilkan nama, harga, dan stok

### 📊 Sidebar Statistik
- Total produk, kategori, node, dan kedalaman tree
- Total nilai inventori dan total stok

### 🔍 Tab Cari
- Mencari produk berdasarkan nama menggunakan algoritma **DFS** dari `find_node()`
- Menampilkan detail produk: nama, harga, dan stok jika ditemukan

---

## 🔍 Detail Implementasi Teknis

### Traversal: Depth-First Search (DFS)

Pencarian node menggunakan algoritma DFS secara rekursif:

```python
def find_node(self, current_node, name):
    if current_node.name.lower() == name.lower():
        return current_node
    for child in current_node.children:
        found = self.find_node(child, name)
        if found:
            return found
    return None
```

### Cascade Delete

Saat menghapus kategori, seluruh sub-tree (anak, cucu, dst.) ikut terhapus secara otomatis. Ini terjadi karena Python's garbage collector membersihkan referensi yang tidak lagi terhubung ke root.

### Session State

Data tree disimpan dalam `st.session_state` Streamlit agar tidak hilang saat pengguna berinteraksi dengan UI:

```python
if 'catalog' not in st.session_state:
    st.session_state.catalog = EcommerceCatalog("TokoPusat")
```

---

## 👥 Anggota Kelompok

| No | Nama                          | NIM        |
|----|-------------------------------|------------|
| 1  | Khalilullah Al Ihsan          | 2530801034 |
| 2  | Nadya Athalia Diva            | 2530801029 |
| 3  | Kaysan Nawfal Salif Athaullah | 2530801042 |

**Mata Kuliah:** Struktur Data
**Dosen Pengampu:** M. Firdaus, M.Kom.  
**Semester:** 2B
