<div align="center">

### Konstruksi Perangkat Lunak

### Pertemuan 11
### Design Pattern Impementation

![image](https://github.com/user-attachments/assets/2948daec-1e7a-4765-8f23-df638a387c87)

Disusun oleh:  
Nama : Aufa Muhammad Isyfa’Lana  
Nim : 2211104015  
Kelas : SE0601

Dosen Pengampu : 
Yudha Islami Sulistya, S.Kom., M.Cs. 

### PRODI S1 REKAYASA PERANGKAT LUNAK  
### FAKULTAS INFORMATIKA  
### TELKOM UNIVERSITY PURWOKERTO  
### 2025

</div>

---
<div align="center">

## Jurnal

</div>

### 1. Membuat Project Baru

![image](https://github.com/user-attachments/assets/841b0263-0677-4dc6-bbf5-747ebd03eca5)

### 2. Menjelaskan Design Pattern Singleton
A. Contoh penggunaan Singleton:
a. Logger – agar hanya satu instance yang menulis log di seluruh aplikasi.
b. Database connection pool – supaya tidak membuat banyak koneksi secara tidak efisien.

B. Langkah implementasi Singleton:
1. Buat constructor private.
2. Buat field statis untuk instance-nya.
3. Buat method publik statis untuk mengakses instance (biasanya GetInstance() atau properti).

C. Kelebihan dan Kekurangan:
- Kelebihan:
- Menghemat memori (hanya satu instance).
- Mudah diakses dari mana saja.
- Cocok untuk shared resources (log, config).

Kekurangan:
- Sulit diunit-test (karena state global).
- Bisa menyebabkan tight coupling.
- Tidak cocok di lingkungan multi-thread tanpa penanganan khusus.

### 3. Implementasi Kode dan Pemhaman
#### PusatDataSingleton.cs

![image](https://github.com/user-attachments/assets/78631168-00b5-4e2e-8869-4d98a81e3a8c)

![image](https://github.com/user-attachments/assets/7cda0c65-2a6f-47c6-a3cb-70a9c316ddf6)

#### Program.cs

![image](https://github.com/user-attachments/assets/8266d22d-07fc-4625-a29d-8411bfaa2944)

#### Output :

![image](https://github.com/user-attachments/assets/b82eef20-fb9f-4ef8-90b0-93b7abb24a40)

#### Penjelasan : 
Kelas PusatDataSingleton merupakan implementasi dari design pattern Singleton, yang memastikan bahwa hanya ada satu instance dari kelas ini selama program berjalan. Kelas ini memiliki atribut private DataTersimpan bertipe List<string> yang menyimpan data dalam bentuk string, dan sebuah atribut statis private _instance untuk menyimpan instance tunggal kelas. Konstruktor dari kelas ini bersifat private agar tidak dapat diakses dari luar kelas dan hanya dapat dipanggil sekali melalui method publik statis GetDataSingleton(). Method ini akan mengembalikan instance yang sudah ada atau membuat instance baru jika belum ada. Selain itu, kelas ini menyediakan beberapa method publik seperti AddSebuahData(string input) untuk menambahkan data ke list, HapusSebuahData(int index) untuk menghapus data berdasarkan indeks, PrintSemuaData() untuk mencetak isi list satu per satu ke konsol, serta GetSemuaData() untuk mengambil seluruh isi list sebagai objek List<string>.

Pada bagian Main, dibuat dua variabel data1 dan data2 yang sama-sama memanggil method GetDataSingleton(). Karena menggunakan pola Singleton, kedua variabel ini akan merujuk ke instance yang sama. Melalui data1, ditambahkan beberapa data berupa nama-nama anggota kelompok dan asisten praktikum ke dalam list. Kemudian, melalui data2, dilakukan pencetakan data untuk memastikan bahwa semua data tersebut tersimpan. Setelah itu, data asisten praktikum dihapus menggunakan HapusSebuahData() dari data2. Saat mencetak ulang data menggunakan data1, terlihat bahwa data asisten praktikum sudah tidak ada, membuktikan bahwa data1 dan data2 memang merujuk pada instance yang sama. Terakhir, jumlah elemen dari list ditampilkan melalui kedua variabel untuk memastikan konsistensinya.

