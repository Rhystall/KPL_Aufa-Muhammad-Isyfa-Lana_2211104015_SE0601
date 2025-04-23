<div align="center">

### JURNAL

### Konstruksi Perangkat Lunak

### Pertemuan 8
### API Design dan Construction Using Swagger

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

### 1. Membuat Project Web API 

![image](https://github.com/user-attachments/assets/3480eabb-0bbc-468b-965b-1ef0e5554b43)

### 2. Melakukan git commit pada project yang dibuat

#### a. Github Repository 
https://github.com/Rhystall/kpl-api/ 
Branch Movie 

#### b. melakukan inisialisasi git 

![image](https://github.com/user-attachments/assets/a5230185-9f2e-425c-99c1-73acc649fec7)

#### c. membuat .gitignore 

![image](https://github.com/user-attachments/assets/f7c34a7f-6d5d-45b2-b7ac-23b9f1f2bd01)

#### d. melakukan first commit & push 

![image](https://github.com/user-attachments/assets/5f523943-2844-4a9a-a173-e03c4a118946)

### 3. Implementasi Web API
#### a. Movie.cs

![image](https://github.com/user-attachments/assets/4c533b44-8b71-4ab1-8400-8406c1cff569)

#### b. MovieController.cs 

![image](https://github.com/user-attachments/assets/8cfa5808-9d49-4cb8-af92-c35d5821ec8a)

![image](https://github.com/user-attachments/assets/c8f156d0-53b2-42bb-a5dd-cbed1cac790e)


#### c. Program.cs

![image](https://github.com/user-attachments/assets/5362d3b7-794c-41a3-b347-3e633f4496d3)

#### d. Hasil Run 

![image](https://github.com/user-attachments/assets/17b85770-68a3-4124-bf97-ea47c51e9bdb)


### Penjelasan Kode : 

Pada kode tersebut kita membuat API sederhana yang mengembalikan detail Movie dengan memanfaat Swagger UI.

### 4. Mendemonstrasikan WEB API

GET /api/Movies → 3 film awal.

![image](https://github.com/user-attachments/assets/496bf43f-e1d7-4374-8232-c1121fa5cb8f)


POST /api/Movies → Tambah film ke-4 dari IMDB.

![image](https://github.com/user-attachments/assets/175a0218-8369-42ec-b0f0-a79ad31164dc)


GET /api/Movies → Cek lagi, pastikan film baru muncul.

![image](https://github.com/user-attachments/assets/79d8cbfe-5945-40ce-a371-9d0070c3b331)

GET /api/Movies/3 → Ambil film baru tadi.

![image](https://github.com/user-attachments/assets/568e58c0-f790-4a4a-bdaf-54e915956335)

DELETE /api/Movies/1 → Hapus film index ke-1 (The Godfather).

![image](https://github.com/user-attachments/assets/00527870-f8f6-4271-a1cd-43d1519e9f9b)


GET /api/Movies → Cek, pastikan The Godfather udah hilang. (Kehapus 3 jir)

![image](https://github.com/user-attachments/assets/f7823515-9117-436e-bdfa-decccf11767f)


### 5. Melakukan Commit dan Push 

![image](https://github.com/user-attachments/assets/a96e9e35-56e1-46ee-ae9f-3b06ee4d1173)


