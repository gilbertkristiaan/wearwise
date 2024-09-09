
## Gilbert Kristian - 2306274951 - PBP D (TUGAS 2)

 - Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    
    JAWAB : 
    
    Langkah-langkahnya adalah sebagai berikut:
    
       1. Membuat sebuah repository lokal dengan nama project "Wearwise" 
       2. Menjalankan "django-admin startproject wear_wise ." untuk memulai project
       3. Menambahkan "localhost", "127.0.0.1" ke dalam list ALLOWED_HOSTS di file settings.py untuk keperluan deployment
       4. Membuat aplikasi baru dengan nama main dengan menjalankan command "python manage.py startapp main"
       5. Mendaftarkan 'main' ke dalam INSTALLED_APPS di settings.py pada direktori wear_wise
       6. Membuat direktori baru di dalam direktori main bernama templates untuk membuat main.html
       7. Membuat model pada aplikasi main dengan nama product yang memiliki atribut name, price, description.
       8. Membuat migrasi model dengan menjalankan "python manage.py makemigrations" untuk menyesuaikan struktur tabel database 
       berdasarkan perubahan model yang telah ditentukan dalam kode.
       9. Menghubungkan views.py pada direktori main dengan template, fungsi ini akan mengatur permintaan HTTP dan mengembalikan 
       nama aplikasi, nama, dan kelas.
       10. Membuat routing dengan membuat file urls.py di aplikasi main untuk memetakan fungsi yang telah dibuat di views.py 
       dengan membuat urlpatterns = [path('', show_main, name='show_main'),]
       11. Membuat routing di file urls.py di direktori wear_wise dengan membuat urlpatterns = [path('', include('main.urls')),] 
       yang akan mengimpor rute URL dari aplikasi
       12. Men-deploy ke PWS agar dapat diakses publik, lalu meletakkan URL PWS ke ALLOWED_HOSTS di settings.py

 - Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    
    Jawab :
   ```mermaid
   sequenceDiagram
      participant Client
      participant Internet
      participant manage.py
      participant urls.py
      participant views.py
      participant models.py
      participant DB
      participant main.html

      Client->>Internet: Request Web Page
      Internet->>manage.py: Forward Request
      activate manage.py

      manage.py->>urls.py: Handle Request URL
      activate urls.py

      Note right of Client: Client mengirimkan request melalui browser

      urls.py->>views.py: Memanggil Fungsi yang Sesuai
      deactivate urls.py
      activate views.py

      Note right of urls.py: urls.py mengarahkan URL ke view yang relevan

      views.py->>models.py: Mengambil data dari model (jika diperlukan)
      activate models.py

      models.py->>DB: Query ke database
      activate DB

      DB-->>models.py: Mengirimkan data ke model
      deactivate DB

      models.py-->>views.py: Data dari database kembali ke views
      deactivate models.py

      views.py->>main.html: Render halaman HTML dengan data
      activate main.html

      Note right of views.py: views.py mengisi template HTML dengan data dari model

      main.html-->>views.py: Halaman HTML yang sudah dirender
      deactivate main.html

      views.py-->>manage.py: Kembali ke manage.py dengan halaman HTML yang dirender
      deactivate views.py

      manage.py-->>Internet: Kirim respons (halaman HTML) ke Internet
      deactivate manage.py

      Internet-->>Client: Kirim halaman web ke Client

      Note over Client,Internet: Client menerima halaman HTML yang dirender dari server Django
```
```

   Penjelasan alur bagan :
   1. Client meminta halaman web, kemudian permintaan ini diteruskan oleh Internet ke server Django, yaitu manage.py.
   2. manage.py menerima permintaan dan meneruskannya ke urls.py, yang bertugas memetakan URL yang diminta ke fungsi yang sesuai di views.py.
   3. urls.py mengarahkan permintaan ke fungsi yang relevan di views.py. Di sini, views.py dapat meminta data dari models.py jika diperlukan.
   4. models.py mengirimkan query ke DB (database) untuk mendapatkan data yang relevan. Setelah data diambil, DB mengembalikannya ke models.py, yang kemudian meneruskannya ke views.py.
   5. Setelah menerima data dari model, views.py merender halaman HTML dengan mengisi template yang relevan (diwakili oleh main.html).
   6. main.html mengembalikan halaman yang telah dirender ke views.py, yang kemudian mengirimkan hasilnya ke manage.py.
   7. manage.py mengirimkan respons halaman HTML yang dirender kembali ke Client melalui Internet, yang akhirnya memungkinkan Client untuk menampilkan halaman web di browser.


- Jelaskan fungsi git dalam pengembangan perangkat lunak!
    
    Jawab : 
    
   Git dapat membantu dalam pengembangan perangkat lunak yang memungkinkan banyak pengembang untuk bekerja sama dan dapat mudah untuk melacak perubahan dalam kode. Fitur yang paling berguna dalam pengembangan perangkat lunak di git adalah branch. Dengan menyediakan mekanisme branch, Git memudahkan kolaborasi antarpengembang sehingga banyak orang dapat bekerja pada fitur yang berbeda secara bersamaan tanpa terjadi konflik. Pengembang bisa membuat branch baru untuk setiap fitur atau bug fix dan menggabungkannya setelah selesai.

   Git juga berfungsi sebagai berikut untuk pengembangan perangkat lunak:
   1. Versi Kontrol: Git memungkinkan tim pengembang untuk melacak perubahan pada kode sumber secara sistematis. Setiap perubahan yang dilakukan pada proyek tersimpan dalam commit sehingga memudahkan untuk melihat riwayat perubahan dan memulihkan versi sebelumnya jika terjadi masalah.

   2. Kolaborasi Tim: Git memungkinkan beberapa pengembang untuk bekerja secara bersamaan pada proyek yang sama tanpa mengganggu pekerjaan satu sama lain. Dengan cabang (branch), setiap pengembang bisa mengerjakan fitur atau perbaikan secara terpisah sebelum menggabungkannya kembali ke cabang utama (main branch).

   3. Manajemen Cabang: Dengan Git, pengembang dapat membuat cabang untuk mengembangkan fitur baru, memperbaiki bug, atau menguji ide eksperimental tanpa mengganggu kode di cabang utama. Cabang ini bisa digabungkan kembali jika sudah stabil atau dihapus jika tidak lagi diperlukan.

   4. Pemulihan Kesalahan: Git memungkinkan pengembang untuk memutar kembali proyek ke versi sebelumnya jika terjadi bug atau kesalahan. Setiap commit menyimpan snapshot dari proyek, sehingga mudah untuk menemukan dan memperbaiki kesalahan tanpa kehilangan pekerjaan penting.

   5. Penyimpanan Terdistribusi: Git menggunakan pendekatan terdistribusi, di mana setiap pengembang memiliki salinan lengkap dari seluruh riwayat proyek. Ini berarti pekerjaan bisa dilanjutkan secara lokal tanpa koneksi internet, dan pengembang dapat menyinkronkan perubahan ke server pusat kapan pun diperlukan.

   6. Integrasi Berkelanjutan (CI/CD): Git sering digunakan dengan alat integrasi berkelanjutan (CI) dan pengiriman berkelanjutan (CD) untuk secara otomatis menguji dan mengirimkan kode setiap kali ada perubahan yang di-push. Hal ini membantu mendeteksi kesalahan lebih awal dan mempercepat siklus pengembangan.

   7. Open Source dan Kolaborasi Global: Git adalah alat open-source yang banyak digunakan di berbagai proyek perangkat lunak, termasuk proyek open-source besar. Platform seperti GitHub dan GitLab memungkinkan pengembang dari seluruh dunia untuk berkontribusi ke dalam satu proyek secara mudah.

- Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    
    Jawab :  

    Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena pengembangannya yang bersifat open source, ridiculously fast, fully loaded, reassuringly secure, exceedingly scalable, dan incredibly versatile. Django menyediakan banyak fitur-fitur bawaan yang memudahkan pemula untuk mulai membangun aplikasi. Django juga menggunakan pola MTV yang membantu pemula lebih mudah dalam memahami struktur aplikasi, yaitu model (database), view (logika aplikasi), dan template (mengelola tampilan). Django juga menggunakan Python, yang jugdi mana merupakan bahasa pemrograman yang populer di kalangan pemula karena sintaksnya yang sederhana dan mudah dibaca. Django juga dirancang dengan mempertimbangkan praktik keamanan yang baik.

- Mengapa model pada Django disebut sebagai ORM?
    
    Jawab :

    Django disebut sebagai Object Relational Mapping karena penggunaan ORM di Django memungkinkan pengembang untuk berinteraksi dengan database menggunakan kode Python tanpa menulis SQL secara manual. Django akan mengubah objek Python (model) menjadi tabel di database. Setiap atribut model diubah menjadi kolom dalam tabel. 



