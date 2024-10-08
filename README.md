# Tugas Individu 2

1. Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).  
* **Membuat sebuah proyek Django baru**  
  Langkah pertama yang saya lakukan adalah membuat direktori baru bernama `eshop` sebagai direktori utama proyek saya. Setelah itu, saya hubungkan repositori lokal dengan repositori GitHub. Kemudian, di dalam direktori tersebut saya menjalankan perintah “`python -m venv env`” pada *command prompt* untuk membuat *virtual environment* sebagai lingkungan kerja. Setelah dibuat, saya mengaktifkan *virtual environment* tersebut dengan menjalankan perintah “`env\Scripts\activate`”. Langkah selanjutnya adalah membuat berkas baru bernama “requirements.txt” yang berisikan beberapa *dependencies*, kemudian install *dependencies* tersebut dengan menjalankan perintah “`pip install -r requirements.txt`”. Setelah itu, saya membuat proyek Django dengan menjalankan perintah “`dangjo-admin startproject eshop .`” pada *command  prompt* direktori proyek.   
    
* **Membuat aplikasi dengan nama `main` pada proyek tersebut**  
  Saya membuat aplikasi baru bernama “`main`” dengan menjalankan perintah “`python manage.py startapp main`”. Kemudian, saya mendaftarkan aplikasi tersebut ke dalam daftar variabel INSTALLED\_APPS di berkas `settings.py` dalam direktori proyek.   
    
* **Melakukan *routing* pada proyek agar dapat menjalankan aplikasi main**  
  Setelah aplikasi berhasil dibuat dan didaftarkan, kita perlu untuk menambahkan rute URL dalam berkas `urls.py` di direktori proyek untuk mengakses tampilan aplikasi `main`. Pada berkas *`urls.py`*, saya melakukan impor fungsi *`include`* dari “`django.urls`.” dan menambahkan rute URL “`path('', include('main.urls')),`” untuk mengarahkan ke tampilan `main` di dalam variabel `urlpatterns`. Path URL dibiarkan berupa string kosong agar halaman aplikasi main dapat diakses secara langsung.  
    
* **Membuat model pada aplikasi `main`**   
  Pada tahap ini, saya membuat model aplikasi dengan memodifikasi berkas `models.py` yang ada di direktori aplikasi `main`. Model yang saya buat terdiri dari 3 atribut/field wajib, yaitu `name, price,`dan `description`. Untuk `name`, tipe data yang digunakan adalah `CharField`, `price` bertipe data `IntegerField`, dan untuk `description` bertipe `TextField`. Langkah selanjutnya adalah membuat dan menerapkan perubahan database sesuai dengan model yang sudah dibuat dengan menjalankan perintah “`python manage.py makemigrations`” dan “`python manage.py migrate`”.  
    
* **Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah *template* HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.**  
  Pada berkas `views.py`, saya menambahkan “`import from django.shortcuts import render”` dan menambahkan fungsi `show_main` di bawah impor. Fungsi ini akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai dengan yang dibuat di berkas `main.html`. Berkas tersebut saya buat di dalam direktori `templates` pada direktori `main` untuk memastikan struktur aplikasi sudah sesuai dengan struktur kode Django, dan template tersebut menerima data dari konteks yang dikirimkan oleh `views.py`.  
* **Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.**  
  Saya membuat berkas `urls.py` di dalam direktori `main`. Pada berkas tersebut, saya mendefinisikan URL pattern untuk memetakan fungsi yang ada di `views.py` sebagai berikut:  
  `from django.urls import path`  
  `from main.views import show_main`  
  `app_name = 'main'`  
  `urlpatterns = [`  
  	`path('', show_main, name='show_main'),`  
  `]`  
  Impor `path` dari `django.urls` berfungsi untuk mendefinisikan pola URL.  
* **Melakukan *deployment* ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.**  
  Sebelum melakukan deployment, saya melakukan `git add`, `commit`, dan `push` semua perubahan ini ke repositori GitHub. Selanjutnya, saya mencoba menjalankan proyek Django dengan perintah `python manage.py runserver.` Setelah aplikasi berhasil berjalan di peramban  http://localhost:8000/, kemudian saya melakukan tahap-tahap deployment ke PWS agar proyek yang saya kerjakan bisa diakses di internet.

2. Buatlah bagan yang berisi *request client* ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara `urls.py`, `views.py`, `models.py`, dan berkas `html`.  
   ![][image1]  
1) **`urls.py`**  
* Django menggunakan file `urls.py` untuk memetakan URL yang diminta oleh client dengan view yang tepat. Saat sebuah URL diminta, Django mencocokkan URL tersebut dengan pola URL yang didefinisikan dalam `urls.py`.  
* Jika URL cocok, Django akan mengarahkan request tersebut ke fungsi yang sesuai di `views.py`.  
     
2) **`views.py`**  
* Fungsi yang terdefinisi dalam views.py menerima request dari urls.py.  
* Fungsi ini dapat memproses data, berinteraksi dengan database melalui `models.py` jika diperlukan, dan mengirimkan data ke template HTML untuk menghasilkan halaman web yang akan dikirim kembali ke client.

3) **`model.py`**  
* Jika fungsi di views.py perlu mengambil atau menyimpan data dari database, maka akan berinteraksi dengan model yang terdefinisi di models.py.  
* Model ini bertindak sebagai representasi data yang ada di database dan digunakan untuk melakukan query seperti mengambil, menambah, menghapus, atau memperbarui data.

4) **`berkas .html`**  
* Setelah data diproses oleh `views.py`, fungsi akan mengirimkan data tersebut ke berkas template HTML yang didefinisikan di direktori `templates`.  
* Template ini akan diisi dengan data dari context (misal: data dari model), dan hasil akhirnya adalah halaman HTML lengkap yang dikirimkan sebagai respon kepada client.

3. Jelaskan fungsi `git` dalam pengembangan perangkat lunak\!

Git adalah *version control system* yang membantu pengembang melacak perubahan kode, bekerja secara kolaboratif, dan mengelola versi perangkat lunak secara efektif. Dengan fitur branching dan merging, pengembang dapat bekerja pada fitur atau perbaikan bug secara terpisah sebelum digabungkan ke dalam kode utama. Git juga memungkinkan pemulihan versi sebelumnya, menyimpan backup kode secara otomatis, dan mendukung integrasi dengan alat *Continuous Integration/Continuous Deployment* untuk pengujian otomatis. Selain itu, Git memfasilitasi review kode dan penyelesaian konflik saat pengembang bekerja secara bersamaan pada proyek yang sama.

4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

Django sering dijadikan platform bagi pemula untuk pembelajaran pengembangan perangkat lunak karena kesederhanaannya dan strukturnya yang jelas, memudahkan pemula memahami konsep fundamental pengembangan web. Django menggunakan arsitektur Model-View-Template (MVT) yang mudah dipahami oleh pemula dan membantu mengajarkan konsep-konsep dasar dalam pemisahan logika bisnis, data, dan tampilan. Django memiliki "batteries-included" approach, artinya framework ini sudah menyediakan berbagai fitur bawaan seperti autentikasi, routing, dan ORM (Object-Relational Mapping), sehingga pemula tidak perlu mengkonfigurasi terlalu banyak komponen dari awal. Selain itu, Django memiliki dokumentasi yang sangat lengkap dan komunitas besar, yang memudahkan belajar dan mendapatkan dukungan. Django memungkinkan pengembang untuk membangun aplikasi yang scalable dan maintainable, yang memberikan pemahaman nyata tentang praktik terbaik dalam pengembangan perangkat lunak.

5. Mengapa model pada Django disebut sebagai *ORM*?

Model pada Django disebut sebagai ORM (Object-Relational Mapping) karena Django menyediakan mekanisme yang memungkinkan pengembang untuk bekerja dengan database menggunakan objek Python, tanpa harus menulis SQL secara langsung. ORM menghubungkan kelas-kelas dalam Python dengan tabel di database, sehingga setiap instance dari model merepresentasikan satu baris data di tabel tersebut. Dengan Django ORM, pengembang dapat melakukan operasi seperti *create*, *read*, *update*, dan *delete* (CRUD) menggunakan metode Python, dan ORM akan menerjemahkannya menjadi perintah SQL.

# Tugas Individu 3

1. **Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**  
   Data delivery menjadi komponen penting dalam sebuah platform karena memfasilitasi pertukaran informasi, meningkatkan kinerja, menjaga keamanan, memastikan skalabilitas, mendukung integrasi dengan sistem lain, dan membantu dalam pengambilan keputusan berbasis data. Sebuah platform yang tidak memiliki mekanisme data delivery yang baik akan mengalami masalah seperti keterlambatan, ketidakamanan, serta gangguan layanan, yang semuanya berdampak pada pengalaman pengguna dan keberhasilan platform itu sendiri.  
     
2. **Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**  
   Menurut saya, JSON lebih baik digunakan dibandingkan dengan XML. Secara syntax, JSON lebih sederhana dan lebih mudah dibaca oleh manusia serta mesin dibandingkan XML, sehingga menghasilkan data yang lebih kecil karena tidak memerlukan tag penutup seperti XML. JSON menggunakan struktur data yang lebih langsung seperti objek, array, angka, string, dll., yang mirip dengan struktur data di banyak bahasa pemrograman modern, terutama JavaScript. Sedangkan XML memiliki struktur yang lebih panjang dan detail karena memerlukan tag pembuka dan penutup, sehingga menghasilkan file yang lebih besar dan lebih sulit dibaca. Secara kinerja, JSON lebih cepat diproses karena memiliki struktur yang lebih sederhana dan secara native didukung oleh JavaScript, yang banyak digunakan dalam pengembangan web modern, sedangkan XML  memerlukan parsing yang lebih kompleks karena strukturnya yang berhirarki dan tag yang panjang. Dalam pengembangan web dan API modern, JSON sangat populer digunakan karena efisiensi dalam pertukaran data, terutama dalam arsitektur RESTful. XML masih digunakan di beberapa domain yang memerlukan markup lebih kompleks atau formal ( (misalnya, protokol SOAP, RSS feeds, dll).   
     
3. **Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?**  
   Fungsi dari method `is_valid()` pada form Django digunakan untuk memvalidasi isi input dari form tersebut. Hal ini penting untuk dilakukan untuk memastikan bahwa data yang diterima aman dan sesuai dengan format yang diharapkan sebelum diproses lebih lanjut, sehingga kita bisa yakin bahwa data yang disimpan atau diproses akan konsisten dan bebas dari kesalahan input.

4. **Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**  
   `csrf_token` adalah token yang berfungsi sebagai security. Token ini di-generate secara otomatis oleh Django untuk mencegah serangan berbahaya. Jika `csrf_token` tidak disertakan di dalam form, aplikasi Django menjadi rentan terhadap serangan CSRF. CSRF itu sendiri adalah jenis serangan di mana penyerang memanfaatkan autentikasi yang sudah ada (seperti *cookie* sesi yang sah) untuk membuat *request* palsu dari browser pengguna tanpa sepengetahuan pengguna tersebut. Oleh karena itu, `csrf_token` digunakan untuk memastikan bahwa permintaan (*request*) yang dikirim ke server berasal dari sumber yang sah, yakni dari pengguna yang benar-benar sedang menggunakan aplikasi tersebut. Ketika pengguna mengirimkan form melalui *request* POST, Django memeriksa apakah token CSRF yang dikirimkan bersamaan dengan form cocok dengan token yang disimpan di sesi pengguna. Jika token cocok, maka *request* dianggap sah dan diproses lebih lanjut oleh server. Jika tidak, Django akan memblokir *request* tersebut.

   Jika `csrf_token` tidak disertakan di dalam form, aplikasi Django berpotensi besar menjadi sasaran serangan CSRF. Contohnya, dalam aplikasi web yang memiliki fungsi seperti mengubah kata sandi, mentransfer uang, atau menghapus akun, jika tidak ada `csrf_token`,  maka penyerang bisa membuat *request* yang tampak sah (karena mereka menggunakan *cookie* sesi sah pengguna) dan mengirimkan *request* POST untuk mengeksploitasi sesi pengguna yang sudah login dan melakukan tindakan yang tidak diinginkan, seperti pengubahan data atau transaksi keuangan tanpa sepengetahuan pengguna. 

   Cara penyerang memanfaatkannya:  
* Penyerang membuat halaman web berbahaya yang memuat kode HTML atau JavaScript yang mengirimkan *request* POST ke situs web target (di mana pengguna sudah login).  
* Pengguna yang terautentikasi mengunjungi situs penyerang: Karena browser pengguna sudah menyimpan *cookie* sesi (*login*) untuk situs web yang sah, *request* dari halaman penyerang akan menyertakan *cookie* sesi yang sah ke server situs web tersebut.  
* *Request* diterima dan dieksekusi tanpa divalidasi, sehingga tindakan berbahaya seperti penghapusan akun, perubahan kata sandi, atau transfer dana bisa terjadi.  
    
5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**  
* **Membuat input form untuk menambahkan objek model pada app sebelumnya**  
  Langkah pertama yang saya lakukan adalah membuat berkas baru bernama `form.py` pada direktori `main` untuk membuat struktur form yang dapat menambahkan data Product Entry baru. Kemudian, saya mengisi berkas tersebut dengan kode sebagai berikut:  
  `from django.forms import ModelForm`  
  `from main.models import ProductEntry`  
    
  `class ProductEntryForm(ModelForm):`  
      `class Meta:`  
          `model = ProductEntry`  
          `fields = ["name", "price"]`  
    
  Setelah itu, saya memodifikasi berkas `views.py` pada direktori main dengan mengimpor beberapa fungsi:  
  `from django.shortcuts import render, redirect`     
  `from main.forms import ProductEntryForm`  
  `from main.models import ProductEntry`  
    
  Selanjutnya, saya membuat fungsi baru bernama `create_produt_entry` yang menerima parameter *request*. Fungsi tersebut saya isi dengan kode di bawah ini untuk menghasilkan form yang dapat menambahkan data *Product Entry* secara otomatis ketika data di-submit dari form.  
  `def create_product_entry(request):`  
      `form = ProductEntryForm(request.POST or None)`  
    
      `if form.is_valid() and request.method == "POST":`  
          `form.save()`  
          `return redirect('main:show_main')`  
    
      `context = {'form': form}`  
      `return render(request, "create_product_entry.html", context)`  
    
  Kemudian, saya menambahkan `'product_entries': product_entries` di dalam variabel context yang berada di fungsi `show_main`. Pada berkas `urls.py`, saya melakukan import fungsi dari `main.views` dan menambahkan rute URL `path('create-product-entry',create_product_entry,name='create_product_entry'),` di variabel `urlpatterns` pada `views.py` di direktori main untuk mengakses fungsi yang sudah di-import pada poin sebelumnya. Selanjutnya, saya membuat berkas HTML baru dengan nama `create_product_entry.html` pada direktori `main/templates`. Isi berkas `create_product_entry.html` adalah kode berikut:  
  `{% extends 'base.html' %}`   
  `{% block content %}`  
  `<h1>Add New Product Entry</h1>`  
    
  `<form method="POST">`  
    `{% csrf_token %}`  
    `<table>`  
      `{{ form.as_table }}`  
      `<tr>`  
        `<td></td>`  
        `<td>`  
          `<input type="submit" value="Add Product Entry" />`  
        `</td>`  
      `</tr>`  
    `</table>`  
  `</form>`  
    
  `{% endblock %}`  
    
  Lalu, saya menambahkan kode di bawah ini pada berkas `main.html` di dalam `{% block content %}` untuk menampilkan data produk dalam bentuk tabel serta tombol `Add New Product Entry` yang akan redirect ke halaman form. Kode yang saya tambahkan adalah sebagai berikut:  
  `{% if not product_entries %}`  
  `<p>Belum ada data produk pada Shopeeta.</p>`  
  `{% else %}`  
  `<table>`  
    `<tr>`  
      `<th>Product Name</th>`  
      `<th>Time</th>`  
      `<th>Price</th>`  
    `</tr>`  
    
    `{% comment %} Berikut cara memperlihatkan data produk di bawah baris ini`   
    `{% endcomment %}`   
    `{% for product_entry in product_entries %}`  
    `<tr>`  
      `<td>{{product_entry.name}}</td>`  
      `<td>{{product_entry.time}}</td>`  
      `<td>{{product_entry.price}}</td>`  
    `</tr>`  
    `{% endfor %}`  
  `</table>`  
  `{% endif %}`  
    
  `<br />`  
    
  `<a href="{% url 'main:create_product_entry' %}">`  
    `<button>Add New Product Entry</button>`  
  `</a>`  
    
* **Menambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID**  
  Pertama-tama, saya menambahkan import `HttpResponse` dan `Serializer` pada bagian paling atas pada berkas views.py yang ada pada direktori main. Setelah itu, saya membuat 2 fungsi baru yang menerima parameter *request* dengan nama `show_xml` dan `show_json`. Fungsi show\_xml digunakan untuk mengembalikan data dalam bentuk XML, sedangkan fungsi `show_json` untuk mengembalikan data dalam bentuk JSON. Di dalam masing-masing fungsi tersebut saya membuat variabel yang menyimpan hasil *query* dari seluruh data yang ada pada *Product Entry*.  
  `data = ProductEntry.objects.all()`   
  *Return function* dari kedua fungsi ini berupa `HttpResponse` yang berisi parameter data hasil *query* yang sudah diserialisasi menjadi XML dan `parameter content_type="application/xml"` serta menjadi JSON dan parameter content\_type="application/json".   
    
  Selanjutnya, saya membuat 2 fungsi baru lagi yang menerima parameter *request* dan id dengan nama `show_xml_by_id` dan `show_json_by_id`. Kedua fungsi tersebut digunakan untuk mengembalikan data berdasarkan ID dalam bentuk XML dan JSON. Di kedua fungsi tersebut saya juga membuat variabel yang menyimpan hasil *query* dari data dengan id tertentu yang ada pada ProductEntry.   
  `data = ProductEntry.objects.filter(pk=id)`  
  *Return function* berupa `HttpResponse` yang berisi parameter data hasil *query* yang sudah diserialisasi menjadi JSON atau XML dan parameter content\_type dengan value "`application/xml`" (untuk format XML) atau "`application/json`" (untuk format JSON).  
    
* **Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2**  
  Pada berkas urls.py yang ada di direktori main, saya import fungsi-fungsi yang telah saya buat pada berkas views.py.   
  `from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id`  
  Kemudian, saya mendaftarkan keempat path URL fungsi tersebut pada urlpatterns agar bisa diakses.   
  `...`  
  `path('xml/', show_xml, name='show_xml'),`  
  `path('json/', show_json, name='show_json'),`  
  `path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),`  
  `path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),`  
  `...`

**Hasil Akses Keempat Url Pada Postman**

* http://localhost:8000/xml

![][image2]

* http://localhost:8000/json

![][image3]

* http://localhost:8000/xml/8616b925-3bf7-4354-9cbf-d418ae2a715f

![][image4]

*  http://localhost:8000/json/8616b925-3bf7-4354-9cbf-d418ae2a715f

![][image5]

# Tugas Individu 4

1. **Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`**  
   **`HttpResponseRedirect()`**`:`  
* merupakan kelas dalam Django yang digunakan untuk membuat respons pengalihan secara manual.  
* perlu memberikan URL tujuan secara eksplisit saat digunakan.  
* hanya menerima **string URL** sebagai parameter.  
* memerlukan penulisan URL penuh secara manual, sehingga sedikit kurang efisien saat bekerja dengan URL yang dinamis atau terdaftar.  
* cocok digunakan ketika ingin memberikan kontrol penuh atas URL yang akan digunakan untuk pengalihan.

**`redirect()`**: 

* **`redirect()`** adalah fungsi utilitas (shortcut) yang disediakan oleh Django untuk mempermudah pembuatan pengalihan.  
* lebih fleksibel, karena bisa menerima **string URL, nama URL (dari `urls.py`), atau objek model** yang memiliki metode `get_absolute_url()`.  
* lebih mudah digunakan karena dapat menerima nama URL atau objek model secara langsung, yang secara otomatis diterjemahkan ke URL.  
* pilihan yang lebih praktis dan efisien, terutama ketika kita ingin mengalihkan ke URL yang dinamis atau memanfaatkan URL yang telah terdaftar dalam aplikasi.

2. **Jelaskan cara kerja penghubungan model `Product` dengan `User`\!**  
   Penghubungan model `Product` dengan `User` di Django biasanya dilakukan dengan menggunakan relasi database yang memungkinkan untuk menghubungkan objek dari dua model berbeda. Umumnya, penghubungan ini dilakukan dengan *ForeignKey, ManyToManyField*, atau *OneToOneField*, tergantung pada jenis relasi yang diinginkan.

   Berikut ini adalah penjelasan cara kerja salah satu jenis relasi penghubungan model `Product` dengan `User`, yaitu ***ForeignKey*** (relasi satu-ke-banyak):  
1) Mendefinisikan Model `Product` dan `User`  
   Django memiliki model `User` yang telah disediakan oleh modul `django.contrib.auth.models`. Model ini bisa dihubungkan ke model lain, seperti `Product`, yang kita buat sendiri. Misalkan, setiap produk (`Product`) memiliki pemilik atau pembuat produk yang merupakan pengguna (`User`). Berikut potongan kode untuk mengimpor modul tersebut.  
   `...`  
   `from django.contrib.auth.models import User`  
   `...`  
2) Menghubungkan Model `Product` dengan `User` menggunakan `ForeignKey` Untuk menghubungkan model `Product` ke `User`, kita dapat menggunakan `ForeignKey` di model `Product`. Ini menciptakan relasi **satu-ke-banyak** di mana satu `User` dapat memiliki banyak `Product`, tetapi setiap `Product` hanya dimiliki oleh satu `User`. Berikut adalah contoh kode yang menunjukkan bagaimana cara kerja penghubungan tersebut pada berkas `models.py` di subdirektori `main`:  
   `from django.db import models`  
   `from django.contrib.auth.models import User`  
   `import uuid`  
   `class ProductEntry(models.Model):`  
   	`user = models.ForeignKey(User, on_delete=models.CASCADE)`  
   	`id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)`  
   	`name = models.CharField(max_length=255)`  
   	`price = models.IntegerField()`  
   	`description = models.TextField()`  
   	`time = models.DateField(auto_now_add=True)`  
* **Penjelasan kode:**  
  `ForeignKey(User, on_delete=models.CASCADE)` yang digunakan pada kode di atas berfungsi untuk menghubungkan `model Product` dengan `model User.` Kemudian, potongan kode `on_delete=models.CASCADE` berarti jika pengguna `(User)` dihapus, semua produk `(Product)` yang dimiliki pengguna tersebut juga akan dihapus.  
3) Cara Kerja di Database  
   Setelah kita mendefinisikan relasi ini, Django akan membuat kolom tambahan (`user`) di tabel `Product` yang menyimpan referensi ke `User`. Kolom ini akan berisi ID dari `User` yang menjadi pemilik produk.  
4) Modifikasi berkas `views.py`  
   Pada berkas `views.py` yang ada pada subdirektori main, lakukan modifikasi kode pada fungsi `create_product_entry` menjadi sebagai berikut:  
   `def create_product_entry(request):`  
       `form = ProductEntryForm(request.POST or None)`  
       `if form.is_valid() and request.method == "POST":`  
   	   `product_entry = form.save(commit=False)`  
   	   `product_entry.user = request.user`  
   	   `form.save()`  
   	   `return redirect('main:show_main')`  
       `context = {'form': form}`

       `return render(request, "create_product_entry.html", context)`  
   **Penjelasan Kode:**  
   Parameter `commit=False` yang digunakan pada potongan kode diatas berguna untuk mencegah Django agar tidak langsung menyimpan objek yang telah dibuat dari `form` langsung ke database. Hal tersebut memungkinkan kita untuk memodifikasi terlebih dahulu objek tersebut sebelum disimpan ke database. Pada kasus ini, kita akan mengisi field `user` dengan objek `User` dari *return value* `request.user`. Penggunaan `request.user` bertujuan agar ketika pengguna menambahkan produk baru, produk tersebut sudah terotorisasi dengan pengguna yang sedang *login*.   
5) Melakukan filterisasi produk berdasarkan pengguna  
   Ubahlah *value* dari `product_entries` dan `context` pada fungsi `show_main` menjadi seperti berikut.  
   `def show_main(request):`  
       `product_entries = ProductEntry.objects.filter(user=request.user)`  
       `context = {`  
           `'name': request.user.username,`  
            `...`  
       `}`  
   `...`  
     
   **Penjelasan kode:**  
   Kode tersebut berfungsi untuk menampilkan objek `Product Entry` yang terkait dengan pengguna yang sedang *login*. Hal ini dilakukan dengan memfilter seluruh objek dan hanya mengambil Product Entry di mana field `user` diisi dengan objek `User` yang sama dengan pengguna yang sedang *login*.  
3. **Apa perbedaan antara *authentication* dan *authorization*, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.**  
   Perbedaan antara *authentication* dan *authorization* adalah sebagai berikut:  
1. *Authentication* (Otentikasi):  
   *Authentication* adalah proses memverifikasi identitas pengguna. Ini memastikan bahwa pengguna adalah siapa yang mereka klaim. Dalam konteks aplikasi, ini seringkali berarti memverifikasi kredensial pengguna seperti *username* dan *password*. Contohnya**,** saat pengguna memasukkan *username* dan *password* di halaman login, aplikasi memverifikasi apakah kredensial tersebut cocok dengan yang tersimpan di database.  
   Di Django, otentikasi biasanya dilakukan dengan memvalidasi kredensial pengguna melalui fungsi bawaan Django seperti `authenticate()` dan `login()`.  
2. *Authorization* (Otorisasi):  
   *Authorization* adalah proses menentukan apakah pengguna yang sudah terotentikasi memiliki izin atau hak untuk mengakses sumber daya tertentu atau melakukan aksi tertentu. Ini mengontrol akses pengguna berdasarkan peran atau izin yang diberikan kepada mereka. Contohnya, setelah pengguna berhasil login, otorisasi memutuskan apakah mereka memiliki hak untuk mengakses halaman admin, melihat data tertentu, atau melakukan tindakan seperti mengedit atau menghapus konten.  
   Di Django, otorisasi diimplementasikan melalui *permissions* dan *groups*, yang menentukan akses apa yang dimiliki pengguna. Django juga memiliki dekorator seperti `@login_required` dan `@permission_required` untuk membatasi akses.

Saat pengguna login, Django melakukan langkah-langkah berikut:

1) *Authentication*: Django memverifikasi apakah kredensial yang dimasukkan (username dan password) cocok dengan yang ada di database menggunakan metode `authenticate()`.  
2) Jika otentikasi berhasil, Django menggunakan metode `login()` untuk menyimpan informasi pengguna di sesi.  
3) *Authorization*: Setelah pengguna berhasil login, setiap permintaan berikutnya dapat dicek apakah pengguna memiliki hak untuk mengakses halaman tertentu berdasarkan izin atau peran mereka. Django mengelola izin melalui model `User` dan `Permissions`.

Cara Django mengimplementasikan authentication dan authorization secara keseluruhan adalah: 

* **User Model**: Model `User` adalah pusat dari kedua proses otentikasi dan otorisasi. Ini menyimpan semua informasi penting terkait pengguna, seperti username, password (yang di-hash), dan informasi izin serta grup.  
* **Sessions**: Django mengelola otentikasi melalui sesi. Setelah pengguna login, Django menyimpan status otentikasi dalam sesi, memungkinkan pengguna untuk tetap login selama sesi berlangsung.  
* **Middleware**: Django menggunakan middleware untuk memeriksa apakah pengguna yang mengirimkan permintaan telah terotentikasi atau tidak. Jika pengguna terotentikasi, permintaan ini akan diproses, jika tidak, pengguna diarahkan ke halaman login.  
* **Permissions dan Groups**: Django memudahkan kontrol otorisasi menggunakan izin default dan kustom serta grup yang memungkinkan pembagian izin kepada banyak pengguna sekaligus.

4. **Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari *cookies* dan apakah semua cookies aman digunakan?**  
   Django mengingat pengguna yang telah login menggunakan session yang disimpan melalui cookies. Ini memungkinkan Django untuk melacak status otentikasi pengguna antara berbagai permintaan HTTP (*stateless*). Saat pengguna login ke aplikasi Django, Django membuat session untuk pengguna. Setiap pengguna yang berhasil login diberikan sebuah ID sesi unik, yang disimpan di dalam cookie browser. Cookie ini dikirim bersama setiap permintaan pengguna ke server, sehingga server dapat mengenali pengguna tersebut di antara permintaan yang berbeda. 

   **Langkah-Langkahnya:**  
1) Setelah pengguna memasukkan kredensial (*username* dan *password*) dan Django berhasil mengautentikasi mereka, Django membuat entri sesi di server dengan ID sesi unik.  
2) Django menyimpan ID sesi di dalam cookie pengguna. Cookie ini disebut `sessionid` secara default.  
3) Pada setiap permintaan berikutnya dari pengguna, browser secara otomatis mengirimkan cookie `sessionid` ini ke server.  
4) Django memeriksa ID sesi di cookie tersebut dan mencocokkannya dengan entri sesi di server untuk mengidentifikasi pengguna.

Kegunaan lain dari Cookies antara lain:

* **Menyimpan Preferensi Pengguna**  
  Cookies dapat digunakan untuk menyimpan informasi seperti bahasa yang dipilih pengguna atau pengaturan tampilan situs, sehingga situs dapat memberikan pengalaman yang dipersonalisasi.  
* **Pelacakan dan Analitik**  
  Cookies sering digunakan untuk melacak perilaku pengguna di situs web guna mengumpulkan data statistik untuk analitik, iklan yang dipersonalisasi, atau pengoptimalan situs.  
* **Keranjang Belanja**  
  Pada e-commerce, cookies dapat digunakan untuk menyimpan informasi sementara seperti item yang dimasukkan pengguna ke dalam keranjang belanja.  
* **Otentikasi Berkelanjutan (Remember Me)**  
  Cookies juga dapat digunakan untuk mengingat pengguna yang telah memilih opsi "Ingat saya" di form login, sehingga mereka tidak perlu login kembali dalam waktu tertentu.

Namun sayangnya, tidak semua cookies aman dari serangan siber. Cookies tanpa atribut `Secure` atau `HttpOnly` rentan terhadap pencurian atau manipulasi oleh penyerang, terutama jika digunakan dalam koneksi yang tidak terenkripsi (HTTP). Selain itu, Cookies yang disimpan terlalu lama tanpa pengaturan masa berlaku yang baik juga dapat menjadi risiko keamanan karena dapat digunakan untuk serangan di kemudian hari. Namun, hal tersebut dapat kita proteksi dengan menggunakan `Secure`, `HttpOnly`, dan `SameSite`. Selain itu, pada keamanan Cookies di Django terdapat beberapa rekomendasi yang dapat dilakukan:

* Menggunakan HTTPS agar semua komunikasi, termasuk cookies, dienkripsi.  
* Aktifkan `SESSION_COOKIE_SECURE` di Django untuk memastikan bahwa cookie sesi hanya dikirimkan melalui koneksi HTTPS  
* Aktifkan `SESSION_COOKIE_HTTPONLY` untuk melindungi cookie sesi dari akses JavaScript  
* Menggunakan `csrf_token` yang disediakan Django untuk melindungi dari serangan CSRF  
  Hal-hal di atas dapat meningkatkan keamanan cookies dari serangan yang umum seperti *session hijacking* atau XSS.

5. **Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial).**  
* **Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.**   
  * Fungsi registrasi

  Langkah pertama yang saya lakukan adalah mengaktifkan virtual environment pada terminal. Setelah itu, saya menambahkan *import* `UserCreationForm` dan `messages` pada bagian paling atas di berkas `views.py` yang ada pada subdirektori main. 

  `from django.contrib.auth.forms import UserCreationForm`

  `from django.contrib import messages`

  Kemudian, saya menambahkan fungsi baru yaitu fungsi `register` ke dalam `views.py` untuk menghasilkan formulir registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-*submit* dari form.

  `def register(request):`

      `form = UserCreationForm()`


      `if request.method == "POST":`

          `form = UserCreationForm(request.POST)`

          `if form.is_valid():`

              `form.save()`

              `messages.success(request, 'Your account has been successfully created!')`

              `return redirect('main:login')`

      `context = {'form':form}`

      `return render(request, 'register.html', context)`

  Selanjutnya, saya membuat berkas HTML baru bernama `register.html` pada direktori `main/templates`. Isi dari `register.html` adalah:

  `{% extends 'base.html' %}`


  `{% block meta %}`

  `<title>Register</title>`

  `{% endblock meta %}`


  `{% block content %}`


  `<div class="login">`

    `<h1>Register</h1>`


    `<form method="POST">`

      `{% csrf_token %}`

      `<table>`

        `{{ form.as_table }}`

        `<tr>`

          `<td></td>`

          `<td><input type="submit" name="submit" value="Daftar" /></td>`

        `</tr>`

      `</table>`

    `</form>`


    `{% if messages %}`

    `<ul>`

      `{% for message in messages %}`

      `<li>{{ message }}</li>`

      `{% endfor %}`

    `</ul>`

    `{% endif %}`

  `</div>`


  `{% endblock content %}`

  Setelah itu, saya impor fungsi register pada berkas `urls.py` yang ada pada subdirektori `main` dan menambahkan path url ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.

  `from main.views import register`

  `urlpatterns = [`

       `...`

       `path('register/', register, name='register'),`

   `]`

  * Fungsi login

  Langkah berikutnya adalah menambahkan *import* `authenticate`, `login`, dan `AuthenticationForm` pada bagian paling atas di berkas `views.py`. 

  `from django.contrib.auth.forms import UserCreationForm, AuthenticationForm`

  `from django.contrib.auth import authenticate, login`

  Masih di berkas yang sama, saya menambahkan fungsi `login_user`. Fungsi ini berfungsi untuk mengautentikasi pengguna yang ingin *login*.

  `def login_user(request):`

     `if request.method == 'POST':`

        `form = AuthenticationForm(data=request.POST)`


        `if form.is_valid():`

              `user = form.get_user()`

              `login(request, user)`

              `return redirect('main:show_main')`


     `else:`

        `form = AuthenticationForm(request)`

     `context = {'form': form}`

     `return render(request, 'login.html', context)`

  Setelah itu, saya membuat berkas HTML baru bernama `login.html` pada direktori `main/templates`. Isi dari `login.html` adalah sebagai berikut:

  `{% extends 'base.html' %}`


  `{% block meta %}`

  `<title>Login</title>`

  `{% endblock meta %}`


  `{% block content %}`

  `<div class="login">`

    `<h1>Login</h1>`


    `<form method="POST" action="">`

      `{% csrf_token %}`

      `<table>`

        `{{ form.as_table }}`

        `<tr>`

          `<td></td>`

          `<td><input class="btn login_btn" type="submit" value="Login" /></td>`

        `</tr>`

      `</table>`

    `</form>`


    `{% if messages %}`

    `<ul>`

      `{% for message in messages %}`

      `<li>{{ message }}</li>`

      `{% endfor %}`

    `</ul>`

    `{% endif %} Don't have an account yet?`

    `<a href="{% url 'main:register' %}">Register Now</a>`

  `</div>`


  `{% endblock content %}`

  Kemudian impor fungsi `login_user` pada berkas `urls.py` dan saya menambahkan path url ke dalam `urlpatterns` untuk mengakses fungsi yang diimpor tersebut.

  `...`

  `from main.views import login_user`


  `urlpatterns = [`

     `...`

     `path('login/', login_user, name='login'),`

  `]`

  * Fungsi registrasi

  Selanjutnya adalah membuat fungsi *logout*. Saya menambahkan import `logout` pada bagian paling atas di berkas `views.py` yang ada di subdirektori main. 

  `from django.contrib.auth import logout`


  Lalu, saya menambahkan fungsi di bawah ini ke dalam fungsi `views.py` untuk melakukan mekanisme *logout*.

  `def logout_user(request):`

      `logout(request)`

      `return redirect('main:login')`

  Pada berkas `main.html` yang ada pada direktori `main/templates`, saya menambahkan potongan kode di bawah ini setelah *hyperlink tag* untuk Add New Product Entry.

  `...`

  `<a href="{% url 'main:logout' %}">`

    `<button>Logout</button>`

  `</a>`

  `...`

  Kemudian impor fungsi `logout_user` pada berkas `urls.py` dan saya menambahkan path url ke dalam `urlpatterns` untuk mengakses fungsi yang diimpor tersebut.

  `...`

  `from main.views import logout_user`


  `urlpatterns = [`

     `...`

     `path('logout/', logout_user, name='logout'),`

  `]`

  * Merestriksi Akses Halaman Main

  Pada berkas `views.py` yang ada pada subdirektori `main`, saya menambahkan import `login_required` pada bagian paling atas.

  from django.contrib.auth.decorators import login\_required

  Setelah itu, tambahkan potongan kode `@login_required(login_url='/login')` di atas fungsi `show_main` agar halaman `main` hanya dapat diakses oleh pengguna yang sudah login (terautentikasi).

  `...`

  `@login_required(login_url='/login')`

  `def show_main(request):`

  `...`

* **Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.**  
    
* **Menghubungkan model Product dengan User.**  
  Langkah pertama yang saya lakukan adalah menambahkan kode berikut pada dibawah baris kode untuk mengimpor model pada berkas `models.py` yang ada pada subdirektori `main`:  
  `...`  
  `from django.contrib.auth.models import User`  
  `...`  
  Pada model `ProductEntry` yang sudah dibuat, tambahkan potongan kode berikut:  
  `class ProductEntry(models.Model):`  
      `user = models.ForeignKey(User, on_delete=models.CASCADE)`  
      `...`  
  Kemudian, ubah potongan kode pada fungsi `create_product_entry` pada berkas `views.py` yang ada pada subdirektori main menjadi sebagai berikut:  
  `def create_product_entry(request):`  
      `form = ProductEntryForm(request.POST or None)`  
    
      `if form.is_valid() and request.method == "POST":`  
          `product_entry = form.save(commit=False)`  
          `product_entry.user = request.user`  
          `form.save()`  
          `return redirect('main:show_main')`  
    
      `context = {'form': form}`  
      `return render(request, "create_product_entry.html", context)`  
  Ubahlah *value* dari `product_entries` dan `context` pada fungsi `show_main` menjadi seperti berikut.  
  `def show_main(request):`  
      `product_entries = ProductEntry.objects.filter(user=request.user)`  
      `context = {`  
          `'name': request.user.username,`  
           `...`  
      `}`  
  `...`  
  Simpan semua perubahan, dan saya melakukan migrasi model dengan `python manage.py makemigrations`. Nantinya, akan muncul error saat melakukan migrasi model dan disajikan 2 pilihan. Pilih nomor 1 untuk menetapkan *default value* untuk *field user* pada semua *row* yang telah dibuat pada *database*. Lalu, ketik angka 1 lagi untuk menetapkan user dengan ID 1 (yang sudah kita buat sebelumnya) pada model yang sudah ada.  
  Selanjutnya, jalankan `python manage.py` migrate untuk mengaplikasikan migrasi yang dilakukan pada poin sebelumnya. Langkah terakhir, kita harus mempersiapkan aplikasi web kita untuk *environment production*. Untuk itu, tambahkan sebuah import baru pada `settings.py` yang ada pada subdirektori `eshop`.  
  `import os`  
  Kemudian, ganti variabel `DEBUG` dari berkas `settings.py` menjadi seperti berikut.  
  `PRODUCTION = os.getenv("PRODUCTION", False)`  
  `DEBUG = not PRODUCTION`  
* **Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.**  
  Untuk menampilkan detail informasi pengguna yang sedang *logged in*, langkah pertama yang saya lakukan adalah *logout* terlebih dahulu apabila sedang menjalankan aplikasi Django. Setelah itu, saya menambahkan import `HttpResponseRedirect`, `reverse`, dan `datetime` pada bagian paling atas di berkas `views.py` yang ada pada subdirektori main.  
  `import datetime`  
  `from django.http import HttpResponseRedirect`  
  `from django.urls import reverse`  
  Pada fungsi `login_user`, saya menambahkan fungsionalitas dengan menambahkan cookie yang bernama `last_login` untuk melihat kapan terakhir kali pengguna melakukan login. Saya mengganti kode yang ada pada blok `if form.is_valid()` menjadi potongan kode berikut.  
  `...`  
  `if form.is_valid():`  
      `user = form.get_user()`  
      `login(request, user)`  
      `response = HttpResponseRedirect(reverse("main:show_main"))`  
      `response.set_cookie('last_login', str(datetime.datetime.now()))`  
      `return response`  
  `...`  
  Kemudian, pada fungsi `show_main`, tambahkan potongan kode `'last_login': request.COOKIES['last_login']` ke dalam variabel `context`.   
  `context = {`  
          `'name': request.user.username,`  
          `'application' : 'Shopeeta',`  
          `'name' : 'Dandi Apriyansyah',`  
          `'class' : 'PBP A',`  
          `'product_entries': product_entries,`  
          `'last_login': request.COOKIES['last_login'],`  
         `}`  
  Setelah itu, saya memodifikasi fungsi `logout_user` menjadi seperti potongan kode berikut.  
  `def logout_user(request):`  
      `logout(request)`  
      `response = HttpResponseRedirect(reverse('main:login'))`  
      `response.delete_cookie('last_login')`  
      `return response`  
  Modifikasi berkas main.html dengan menambahkan potongan kode berikut di setelah tombol `logout` untuk menampilkan data *last login*.  
  `...`  
  `<h5>Sesi terakhir login: {{ last_login }}</h5>`  
  `...`  
  Langkah terakhir adalah *refresh* halaman *login* (atau jalankan dengan perintah `python manage.py runserver` jika kamu belum menjalankan proyekmu) dan cobalah untuk *login*. Data last login kamu akan muncul di halaman main. 

# Tugas Individu 5

1. **Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut\!**  
1) Inline styles (anything inside a style tag)   
   Inline styles yang ditulis langsung pada elemen HTML memiliki prioritas tertinggi. Inline styles didefinisikan langsung dalam atribut `style` elemen. CSS ini akan memiliki prioritas tertinggi karena ditulis langsung pada elemen `<p>.`  
2) ID selectors  
   Selector yang menggunakan ID (`#id`) memiliki spesifisitas yang lebih tinggi dibandingkan classes selector dan elemen selector. CSS selector ini memiliki prioritas yang lebih kuat karena ID dalam satu halaman HTML harus unik.   
3) Classes selector  
   Selector yang menggunakan class (`.class`), pseudo-class (`:hover`, `:nth-child`), atau attribute selector (`[type="text"]`) berada di level prioritas berikutnya setelah ID selector. Jika ada konflik antara class, pseudo-class, atau attribute selector, maka aturan dengan selector yang lebih spesifik akan diterapkan.  
4) Element selector  
   Selector yang hanya menggunakan nama tag HTML (misalnya `div`, `p`, `a`) memiliki prioritas paling rendah dibandingkan yang lainnya. Mereka akan diterapkan hanya jika tidak ada selector lain yang lebih spesifik.  
     
2. **Mengapa *responsive design* menjadi konsep yang penting dalam pengembangan aplikasi *web*? Berikan contoh aplikasi yang sudah dan belum menerapkan *responsive design*\!**

Alasan responsive design menjadi konsep yang penting dalam pengembangan aplikasi web adalah sebagai berikut:

1. **Pengalaman Pengguna yang Konsisten di Berbagai Perangkat**  
   Responsive design memastikan tampilan yang optimal dan konsisten, baik pada perangkat mobile, tablet, maupun desktop. Pengguna dapat mengakses website tanpa harus melakukan zoom atau scroll secara horizontal, sehingga mereka dapat dengan mudah menavigasi dan membaca konten.  
2. **Meningkatkan Aksesibilitas**  
   Dengan responsive design, aplikasi web dapat diakses oleh lebih banyak orang di berbagai jenis perangkat. Ini mendukung inklusivitas, karena pengguna dengan berbagai perangkat (termasuk yang lebih tua atau berbeda resolusinya) tetap dapat menggunakan aplikasi tersebut dengan nyaman.  
3. **SEO dan Peringkat di Mesin Pencari**  
   Mesin pencari seperti Google memberi prioritas lebih tinggi kepada website yang responsive karena mereka memberikan pengalaman pengguna yang lebih baik. Dengan menerapkan responsive design, sebuah website dapat meningkatkan ranking SEO dan menarik lebih banyak traffic.  
4. **Efisiensi Biaya dan Waktu**  
   Responsive design menghilangkan kebutuhan untuk mengembangkan versi aplikasi yang terpisah untuk desktop dan mobile. Dengan satu basis kode dan desain yang fleksibel, aplikasi web bisa diakses di berbagai perangkat dengan menyesuaikan layout secara otomatis.  
5. **Adaptasi untuk Perangkat Masa Depan**  
   Seiring berkembangnya teknologi dan munculnya perangkat baru dengan berbagai ukuran layar, responsive design memastikan bahwa aplikasi web dapat beradaptasi dengan perangkat baru tanpa perlu perubahan besar.

Contoh aplikasi yang sudah menerapkan responsive design adalah X (Twitter), Airbnb, Google, Spotify, dan sebagainya. Sedangkan contoh aplikas yang belum menerapkan responsivr design adalah Situs Web Institusi Pemerintah Lama dan Situs Sekolah atau Universitas Lama.

3. **Jelaskan perbedaan antara *margin*, *border*, dan *padding*, serta cara untuk mengimplementasikan ketiga hal tersebut\!**  
1. Margin  
   Margin adalah jarak antara elemen dengan elemen lain di sekitarnya (spasi di luar border). Margin berfungsi untuk mengosongkan area di sekitar *border* (transparan) dan mengontrol ruang kosong antara elemen dengan elemen lainnya. Margin tidak mempengaruhi ukuran elemen itu sendiri.  
   \`\`\`python  
   `.element {`  
       `margin: 20px; /* Memberikan margin sebesar 20px di semua sisi */`  
   `}`

	\`\`\`

2. Border  
   Border adalah garis pembatas di sekitar elemen, yang berada di antara margin dan padding. Border berfungsi untuk memberikan visualisasi batas di sekitar elemen, bisa berupa garis dengan berbagai warna, gaya, dan ketebalan.  
   \`\`\`python  
   `.element {`  
       `border: 2px solid black; /* Memberikan border dengan ketebalan 2px, solid, dan warna hitam */`  
   `}`  
   \`\`\`  
3. Padding   
   Padding adalah ruang kosong antara konten elemen dan batas elemen (border). Padding berfungsi untuk mengontrol jarak antara konten elemen dengan border. Padding akan memperbesar ukuran elemen secara keseluruhan jika diberikan nilai tanpa mempengaruhi konten di dalamnya.  
   \`\`\`python  
   `.element {`  
       `padding: 10px; /* Memberikan padding sebesar 10px di semua sisi konten */`  
   `}`  
   \`\`\`  
4. **Jelaskan konsep *flex box* dan *grid layout* beserta kegunaannya\!**  
* Flexbox (Flexible Box Layout)

Flexbox adalah metode tata letak satu dimensi (one-dimensional layout), yang berarti bahwa elemen-elemen ditata dalam satu arah, baik itu sejajar secara horizontal (baris) atau vertikal (kolom). Flexbox memudahkan pengaturan posisi, ukuran, dan distribusi ruang antar elemen dalam sebuah kontainer, terutama ketika ukuran elemen tidak diketahui atau dinamis.

Kegunaan:

* Memudahkan pembuatan tata letak yang responsif.  
* Ideal untuk tata letak yang sederhana dan linear, seperti baris elemen navigasi, kartu, atau elemen daftar.  
* Flexbox sangat berguna ketika Anda memiliki konten yang bervariasi ukurannya, namun Anda ingin elemen-elemen tersebut tetap seimbang secara proporsional di dalam suatu kontainer.

*  CSS Grid Layout

CSS Grid adalah metode tata letak dua dimensi (two-dimensional layout), yang berarti elemen dapat disusun baik secara baris (horizontal) maupun kolom (vertikal). Grid memberikan kontrol yang lebih baik dan fleksibilitas lebih besar untuk tata letak halaman yang kompleks. Anda dapat membuat baris dan kolom dengan ukuran yang tetap atau dinamis, serta mengatur elemen agar melintasi beberapa baris atau kolom.

Kegunaan:

* Cocok untuk tata letak halaman yang lebih kompleks, seperti tata letak galeri, dashboard, atau halaman web dengan struktur grid yang kaku.  
* CSS Grid sangat berguna ketika Anda memiliki kontrol penuh atas struktur tata letak halaman dengan baris dan kolom yang teratur.  
* Fleksibel dalam mengatur ukuran kolom dan baris, serta elemen-elemen yang merentang beberapa baris atau kolom.

5. **Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial)\!**  
* **Implementasi fungsi untuk menghapus dan mengedit *product*.**  
  Langkah pertama yang saya lakukan adalah menambahkan fungsi baru bernama `edit_product` yang menerima parameter request dan id pada berkas views.py di direktori main.  Setelah itu, saya menambahkan import pada berkas views.py sebagai berikut:  
  \`\`\`python  
  `from django.shortcuts import .., reverse`  
  `from django.http import .., HttpResponseRedirect`  
  \`\`\`  
  Kemudian saya membuat berkas HTML baru bernama `edit_product.html` pada subdirektori `main/templates`. Isi berkas tersebut dengan template berikut.  
  \`\`\`python  
  `{% extends 'base.html' %}`  
  `{% load static %}`  
  `{% block meta %}`  
  `<title>Edit Product</title>`  
  `{% endblock meta %}`  
    
  `{% block content %}`  
  `{% include 'navbar.html' %}`  
  `<div class="flex flex-col min-h-screen bg-gray-100">`  
    `<div class="container mx-auto px-4 py-8 mt-16 max-w-xl">`  
      `<h1 class="text-3xl font-bold text-center mb-8 text-black">Edit Product Entry</h1>`  
      
      `<div class="bg-gray rounded-lg p-6 form-style">`  
        `<form method="POST" class="space-y-6">`  
            `{% csrf_token %}`  
            `{% for field in form %}`  
                `<div class="flex flex-col">`  
                    `<label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">`  
                        `{{ field.label }}`  
                    `</label>`  
                    `<div class="w-full text-black">`  
                        `{{ field }}`  
                    `</div>`  
                    `{% if field.help_text %}`  
                        `<p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>`  
                    `{% endif %}`  
                    `{% for error in field.errors %}`  
                        `<p class="mt-1 text-sm text-red-600">{{ error }}</p>`  
                    `{% endfor %}`  
                `</div>`  
            `{% endfor %}`  
            `<div class="flex justify-center mt-6">`  
                `<button type="submit" class="bg-indigo-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-indigo-700 transition duration-300 ease-in-out w-full">`  
                    `Edit Product Entry`  
                `</button>`  
            `</div>`  
        `</form>`  
    `</div>`  
    `</div>`  
  `</div>`  
  `{% endblock %}`  
  \`\`\`  
  Setelah membuat berkas tersebut, saya mengimpor fungsi `edit_product` yang sudah dibuat pada berkas urls.py dan menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi. Lalu, pada berkas `main.html` yang berada pada subdirektori `main/templates` saya menambahkan potongan kode berikut sejajar dengan elemen `<td>` terakhir agar terlihat tombol *edit* pada setiap baris tabel.  
  \`\`\`python  
  `...`  
  `<tr>`  
      `...`  
      `<td>`  
          `<a href="{% url 'main:edit_product' product_entry.pk %}">`  
              `<button>`  
                  `Edit`  
              `</button>`  
          `</a>`  
      `</td>`  
  `</tr>`  
  `...`  
  \`\`\`  
  Untuk menghapus product, kurang lebih cara yang saya terapkan sama. Pertama, saya menambahkan fungsi baru bernama `delete_product` yang menerima parameter request dan id pada berkas views.py di direktori main untuk mengaus data.  Setelah itu, saya menambahkan import pada berkas views.py sebagai berikut:  
  \`\`\`python  
  `from django.shortcuts import .., reverse`  
  `from django.http import .., HttpResponseRedirect`  
  \`\`\`  
  Kemudian saya membuat berkas HTML baru bernama `edit_product.html` pada subdirektori `main/templates`. Isi berkas tersebut dengan template berikut.  
  \`\`\`python  
  `def delete_product(request, id):`  
      `# Get product berdasarkan id`  
      `product = ProductEntry.objects.get(pk = id)`  
      `# Hapus product`  
      `product.delete()`  
      `# Kembali ke halaman awal`  
      `return HttpResponseRedirect(reverse('main:show_main'))`  
  \`\`\`  
  Setelah membuat berkas tersebut, saya mengimpor fungsi `delete_product` yang sudah dibuat pada berkas urls.py dan menambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang sudah diimpor tadi.   
    
* **Kustomisasi desain pada *template* HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework**  
  Sebelum kustomisasi desain pada aplikasi, saya melakukan konfigurasi *Static Files* pada Aplikasi. Pada berkas setting.py, saya menambahkan *middleware* WhiteNoise.  
  \`\`\`python  
  `...`  
  `MIDDLEWARE = [`  
      `'django.middleware.security.SecurityMiddleware',`  
      `'whitenoise.middleware.WhiteNoiseMiddleware', #Tambahkan tepat di bawah SecurityMiddleware`  
      `...`  
  `]`  
  `...`  
  \`\`\`  
  Dengan menambahkan *middleware* WhiteNoise pada `settings.py`, Django dapat menangani *file* statis secara otomatis saat berada dalam mode produksi `(DEBUG=False)` tanpa perlu pengaturan yang rumit. Ini penting agar file statis tetap dapat diakses dalam proses deployment, karena secara default, ketika `DEBUG=False`, Django tidak memberikan akses ke *file* statis. Kemudian, pada berkas `settings.py`, saya memastikan variabel `STATIC_ROOT`, `STATICFILES_DIRS`, dan `STATIC_URL` dikonfigurasikan seperti ini:  
  \`\`\`python  
  `...`  
  `STATIC_URL = '/static/'`  
  `if DEBUG:`  
      `STATICFILES_DIRS = [`  
          `BASE_DIR / 'static' # merujuk ke /static root project pada mode development`  
      `]`  
  `else:`  
      `STATIC_ROOT = BASE_DIR / 'static' # merujuk ke /static root project pada mode production`  
  `...`  
  \`\`\`  
  Selanjutnya, saya membuat berkas `global.css` di `/static/css` pada `root directory`. Lalu, saya menghubungkan `global.css` dan *script* Tailwind ke `base.html` dengan menambahkan berkas tersebut ke `base.html` `a`gar *style* CSS yang ditambahkan di `global.css` dapat digunakan dalam template Django. Modifikasi berkas `base.html` kamu seperti berikut:  
  \`\`\`python  
  `{% load static %}`  
  `<!DOCTYPE html>`  
  `<html lang="en">`  
    `<head>`  
      `<meta charset="UTF-8" />`  
      `<meta name="viewport" content="width=device-width, initial-scale=1.0" />`  
      `{% block meta %} {% endblock meta %}`  
      `<script src="https://cdn.tailwindcss.com"></script>`  
      `<link rel="stylesheet" href="{% static 'css/global.css' %}"/>`  
    `</head>`  
    `<body>`  
      `{% block content %} {% endblock content %}`  
    `</body>`  
  `</html>`  
  \`\`\`  
  * ***Styling*** **halaman Login** 

  Modifikasi `login.html` pada subdirektori `main/templates/` menjadi seperti berikut:

  \`\`\`python

  `{% extends 'base.html' %}`


  `{% block meta %}`

  `<title>Login</title>`

  `{% endblock meta %}`


  `{% block content %}`

  `<div class="min-h-screen flex items-center justify-center w-screen bg-teal-700 py-12 px-4 sm:px-6 lg:px-8">`

    `<div class="max-w-md w-full space-y-8">`

      `<div>`

        `<h2 class="mt-6 text-center text-white text-3xl font-extrabold text-gray-900">`

          `Login to your account`

        `</h2>`

      `</div>`

      `<form class="mt-8 space-y-6" method="POST" action="">`

        `{% csrf_token %}`

        `<input type="hidden" name="remember" value="true">`

        `<div class="rounded-md shadow-sm -space-y-px">`

          `<div>`

            `<label for="username" class="sr-only">Username</label>`

            `<input id="username" name="username" type="text" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-blue-900 focus:border-blue-900 focus:z-10 sm:text-sm" placeholder="Username">`

          `</div>`

          `<div>`

            `<label for="password" class="sr-only">Password</label>`

            `<input id="password" name="password" type="password" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-blue-900 focus:border-blue-900 focus:z-10 sm:text-sm" placeholder="Password">`

          `</div>`

        `</div>`


        `<div>`

          `<button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-blue-900 hover:bg-blue-950 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-900">`

            `Sign in`

          `</button>`

        `</div>`

      `</form>`


      `{% if messages %}`

      `<div class="mt-4">`

        `{% for message in messages %}`

        `{% if message.tags == "success" %}`

              `<div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">`

                  `<span class="block sm:inline">{{ message }}</span>`

              `</div>`

          `{% elif message.tags == "error" %}`

              `<div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">`

                  `<span class="block sm:inline">{{ message }}</span>`

              `</div>`

          `{% else %}`

              `<div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">`

                  `<span class="block sm:inline">{{ message }}</span>`

              `</div>`

          `{% endif %}`

        `{% endfor %}`

      `</div>`

      `{% endif %}`


      `<div class="text-center mt-4">`

        `<p class="text-sm text-white">`

          `Don't have an account yet?`

          `<a href="{% url 'main:register' %}" class="font-medium text-blue-900 hover:text-black">`

            `Register Now`

          `</a>`

        `</p>`

      `</div>`

    `</div>`

  `</div>`

  `{% endblock content %}`

  \`\`\`

  * ***Styling*** **halaman Register**

  Modifikasi `register.html` pada subdirektori `main/templates/` menjadi seperti berikut:

  \`\`\`python

  `{% extends 'base.html' %}`


  `{% block meta %}`

  `<title>Register</title>`

  `{% endblock meta %}`


  `{% block content %}`

  `<div class="min-h-screen flex items-center justify-center bg-teal-700 py-12 px-4 sm:px-6 lg:px-8">`

    `<div class="max-w-md w-full space-y-8 form-style">`

      `<div>`

        `<h2 class="mt-6 text-center text-3xl font-extrabold text-white">`

          `Create your account`

        `</h2>`

      `</div>`

      `<form class="mt-8 space-y-6" method="POST">`

        `{% csrf_token %}`

        `<input type="hidden" name="remember" value="true">`

        `<div class="rounded-md shadow-sm -space-y-px">`

          `{% for field in form %}`

            `<div class="{% if not forloop.first %}mt-4{% endif %}">`

              `<label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-white">`

                `{{ field.label }}`

              `</label>`

              `<div class="relative">`

                `{{ field }}`

                `<div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">`

                  `{% if field.errors %}`

                    `<svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">`

                      `<path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />`

                    `</svg>`

                  `{% endif %}`

                `</div>`

              `</div>`

              `{% if field.errors %}`

                `{% for error in field.errors %}`

                  `<p class="mt-1 text-sm text-red-600">{{ error }}</p>`

                `{% endfor %}`

              `{% endif %}`

            `</div>`

          `{% endfor %}`

        `</div>`


        `<div>`

          `<button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-blue-900 hover:bg-blue-950 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-900">`

            `Register`

          `</button>`

        `</div>`

      `</form>`


      `{% if messages %}`

      `<div class="mt-4">`

        `{% for message in messages %}`

        `<div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">`

          `<span class="block sm:inline">{{ message }}</span>`

        `</div>`

        `{% endfor %}`

      `</div>`

      `{% endif %}`


      `<div class="text-center mt-4">`

        `<p class="text-sm text-white">`

          `Already have an account?`

          `<a href="{% url 'main:login' %}" class="font-medium text-blue-900 hover:text-blue-950">`

            `Login here`

          `</a>`

        `</p>`

      `</div>`

    `</div>`

  `</div>`

  `{% endblock content %}`

  \`\`\`

  * ***Styling*** **halaman Create Product Entry**

  Modifikasi `create_product_entry.html` pada subdirektori `main/templates/` menjadi seperti berikut:

  \`\`\`python

  `{% extends 'base.html' %}`

  `{% load static %}`

  `{% block meta %}`

  `<title>Create Product</title>`

  `{% endblock meta %}`


  `{% block content %}`

  `{% include 'navbar.html' %}`


  `<div class="flex flex-col min-h-screen bg-gray-100">`

    `<div class="container mx-auto px-4 py-8 mt-16 max-w-xl">`

      `<h1 class="text-3xl font-bold text-center mb-8 text-black">Create Product Entry</h1>`

    

      `<div class="bg-white shadow-md rounded-lg p-6 form-style">`

        `<form method="POST" class="space-y-6">`

          `{% csrf_token %}`

          `{% for field in form %}`

            `<div class="flex flex-col">`

              `<label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">`

                `{{ field.label }}`

              `</label>`

              `<div class="w-full text-black">`

                `{{ field }}`

              `</div>`

              `{% if field.help_text %}`

                `<p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>`

              `{% endif %}`

              `{% for error in field.errors %}`

                `<p class="mt-1 text-sm text-red-600">{{ error }}</p>`

              `{% endfor %}`

            `</div>`

          `{% endfor %}`

          `<div class="flex justify-center mt-6">`

            `<button type="submit" class="bg-indigo-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-indigo-700 transition duration-300 ease-in-out w-full">`

              `Create Product Entry`

            `</button>`

          `</div>`

        `</form>`

      `</div>`

    `</div>`

  `</div>`


  `{% endblock %}`

  \`\`\`

  * *Styling* halaman Home

  Saya membuat berkas `card_info.html` di directory `main/templates`, lalu mengisi berkas tersebut dengan kode html seperti berikut:

  \`\`\`python

  `<div class="bg-teal-700 rounded-xl overflow-hidden border-2 border-teal-700">`

      `<div class="p-4">`

        `<h5 class="text-lg font-semibold text-white">{{ title }}</h5>`

        `<p class="text-white">{{ value }}</p>`

      `</div>`

  `</div>`

  \`\`\`

  Kemudian, saya membuat berkas `card_product.html` di directory `main/templates`, lalu mengisi berkas tersebut dengan kode html seperti berikut:

  \`\`\`python

  `<div class="relative break-inside-avoid">`

      `<div class="relative top-5 bg-white hover:bg-gray-200 shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border border-gray-200">`

        `<div class="p-4">`

          `<h2 class="text-lg font-bold mt-1 text-gray-800 mb-2">{{product_entry.name}}</h2>`

          `<p class="font-semibold text-black mb-2">Description</p>` 

          `<p class="text-gray-700 mb-2">`

            `<span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#CDC1FF_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">{{product_entry.description}}</span>`

          `</p>`

          `<div class="mt-4">`

            `<p class="text-lg font-bold text-indigo-600 mt-2">IDR {{product_entry.price}}</p>`

          `</div>`

        `</div>`

      `</div>`

      `<div class="absolute flex space-x-1 -bottom-9 right-0 transform translate-x-2">`

        `<a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">`

          `<svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">`

            `<path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />`

          `</svg>`

        `</a>`

        `<a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">`

          `<svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">`

            `<path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />`

          `</svg>`

        `</a>`

      `</div>`

    `</div>`

  \`\`\`

  Selanjutnya, saya memilih satu foto atau *icon* sedih dari internet dan dinamakan `sedih-banget.png`. Setelah itu, saya menambahkan foto `sedih-banget.png` tadi ke direktori `static/image` yang berada di `root project`. Setelah semua berkas selesai dibuat, saya menggunakan `card_info.html, card_product.html, dan sedih-banget.png` tersebut ke template `main.html`. Pada *directory* `main/templates`, modifikasi main.html seperti ini:

  \`\`\`python

  `{% extends 'base.html' %}`

  `{% load static %}`


  `{% block meta %}`

  `<title>Shopeeta</title>`

  `{% endblock meta %}`

  `{% block content %}`

  `{% include 'navbar.html' %}`

  `<div class="overflow-x-hidden px-4 md:px-8 pb-8 pt-24 min-h-screen bg-gray-100 flex flex-col">`

    `<div class="p-2 mb-6 relative">`

      `<div class="relative grid grid-cols-1 z-30 md:grid-cols-3 gap-8">`

        `{% include "card_info.html" with title='NPM' value=npm %}`

        `{% include "card_info.html" with title='Name' value=name %}`

        `{% include "card_info.html" with title='Class' value=class %}`

      `</div>`

      `<div class="w-full px-6  absolute top-[44px] left-0 z-20 hidden md:flex">`

        `<div class="w-full min-h-4 bg-indigo-700">`

        `</div>`

      `</div>`

      `<div class="h-full w-full py-6  absolute top-0 left-0 z-20 md:hidden flex ">`

        `<div class="h-full min-w-4 bg-indigo-700 mx-auto">`

        `</div>`

      `</div>`

  `</div>`

      `<div class="px-3 mb-4">`

        `<h1 class="font-bold text-blue-900 text-center">Last Login: {{last_login}}</h1>`

      `</div>`

      `<div class="flex justify-end mb-6">`

          `<a href="{% url 'main:create_product_entry' %}" class="bg-blue-900 hover:bg-blue-950 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">`

              `Add New Product Entry`

          `</a>`

      `</div>`

      

      `{% if not product_entries %}`

      `<div class="flex flex-col items-center justify-center min-h-[24rem] p-6">`

          `<img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>`

          `<p class="text-center text-gray-600 mt-4">Belum ada produk yang terdaftar.</p>`

      `</div>`

      `{% else %}`

      `<div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">`

          `{% for product_entry in product_entries %}`

              `{% include 'card_product.html' with product_entry=product_entry %}`

          `{% endfor %}`

      `</div>`

      `{% endif %}`

  `</div>`

  `{% endblock content %}`

  \`\`\`

  * *Styling* halaman Edit Product

  Membuat berkas `edit_product.html` pada subdirektori `main/templates` dengan potongan kode seperti berikut:

  \`\`\`python

  `{% extends 'base.html' %}`

  `{% load static %}`

  `{% block meta %}`

  `<title>Edit Product</title>`

  `{% endblock meta %}`


  `{% block content %}`

  `{% include 'navbar.html' %}`

  `<div class="flex flex-col min-h-screen bg-gray-100">`

    `<div class="container mx-auto px-4 py-8 mt-16 max-w-xl">`

      `<h1 class="text-3xl font-bold text-center mb-8 text-black">Edit Product Entry</h1>`

    

      `<div class="bg-gray rounded-lg p-6 form-style">`

        `<form method="POST" class="space-y-6">`

            `{% csrf_token %}`

            `{% for field in form %}`

                `<div class="flex flex-col">`

                    `<label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">`

                        `{{ field.label }}`

                    `</label>`

                    `<div class="w-full text-black">`

                        `{{ field }}`

                    `</div>`

                    `{% if field.help_text %}`

                        `<p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>`

                    `{% endif %}`

                    `{% for error in field.errors %}`

                        `<p class="mt-1 text-sm text-red-600">{{ error }}</p>`

                    `{% endfor %}`

                `</div>`

            `{% endfor %}`

            `<div class="flex justify-center mt-6">`

                `<button type="submit" class="bg-indigo-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-indigo-700 transition duration-300 ease-in-out w-full">`

                    `Edit Product Entry`

                `</button>`

            `</div>`

        `</form>`

    `</div>`

    `</div>`

  `</div>`

  `{% endblock %}`

  \`\`\`

  * **Membuat *navigation bar* (*navbar*) untuk fitur-fitur pada aplikasi yang *responsive* terhadap perbedaan ukuran *device*, khususnya *mobile* dan *desktop*.**

  Saya membuat berkas HTML baru dengan nama `navbar.html` pada folder `templates/` di `root directory`. Isi dari `navbar.html` adalah sebagai berikut:

  \`\`\`python

  `<!DOCTYPE html>`

  `<html lang="en">`

  `<head>`

      `<meta charset="UTF-8">`

      `<meta name="viewport" content="width=device-width, initial-scale=1.0">`

      `<title>Responsive Navbar</title>`

      `<script src="https://cdn.tailwindcss.com"></script>`

  `</head>`

  `<body class="bg-teal-700 text-white">`


      `<!-- Navbar -->`

      `<nav class="bg-teal-700 p-4">`

          `<div class="container mx-auto flex justify-between items-center">`

              `<!-- Logo -->`

              `<div class="text-2xl font-bold">`

                  `Shopeeta`

              `</div>`


              `<!-- Mobile hamburger menu button -->`

              `<div class="block lg:hidden">`

                  `<button id="hamburger" class="text-gray-400 focus:outline-none">`

                      `<svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">`

                          `<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7"></path>`

                      `</svg>`

                  `</button>`

              `</div>`


              `<!-- Links (hidden on mobile) -->`

              `<div class="hidden lg:flex justify-between items-center space-x-6">`

                `<a href="#" class="hover:text-gray-400">Home</a>`

                `<a href="#" class="hover:text-gray-400">Products</a>`

                `<a href="#" class="hover:text-gray-400">Categories</a>`

                `<a href="#" class="hover:text-gray-400">Cart</a>`

              `</div>`


              `<!-- Authentication Links -->`

              `<div class="hidden lg:flex items-center">`

                `{% if user.is_authenticated %}`

                  `<span class="text-gray-300 mr-4">Welcome, {{ user.username }}</span>`

                  `<a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">`

                    `Logout`

                  `</a>`

                `{% else %}`

                  `<a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">`

                    `Login`

                  `</a>`

                  `<a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">`

                    `Register`

                  `</a>`

                `{% endif %}`

              `</div>`

          `</div>`


          `<!-- Mobile Menu -->`

          `<div id="mobileMenu" class="hidden lg:hidden">`

              `<a href="#" class="block py-2 px-4 hover:bg-gray-700">Home</a>`

              `<a href="#" class="block py-2 px-4 hover:bg-gray-700">Products</a>`

              `<a href="#" class="block py-2 px-4 hover:bg-gray-700">Categories</a>`

              `<a href="#" class="block py-2 px-4 hover:bg-gray-700">Cart</a>`

              `{% if user.is_authenticated %}`

                `<span class="block py-2 px-4">Welcome, {{ user.username }}</span>`

                `<a href="{% url 'main:logout' %}" class="block bg-red-500 py-2 px-4 text-center hover:bg-red-600">Logout</a>`

              `{% else %}`

                `<a href="{% url 'main:login' %}" class="block bg-blue-500 py-2 px-4 text-center hover:bg-blue-600">Login</a>`

                `<a href="{% url 'main:register' %}" class="block bg-green-500 py-2 px-4 text-center hover:bg-green-600">Register</a>`

              `{% endif %}`

          `</div>`

      `</nav>`


      `<script>`

          `const hamburger = document.getElementById('hamburger');`

          `const mobileMenu = document.getElementById('mobileMenu');`


          `hamburger.addEventListener('click', () => {`

              `mobileMenu.classList.toggle('hidden');`

          `});`

      `</script>`


  `</body>`

  `</html>`

  \`\`\`


# **Tugas Individu 6**

1. **Jelaskan manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web\!**

Penggunaan JavaScript dalam pengembangan aplikasi web memiliki banyak manfaat, di antaranya:

* Interaktivitas yang Lebih Baik    
  JavaScript memungkinkan pengembang untuk membuat aplikasi web yang lebih interaktif dan dinamis. Misalnya, JavaScript bisa digunakan untuk menangani event seperti klik, scroll, atau input pengguna, memberikan pengalaman yang lebih responsif tanpa perlu memuat ulang halaman.  
* Pengembangan Aplikasi Web yang Cepat dan Responsif  
  Dengan JavaScript, aplikasi web bisa melakukan banyak tugas di sisi klien *(client-side)*, seperti validasi form, manipulasi DOM, dan perubahan tampilan halaman secara langsung, sehingga mengurangi beban di server dan mempercepat waktu respons aplikasi.  
* Penggunaan AJAX (*Asynchronous JavaScript and XML*)   
  JavaScript mendukung teknik AJAX, yang memungkinkan aplikasi web berkomunikasi dengan server secara asynchronous. Hal ini memungkinkan pengiriman dan penerimaan data dari server tanpa perlu memuat ulang seluruh halaman, memberikan pengalaman pengguna yang lebih mulus.  
* Kompatibilitas dengan Browser  
  JavaScript didukung oleh hampir semua browser modern tanpa perlu instalasi tambahan, sehingga mudah digunakan dalam aplikasi web yang ditujukan untuk berbagai platform dan perangkat.  
* Pengembangan Sisi Klien (*Client-Side Development*)  
  JavaScript berperan penting dalam pengembangan sisi klien untuk membangun antarmuka pengguna yang kaya dan responsif, mengelola elemen UI, dan memproses input dari pengguna secara langsung sebelum data dikirim ke server.  
* Dukungan Framework dan Library    
  Terdapat banyak framework dan library berbasis JavaScript seperti React, Angular, dan Vue.js yang mempercepat proses pengembangan aplikasi web dengan menyediakan komponen yang siap digunakan dan alur kerja yang lebih terstruktur.  
* Eksekusi di Sisi Klien dan Server (Full-Stack Development)    
  Dengan teknologi seperti Node.js, JavaScript tidak hanya terbatas pada sisi klien tetapi juga bisa digunakan untuk pengembangan server-side, memungkinkan pengembang untuk bekerja secara full-stack menggunakan satu bahasa pemrograman.  
* Pengembangan Game dan Aplikasi Berbasis Web\*\*    
  JavaScript juga digunakan dalam pengembangan game berbasis web dan aplikasi yang memerlukan animasi dan rendering dinamis dengan bantuan library seperti Three.js untuk 3D rendering atau p5.js untuk visualisasi.

2. **Jelaskan fungsi dari penggunaan `await` ketika kita menggunakan `fetch()`\! Apa yang akan terjadi jika kita tidak menggunakan `await`?**

Fungsi `await` digunakan untuk menunggu hasil dari fungsi `async`. Fungsi dari penggunaan await ketika menggunakan `fetch()` adalah untuk menunggu hasil dari operasi asynchronous (seperti permintaan HTTP) sebelum melanjutkan eksekusi kode. `fetch()` adalah fungsi asynchronous yang digunakan untuk membuat permintaan HTTP (seperti GET atau POST) ke server. Ketika menggunakan `await` sebelum `fetch()`, kode akan "pause" hingga operasi `fetch()` selesai (entah berhasil atau gagal) dan mengembalikan sebuah `Promise` yang berisi respons dari server. Setelah permintaan selesai, hasilnya (response) akan disimpan dalam variabel yang mengikuti `await`. Jika tidak menggunakan `await` dengan `fetch()`, maka `fetch()` akan mengembalikan `Promise` yang belum diselesaikan (pending). Ini berarti alur eksekusi kode tidak akan menunggu sampai permintaan selesai dan akan melanjutkan eksekusi kode berikutnya, yang dapat menyebabkan hasil yang tidak diinginkan atau error.

3. **Mengapa kita perlu menggunakan *decorator* `csrf_exempt` pada *view* yang akan digunakan untuk AJAX `POST`?**

*Decorator* `@csrf_exempt` digunakan untuk menonaktifkan validasi CSRF pada view Django. Ini sering diterapkan pada view yang menangani AJAX POST ketika CSRF token tidak dikirimkan dalam request. Kita perlu menggunakan decorator ini untuk menghindari Error 403 (Forbidden). Jika request POST AJAX tidak menyertakan CSRF token, Django akan memblokir permintaan dengan error "CSRF Token Missing or Incorrect". Dengan `@csrf_exempt`, pengecekan ini diabaikan. Selain itu, *decorator* ini juga memungkinkan AJAX POST Berjalan: Pada beberapa kasus, seperti API internal atau data tidak sensitif, CSRF protection tidak diperlukan sehingga `@csrf_exempt` mempermudah penerimaan POST request tanpa CSRF token.

4. **Pada tutorial PBP minggu ini, pembersihan data *input* pengguna dilakukan di belakang (*backend*) juga. Mengapa hal tersebut tidak dilakukan di *frontend* saja?**

Pembersihan data di *backend* penting meskipun sudah dilakukan di *frontend* karena:

* **Keamanan**: Frontend bisa dimanipulasi oleh pengguna atau dilewati. *Backend* memastikan validasi tetap dijalankan untuk mencegah data berbahaya masuk.  
* **Integritas Data**: Backend bertanggung jawab menjaga data yang masuk tetap valid dan aman, karena tidak semua klien mematuhi validasi di frontend.  
* **Serangan Berbahaya**: *Backend* melindungi dari ancaman seperti **SQL Injection** dan **XSS**, yang bisa terjadi jika input tidak dibersihkan dengan baik.  
* **Kontrol Penuh**: Backend memberi kendali penuh atas pembersihan dan validasi data, memungkinkan penerapan logika validasi yang lebih kompleks dan konsisten.

Oleh karena itu, meskipun pembersihan di *frontend* membantu memperbaiki pengalaman pengguna, pembersihan di *backend* wajib dilakukan untuk menjaga keamanan, integritas, dan memastikan bahwa aplikasi terlindung dari manipulasi pengguna dan serangan berbahaya.

5. **Jelaskan bagaimana cara kamu mengimplementasikan *checklist* di atas secara *step-by-step* (bukan hanya sekadar mengikuti tutorial)\!**  
* **AJAX `GET`**  
  Langkah pertama yang saya lakukan adalah menghapus 2 baris pada berkas views.py. Kedua baris itu adalah:  
  `product_entries = ProductEntry.objects.filter(user=request.user)`  
  `'product_entries': product_entries,`  
    
  Kemudian, saya memodifikasi baris pertama *views* untuk `show_json` dan `show_xml` seperti berikut:  
  `data = ProductEntry.objects.filter(user=request.user)`  
    
  Setelah itu, saya mengganti bagian *block conditional* `product_entries` untuk menampilkan card\_product ketika kosong atau tidak pada berkas main.html dengan potongan kode berikut:  
  ```python  
  ...  
  <div id="product_entry_cards"></div>  
  ...  
  ```  
  Selanjutnya, saya membuat *block* `<script>` di bagian bawah berkas `main.html` (sebelum `{% endblock content %}`) disertai fungsi baru dengan nama `getProductEntries` dan `refreshProductEntries` yang digunakan untuk me-*refresh* data *products* secara asinkronus. Berikut potongan kode yang saya tambahkan pada berkas `main.html`.  
  ```python  
  <script>  
    async function getProductEntries(){  
        return fetch("{% url 'main:show\_json' %}").then((res) => res.json())  
    }  
    
    async function refreshProductEntries() {  
      document.getElementById("product_entry_cards").innerHTML = "";  
      document.getElementById("product_entry_cards").className = "";  
      const productEntries = await getProductEntries();  
      let htmlString = "";  
      let classNameString = "";  
    
      if (productEntries.length === 0) {  
          classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";  
          htmlString = `  
              <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">  
                  <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>  
                  <p class="text-center text-gray-600 mt-4">Belum ada data product pada mental health tracker.</p>  
              </div>  
          `;  
      }  
      else {  
          classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full"  
          productEntries.forEach((item) => {  
              const name = DOMPurify.sanitize(item.fields.name);  
              const description = DOMPurify.sanitize(item.fields.description);  
              const price = DOMPurify.sanitize(item.fields.price);  
              htmlString += `  
              <div class="relative break-inside-avoid">  
                <div class="relative top-5 bg-white hover:bg-gray-200 shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border border-gray-200">  
                  <div class="p-4">  
                    <h2 class="text-lg font-bold mt-1 text-gray-800 mb-2">${name}</h2>  
                    <p class="font-semibold text-black mb-2">Description</p>   
                    <p class="text-gray-700 mb-2">  
                      <span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#CDC1FF_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">${description}</span>  
                    </p>  
                    <div class="mt-4">  
                      <p class="text-lg font-bold text-indigo-600 mt-2">IDR ${price}</p>  
                    </div>  
                  </div>  
                </div>  
                <div class="absolute flex space-x-1 -bottom-9 right-0 transform translate-x-2">  
                  <a href="/edit-product/${item.pk}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">  
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">  
                        <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />  
                    </svg>  
                  </a>  
                  <a href="/delete/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">  
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">  
                        <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />  
                    </svg>  
                  </a>  
                </div>  
              </div>  
              `;  
          });  
      }  
      document.getElementById("product_entry_cards").className = classNameString;  
      document.getElementById("product_entry_cards").innerHTML = htmlString;  
    }  
    refreshProductEntries();  
  . . .  
  </script>  
  ```  
* **AJAX `POST`**  
  Pada berkas views.py, saya menambahkan impor `csrf_exempt` dan `require_POST.` Kemudian, saya membuat fungsi baru bernama `add_product_entry_ajax` yang menerima parameter `request` seperti berikut.  
  ```python  
  ...  
  @csrf_exempt  
  @require_POST  
  def add_product_entry_ajax(request):  
      name = strip_tags(request.POST.get("name")) # strip HTML tags!  
      description = strip_tags(request.POST.get("description")) # strip HTML tags!  
      price = request.POST.get("price")  
      user = request.user  
    
      new_product = ProductEntry(  
          name=name, price=price,   
          description=description, user=user  
      )  
      new_product.save()  
    
      return HttpResponse(b"CREATED", status=201)  
  ```  
  Setelah membuat fungsi, saya melakukan routing fungsi tersebut ke berkas urls.py. Caranya adalah dengan mengimpor fungsi tersebut terlebih dahulu pada berkas urls.py, lalu mendaftarkan *path url* ke dalam `urlpatterns` untuk mengakses fungsi yang sudah diimpor tadi.  
  ```python  
  from main.views import add_product_entry_ajax  
    
  urlpatterns = [  
      ...  
      path('create-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),  
  \]  
  ```  
  Untuk mengimplementasikan modal (*Tailwind*) pada aplikasi kamu, saya meletakkan potongan kode berikut dibawah `div` dengan `id` `product_entry_cards` pada berkas `main.html.`  
  ```python  
  ...  
  <div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">  
        <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">  
          <!-- Modal header -->  
          <div class="flex items-center justify-between p-4 border-b rounded-t">  
            <h3 class="text-xl font-semibold text-gray-900">  
              Add New Product Entry  
            </h3>  
            <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">  
              <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">  
                <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>  
              </svg>  
              <span class="sr-only">Close modal</span>  
            </button>  
          </div>  
          <!-- Modal body -->  
          <div class="px-6 py-4 space-y-6 form-style">  
            <form id="productEntryForm">  
              <div class="mb-4">  
                <label for="name" class="block text-sm font-medium text-gray-700">Product</label>  
                <input type="text" id="name" name="name" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700 text-black" placeholder="Enter your product" required>  
              </div>  
              <div class="mb-4">  
                <label for="price" class="block text-sm font-medium text-gray-700">Price</label>  
                <input type="number" id="price" name="price" min="1" max="10" class="mt-1 block w-full border border-gray-300 rounded-md p-2 hover:border-indigo-700 text-black" placeholder="Enter your price" required>  
              </div>  
              <div class="mb-4">  
                <label for="description" class="block text-sm font-medium text-gray-700">Description</label>  
                <textarea id="description" name="description" rows="3" class="mt-1 block w-full h-52 resize-none border border-gray-300 rounded-md p-2 hover:border-indigo-700 text-black" placeholder="Describe your product" required></textarea>  
              </div>  
            </form>  
          </div>  
          <!-- Modal footer -->  
          <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end">  
            <button type="button" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>  
            <button type="submit" id="submitProductEntry" form="productEntryForm" class="bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg">Save</button>  
          </div>  
        </div>  
      </div>  
  ...  
  ```  
  Kemudian, agar modal dapat berfungsi, kita perlu menambahkan fungsi-fungsi JavaScript berikut.  
  ```python  
  ...  
  const modal = document.getElementById('crudModal');  
    const modalContent = document.getElementById('crudModalContent');  
    
    function showModal() {  
        const modal = document.getElementById('crudModal');  
        const modalContent = document.getElementById('crudModalContent');  
    
        modal.classList.remove('hidden');   
        setTimeout(() => {  
          modalContent.classList.remove('opacity-0', 'scale-95');  
          modalContent.classList.add('opacity-100', 'scale-100');  
        }, 50);   
    }  
    
    function hideModal() {  
        const modal = document.getElementById('crudModal');  
        const modalContent = document.getElementById('crudModalContent');  
    
        modalContent.classList.remove('opacity-100', 'scale-100');  
        modalContent.classList.add('opacity-0', 'scale-95');  
    
        setTimeout(() => {  
          modal.classList.add('hidden');  
        }, 150);   
    }  
    
    document.getElementById("cancelButton").addEventListener("click", hideModal);  
    document.getElementById("closeModalBtn").addEventListener("click", hideModal);  
  ...  
  ```  
  Setelah itu, saya memodifikasi bagian tombol *Add New Product Entry* yang sudah ditambahkan di tutorial sebelumnya dan menambahkan tombol baru untuk melakukan penambahan data dengan AJAX.  
  ```python  
  ...  
  <a href="{% url 'main:create_product_entry' %}" class="bg-indigo-400 hover:bg-indigo-400 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105 mx-4 ">  
          Add New Product Entry  
        </a>  
        <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-indigo-700 hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">  
          Add New Product Entry by AJAX  
        </button>  
  ...  
  ```  
  Selanjutnya, saya membuat fungsi baru pada *block* `<script>` dengan nama `addProductEntry`.  
  ```python  
  <script>  
    function addProductEntry() {  
      fetch("{% url 'main:add_product_entry_ajax' %}", {  
        method: "POST",  
        body: new FormData(document.querySelector('#productEntryForm')),  
      })  
      .then(response => refreshProductEntries())  
    
      document.getElementById("productEntryForm").reset();   
      document.querySelector("[data-modal-toggle='crudModal']").click();  
    
      return false;  
    }  
  ...  
  </script>  
  ```  
  Untuk menutup celah keamanan *Cross Site Scripting* atau XSS saya mengimpor fungsi berikut pada berkas views.py dan forms.py.  
  `from django.utils.html import strip_tags`  
    
  Pada fungsi `add_product_entry_ajax` di `views.py`, gunakanlah fungsi `strip_tags` pada data `product` dan `description` sebelum data tersebut dimasukkan ke dalam `ProductEntry`.  
  ```python  
  ...  
  @csrf_exempt  
  @require_POST  
  def add_product_entry_ajax(request):  
      name = strip_tags(request.POST.get("name"))  
      description = strip_tags(request.POST.get("description"))  
      ...  
  ```  
  Kemudian, pada berkas forms.py saya menambahkan 2 method pada class ProductEntryForm seperti berikut.  
  ```python  
  ...  
  class ProductEntryForm(ModelForm):  
      class Meta:  
          ...  
        
      def clean_name(self):  
          name = self.cleaned_data["name"]  
          return strip_tags(name)  
    
      def clean_description(self):  
          description = self.cleaned_data["description"]  
          return strip_tags(description)  
  ...  
  ```  
  Jika ingin menggunakan *library* JavaScript DOMPurify untuk melakukan pembersihan di frontend, maka saya menambahkan potongan kode berikut pada block meta di berkas main.html.  
  ```python  
  {% block meta %}  
  ...  
  <script src="https://cdn.jsdelivr.net/npm/dompurify@3.1.7/dist/purify.min.js"></script>  
  {% endblock meta %}  
  ```  
  Selanjutnya, pada fungsi `refreshProductEntries`, saya menambahkan potongan kode berikut.  
  ```python  
  <script>  
      ...  
      async function refreshProductEntries() {  
          ...  
          const name = DOMPurify.sanitize(item.fields.name);

            	        const description = DOMPurify.sanitize(item.fields.description);  
            	        const price = DOMPurify.sanitize(item.fields.price);

            ...  
        });  
        ...  
    }  
    ...  
</script>  
```  
Saya juga tidak lupa untuk mengubah semua kemunculan `item.fields.name` menjadi `name`, `item.fields.description` menjadi `description,` dan `item.fields.price` menjadi `price`.  


[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAbQAAAEtCAYAAABgXZXNAABOrUlEQVR4Xu2dB5gURde28RURSSb0w5xzAowYACMGDBgBs4BgThjAgKhkUDGCoiQFBQNJxYCYRUFFESOCKCCYBRVz/e993r/GpndZdmFC9fRzX1dfu9PT09PT3VXPOadOna7khBBCiCKgUnyFEEIIkUQkaEIIIYoCCZoQQoiiQIImhBCiKJCgCSGEKAokaEIIIYoCCZoQQoiiQIImhBCiKJCgCZElbrrpJle5cmVXtWpVt+aaa2op0LLGGmu4rbfe2r377rvxSySKHAmaEFni+uuvd7Vq1XIdO3Z0TzzxhBs3bpyWPC9PPfWUe/zxx91GG23kpk6dGr9EosiRoAmRJRC09dZbz8RMFI5//vnHBE0eWvqQoAmRJRC0//u//zMPQRSOX375RYKWUiRoQmQJL2iPPfZY/K2CsHjxYrdw4cIl1v3xxx+2Di/mt99+cz/99JP78ccfbfn111+X2La0z0dZtGiR++6779zPP/8cf6ugSNDSiwRNiCwRkqD99ddf7oEHHnDnn3/+EuvfeOMNd95555mYPfzww+6UU05xRx99tC2XXnqpe/XVV03c/vzzTzdo0CB38cUXL/F5z+jRo90ZZ5zhmjRp4s4++2z35JNPxjcpGBK09CJBK1LokN566y334osvLrH+448/dpMmTXLvv/++GzNmjA2kjx8/3jok/qfD++ijj9zYsWNtLIhBdv6y7TPPPOO+/fZb99xzz2UG4F9++eUl9p9mQhI0PLHWrVu7GjVqLLF+yJAhrnr16iZaZ555plt77bXdrFmz3OzZs93w4cPdVltt5XbeeWcTvNNPP92tu+66S3we3nnnHcsi5PpzP9x3331up512cp9++ml804IgQUsvErQixXdY++yzzxLrycA76KCD3DXXXOPWWmst64A32GADt/7667s6deq4448/3jrm2rVr2zreI9GBdOjtttvOvfDCC9Z5sY5Og87v3nvvdfPmzVvie9JISIL2+++/uzZt2rjVV199ifVDhw51NWvWtPvjrLPOsuvrQcTwyBA5wom8zz0R56WXXnK77bbbElmEGEJ8JgQkaOlFglak/PDDD+6YY45x22yzzRLrsdpp7FHotLp162b/M7bCAjNmzHD169e3js6/N2rUKBM7vw2e4BZbbOEOPvhg98EHH/xvhyklJEHDQytN0B588EGbWsDYGaFC5s0ROsT4OfDAA93GG2/sLrnkEvs8HlppggaIHffRhhtu6A4//HAzkEJBgpZeJGhFCoLWrFkzt+mmm7rvv//ePKhvvvnGnXjiiWUKWpTPPvvMBI3OzeMFLcq+++5rwpn28GNIgoaHhvGCNxZl4MCBFoZE0Nq1a+cqVark9tprL7fHHnvYhPAuXbq4OXPmWEJIWYK2YMEC89bx+DBo2CfhxxCQoKUXCVqRgqCdcMIJbpVVVnEnnXSShRIRMzqoaJgJWEdHFocxkXr16i2R/UYyACGpDz/80H3yySc2nkI4smXLltYRppmQBI2kkGuvvda8Me9N8/eKK65wq666qmUvtmrVyowTrjPjplzXCy+80ASBa740QUO42L9nwoQJZtTwNwQkaOlFglakeA+Nho2nRTiQjuuII46wMFGUiggaySF0fFdddZUtl112mXv99dcjn0ovoc1D++qrr8yYIfTctWtXd8ghh5gX1rRpU/O6MUIYR/Vw3Agc42M+KWTllVd2PXr0cN27d3d9+vSxRKNnn33Wbb/99u7qq692999/v4U2GVMNRUAkaOlFglakLG0MDauccZIoFRE0H3L0FnrUUk87IXloQNjxlVdeMfFZZ511zBDBSyfzFcE655xz3LbbbpvZnvlk1113nXnwJI20b9/eQpb8Jhbum759+1ryR926dS0DkvuL+4dxtPg8tkIhQUsvErQihXEz5hZtueWWS6wnASDuodExUVg3DiFFOq5oR4UVH7Xqxb+EJmie1157zT3yyCM2NYP0fMAQefvtt20qRhTuG6ZpIHhM7SDEzO9hwZiZPn26bTdlyhR7PXLkSNueBKJQkKClFwlakYK1TaIHVniU2267zby0KISW6JjikEjCZFssfQ/p2aeeempkK+EJLeSYViRo6UWCVqSQAEDDjs8NInstvo7XUdHy/P333yaMPqkASNMvqxxSMYK3MnHiRAvflfXbQ/XQ0oYELb1I0IRYBoThmHdFijsL40qkxN9+++3WafpxxBtuuEGCFgAStPQiQRNiGeDVnnvuuRlB8wtjibvuuqvr16+fVc2gCkshQ46Mdc6cOdPmiJUH5qJ9/vnnS3jg2YDj4Bjw8AuBBC29SNBEYqHTJIWcZIdcLiNGjHCHHnpoCUHzC1mflAPbe++9LeOPRIpC8NBDD1kiEFMrlgUihifJ/ERfCSZbcF3atm1rSUWFQIKWXiRoRQDFZZnoTOFhPyk2DZCF16lTJ3fllVfmdLnoooss2zMuZH5ZaaWVXLVq1dwmm2xiHlp5BCXbEBYle5UK+ogVc9B8hRdS8HnNOOn8+fPNM/viiy9sqgb1Ov3jX1jHdA880jisY2EMlXmN3vui+owff2Udj5NhHUJJ7c9CIEFLLxK0IqB58+auUaNG5kWQls9rUrILOUeMjq8i4a+QiZaJii5MOsY7wxuh4vwFF1xgHlohQo6k35Ot6sN9PDbG19YcNmyYVQDB6GEiPHUbOVbCqJtttpmJGJ4uE635nbwff8YZBYnvuOMOm1x91FFHuTvvvNOyYCl9xZMZgEoxZMWy+CLWhbj+ErT0IkErAhjLYdLrscceaxNcd9hhB5tU/d577y2xHSKTDcoz5oLXSAUJEieSDpmNFPKNihnnGAGgNiJeD9x4440FSwphwvM999xj/zNXjAnT/tFBlMDacccd7VlneE14lJTAorI+gsZ2hx12mE2qRrCYTB8VA643oog3x33FucAbxRvk9yNgbEMWKL+fCjVkzrJPSmrlGwlaepGgFQFUdqC0UZQ11ljDShYBc9F22WUX8+KoGkHHhwXO+xSWpeYjISIeBUOnRDUJ30kzYZYODEsbj48kCB5JQ0eItU84q0OHDjaBmw6MDhPr/8gjj3T/+c9/bNI2IagkQ+eMd4JokPxBeK80CjUP7csvv7S5gXhRgKBxvX2xaISW68YEa64xD/WE3r17W8kqJlt37tzZClGzLROl4yBeXN+5c+faa8bq9txzTxMNfjMeG9ecddwzjMtRGq1///55Tw6RoKUXCVoRgOWMiBDiY3yDB3DSyTz66KP2Pt4baeZMisb6RtgICfE/iQx0VlRbx/OgwCyPEfEdF2Eq6gESXuLBoDwmhvAUVjgPgyQBgoc9UgKJyhF4AzwRGdGkU2nRokW5PLqQ8fPxltUxF2oeGgKG2OCB+deM+WGcgB8DROAaNGhgJa3ACxpjYFxfPHwME8KojLlFIeHk5JNPzhg6GEBcc76L689k/d13392MJ8KeCBq1HqkBGX1aQz6QoKUXCVoRQKdECIixDTwuhMl3SIQdqYaPSBEuwgpnnIfxEx4tg1WP4CBACCMTiOkcfcdFoglzsOi4GJujQ2Q/++23n9UGxLtDOLH8OQYEjMxAxnQIc+G9pYVCCZoXD/+9eNJ46L169TIjhydUY3wQWkR0eN4ZIDZ40Bglp512mnnhpPHzPwKGZ4qHRTIIXif1IO+66y67J7iH8Op4jwLFiCAi5x8hg6gxnotXmG8kaOlFglYEEHIkCYBQDx0RYT9fc48QGYKHVc58KTof6vphteO5+Ud+3HzzzdYJPv/881aV3df8mzZtmiUJkFFImInEA8JLJEGQEIAg0oEinIyn8EDJhg0b2n5JCmBuVloolKABQsP4l4eK+XhQXDO86QMOOMA8dK4tmaHAdeReoS4jySBs07hxYzNOCBPjpfNYGMLKCBrvEdok+Yj98uggYLwUI+fuu+/OfD8GFfsrROq+BC29SNCKADwrqlQA3hYdGwJHKAlhwppGbGDcuHHmhSFum2++uSUC4I3hfeHZ0bmR7EDYEoYPH26dGJX38eoYF/GloEhPx6LHwvcCSMdYpUoVC2nSoSKcaaGQgsYjfHg0kPfMCS+S+HHLLbdYqJikDt7jr3/cDx0+HphP88czw8Pm3gDGCjF08MIIS996660mihSy5rr7ECz3D+OuvOcZNGiQhS8Rw3wjQUsvErQiAGuZDiQ6xsNYFx0sKeeDBw82LwuPiQ6LsS5EiQnDWO+IEJ4XwkgKN1Y12xJCInGE/WCx0/EhUIy3EZbEwqfTY/+8ZiylSZMm1vkRrmKeE2M3kydPjhxt8VKopBDPcccdZ+c7F2E+hJDrHc+UxTMnpInX5kFQiBogpoVAgpZeJGhFAOHAr7/+eol1hBzpbPx8IoSHMKAf4/AwdwixIlSJx+bHzrDw8coIJ5Jo4qtJYK3TYUZLJiGkbEt2XDRNG3FEzOLFkIuVQnpogIeEiOTCgGDcjP3H5zZy/2BM+RA3cN0xcuL3ZL6QoKUXCZowhgwZYqHJeHabKD+FFjQgGYMOPdtgvBDCLk/GatyLyzcStPQiQRMGntubb75Z8M4oyYQgaEKClmYkaEJkCQStkMWJxf8gPC5BSycSNCGyBOnwZIpSpYM5gVTOYPH/87es//O1LO37+Z/0ezJe/evSji/+mbLez+fij79p06ZWqNlPKxDpQYImRJYYMGCAzeFiEjMZn0lbqP+IECDK/AamXcS3ScqCsBViDpwoLBI0IbIE2aJk+5F16v8ubYm+X9q2uX6/tG3JZh05cqQVu2ZCPhmrFfn80pZlHUs23/evo5m5Ij1I0IQQGUgMIrElLc/UE8WFBE0IkUGCJpKMBE0IkUGCJpKMBE0IkYEqIxI0kVQkaEKIDPLQRJKRoAkhMkjQRJKRoAkhMijkKJKMBE0IkQEPjadPS9BEEpGgCZEyeNwPk45Lq5w/b948e0CsilSLJCJBEyJHIBxUrODp3s8//7wtzz77bOaJ0YUC0brjjjvs4a+lEX1QbCH4448/ShVbRDj+PDYhokjQhMgRPD+MgsU8PZzCuRTNPfDAA93ZZ58d3zSvfPjhh/aU81CffYcB4B9MG+X++++3slZCLA0JmhA5Ao+CyvXURYzDE8THjx/vOnfu7C644AJ7Yjh88MEH7uqrr3YXXniha9asmTvppJMynznhhBPcCy+8YP/fddddrmPHjla7kO0RzN69e2c6/GuuucbdcMMN9kibGTNmuC+//NKddtpp7qqrrjLvrGXLlpmnkwMe0eWXX25PvL744ovtqdOzZs2ygsuHHXaYu+yyyzJhyAULFri2bdu6Sy+91D3wwAN2LOzrvPPOs+MBnl7OdwFPrh4xYoQ79NBDXatWrdzjjz9u6+fOnetOP/10d8kll7hu3brZcXbv3t2tu+667pBDDrEno/tj45E8FE3edNNN3Z133unefvtt17dvX3fGGWe4e++9156oLYQETYgc4QVt2rRp8bfc4MGD7ZlddNANGzZ0a6+9tgnGiy++aFXvqdqPSG288caWoEHnT4eOxwcNGjQwUcGb2W677UyMqJR/8skn28Na69Wr56pXr+622GIL98Ybb5j4NG7c2J111llujz32cKeeeqoJk4dQHtmNa6yxhttxxx1NzC666CK3/vrrm+BSfZ/fsXjxYhOd3Xff3TxN9nnKKaeYEG+wwQYm0nDTTTfZfqB///723hVXXGHHvckmm9h+EOIWLVrYb+Ic9OvXLyNo5557rnvvvfcyx/fkk0+6VVZZxR100EHu0UcfdY0aNbJjPfbYY+24+d1CSNCEyBEIGh4Ene9xxx1nAnXEEUe4Ll26uM0339xeI1SAt4HIvfLKK2777be3zyJwrVu3Nq9r0KBBbocddrDwJY9FQQy9p3PrrbeagCCO6623nnlxCCLPZUMU8I6qVKmSOS7G8BBaPCcPgsbDSfHcFi5caN4fgoHgcLz85T0vxH4sy++LMCZC9fTTT9t6PK769evbMSJmBxxwgIkVXhzHyFjiPffc43bddVcTtpdfftk+99Zbb5kYI5BRfvzxRxMuPEbEkH16z3fo0KEm6osWLVriMyJ9SNCEyBGIEt4LYb8HH3zQ3XfffbbQeSMKiJVPjyfk2LNnT3sP74dOG4YPH+66du3qzjnnHHfbbbeZeAwcONA8FUJ0r776qokjQoeXhyghFogZIkIo7uGHH3ZVq1bNHBeiQSgz6qGRCIIgEf5j/IrvwyNCcPDCWAhF4kWtueaamc9NmjRpCUF77rnnbD2h1J122skNGTLErb766vaMMr+fvfbay8KJv/zyi/2PGG255ZZu5syZJlIIWtyrJQSKoCGCnDN+M78f8FIRe8KqIt1I0ITIET7k6J+cHM3cw2vjIZRz5syx16TKM3710ksvWSfvhW727NnmseF90WETMtx///3N08GTIhzI2BghQsa6mEOGl1S3bl0TPQRt3Lhxbp111sl8txehuIdGqJPj4H/CmQgRx4Rw8Gw0xskI/bEvnwmJoLIvvifqNTJWxmsEDU8PgSTj89NPP3XvvvuuCdR3331nv5/j5djxBNkfIsr3RWHMEUHDIMBzRQAZRwO8RsKtUYEW6USCJkSOQNAI1XlBi4Ko4K3guRCa82NlpPbjoUUnNlerVs22A8KLeFtTpkyx13TwdOZkTxLCRETwcFiaNGliwkC4jgQR1pFswTYkY0QFDYHifTxJwFtCLDkuwqR4ZUy65jeRhMH4GEkrCDOhSKYC8D+iQ3h1t912M68J0SUJheMnqYXvxrtCoBg7O/744218j3G9sWPHmmfKeCC/he+LwrEwJki2I8fGvvg9/H4EUwgJmhA5Ak+CJ0CXlh7PXCtCf2QmXnnlldaZA56W90I8PXr0sE4cEChCkD4kSQIIHhpjdYw74RGxPYkYw4YNMy8IOAZCnGzHeN0jjzxiYuPBe+QziK/3JPGeGH9DoK677rrME6ARSMKPHAfjV3hoeJKEG8lsxHt85plnLDQKfM9TTz1l+yHRhIxFwKM688wzTTDZnx8DY9wPsYtnhzKOiNhx7Hwf5wkhI9Pyiy++WGJbkU4kaELkEOailTVRmfcYS/IgJohdFIQkus6LmQdh8OE2woV8J4IYr/bxzTffZFL12Wf8uPzn4iAevBcF8eHzCDCeFx4dcGx4XxD/HewnKqLAMRGGjCd0cE5Km0SN5+qFFfx3CQESNCHEcoNAElKMhi+FKBQSNCHEcoNHiSdVWqkqIfKNBE0IIURRIEETImUwjkV6PeNXuYTxNJJBSNEXIh9I0IRIGWQvMrHa110sDeaKMfl5RZ6LRjZku3btbP6ZEPlAgiZEDqHqBoWCKe5LGrofayIFnWoYY8aMsTR0svzwmJgHRvo7qfc333yzTWomm5AJ16SpM/mYwr+k4ZOiT5o8qfZsgwhRyYNtmXd29913m3iRoUgaPfPHKEnF91E9xHtoVCChziI1EjkOFuaZUaLqxhtvtG0+//xzm17Ab2GidhSyFJlWEBU/ChZT15Hf5z00ynpRootzgcjxPUxr8J/jOHjNmBy/hXMUz8QUoiwkaELkCFLg6dipasFEYx4f4ydZM0mYScFMfmaicYcOHax8FEV6ERMWivRSQQNBuvbaa61Q8DbbbGNZhXhYVPZgYVIyYsXCNnwXxYQRpBNPPNGEg2K/vKYkFuK13377mWiQSk+5LCZVU4KKSvaI4FprrWXFjZmAjafGXDGOzU9ujiaB8Jv8JG4Pk50RTyZfU3sSYad6CZPGqQRCMWH2y2RsfjciRkURzgmZk+3bt7ffIURFkKAJkSPwPPBq8GiYp0UpKSYvw6qrrmqVQphQTZUPKmwwMRphoSoHVfeZRIyo4EmxH6pn4PVQrJh9UUCYahoI4t57721iVLlyZRMdKo4wibpGjRr2ef5HBClczEIVj8mTJ9vkbrw8JjMjIIgN3tO+++5rlfEpRUUlj80228y8NCZr8380XIlgMsEZzxGYm4YgMymbepIcL8eNKLI/BAzB43ip/4hXxgRxniaA+HN8lO1CfIWoCBI0IXIEoTa8Jmox8pgTxIlQIB4X9RAJsQHig0DR8SModOZAlQ9EzD8jjaLDgBAdddRRJgJApYxatWplCgf7B4giLAgdIcE2bdqYeAF1F/GWeKwM30kRYYSHCvaIIQWS8SYPP/xwC21S9Jgakfvss4/tj0r+hCej8F14W3hXhEVHjRplY2jsAw+O70cw8fLYB4KHSCOcCDehVrwyPDTCmhzT7bffvsR3CLEsJGhC5IgJEyaYB0IHTSHdmjVrWuV9xoUQCEpQAV4a4TbEhbqOFB8GxIQq+ggQgobXBrym4/eFjfF0VlttNfP+EEa8MfACiceFoPhivnye0B+eECKCmHEMeGSEJfGi8KYQIyZME35EABl3w0Oj3JX/bg/eKN4l43YIMh5pVNA4Jh5aylMFeIIA+0FQ+V2EVfkMx9OrVy+rPELtR/9IGSHKiwRNiBxBAWEECi+LsSQ8ILw0QngIGqJCqI4QHgKCJ8Z4GGNnVNUn5EYIjvEnivEikB7G0vg8WYSIEA/sREwQTbwsxr7wchAiykMRbsSzA8a68BoRSMa58JgQHPbJI2M4FgSQosiMvZGcQliTY2DsDdGMl98CvDrChhQNBspx4YERniQhhvV4qtSexMtDsPhNrOdzlMpC1Pj9VP0vrQyXEGUhQRMiRxBaJOSIMNHZE0IjeQJhYAwLb43xK8SDTh9PBkE7+uijzQPDc8IroqPnMS7ewwIe40IlfzwwQpdUu6cSP6FMxI3QHu8jGMw747t80gaJICRlMJaF94ZnhXfGPnnsC8WGGffDc8JbJHRKQWGOje+j+HBpEPLcc889bWwPCJmef/75mbR9QpGEJRFZvEmEGi+UZ7Dxe4HQJSFTMiKFqCgSNCFyCJ02YkVCBQV3qQrPgof02GOPWUKFr4PIGBeigcDRsSMEvqwU28TnhCFipP77wsF4UggaIU7S/f3TsNkHY1u+qC/bI2q8Zt94hv4J0XhVHCseGNtEnxzNdyGKvoJ/nJ9++snG6/zvwcPiGPz38vt5n/PhPTy+n+/0osex8rviv1WI8iBBEyLPMIaG50MVjSiMeeHJkVa/PDBvC++HcSgh0ogETYgCwFiRf5SLBw+HcSU8oeUBj4pMSLwgIdKIBE0IIURRIEETQmRgHI9sR41hiSQiQRNCZGBuGHPiJGgiiUjQhBAZKKVFGS4JmkgiEjQhRAYmX0vQRFKRoAkhMshDE0lGgiZEymFenC8zNWnSJBM0JnwDVUqESAoSNCFSDs9F69mzp1UaoSwXj5zp2rWrrevcubO8NZEYJGhCpJzBgwfbI2LIbkTMVlppJStAzEKxYoobC5EEJGhCpJyJEyfaUwGoeB9fqlatWmplfSFCRIImRMqhGn+HDh1KiJl/grQQSUGCJoSwR9fExYxnqzGWJkRSkKAJIewxN3FB48Gjemq0SBISNCGEPYesVq1aSwjawQcfrMr9IlFI0IQQRsuWLTNiRoYjT8sWIklI0IQQRt++fTNe2iGHHLLcz2UTolBI0IQQxocffuh23HFHE7Rbbrkl/rYQwROUoFF2h8yqddddV0sFFibFYllT6UEUjt69e9u1WHPNNUtcoyQstWvXtnlnK6+8soUcKYEV3yYpy2677SYPM4UEJWgvvfSS23nnnS1VuEePHq5bt25LXbp3715iXUXeL5aF39m8eXOzqm+44Yb4KRV5pFOnTiYIjEUt6/6Lvl/atrl+v7Rt+dunTx8zjCh7FX9/aUtF3i9t22y+z3HfdNNNbsMNN3RTp06NXyJR5AQlaKQIt27dOlMoVZSPkSNHWokiCVphuf76682rGTVqVPwtkUeobLLRRhtZjUqRLoITtFatWrnff/89/pYoA7LRJGiFxwva448/Hn9L5JFffvlFgpZSJGhFgAQtDLygPfbYY/G3RB6RoKUXCVoRIEELAwlaGEjQ0osErQgYMWKEBC0AFHIMAwlaepGgFQHy0MJAHloYSNDSiwStCJCghYEELQwkaOlFglYESNDCQIIWBhK09CJBKwIkaGEgQQsDCVp6kaAVARK0MJCghYEELb1I0IoACVoYSNDCQIKWXiRoRYAELQwkaGEgQUsvErQiQPPQwkDz0MJAgpZeJGhFgDy0MJCHFgYStPQiQSsCJGhhIEELAwlaepGgFQEStDCQoIWBBC29SNCKAAlaGEjQwkCCll4kaEWABC0MJGhhIEFLLxK0IkCCFgYStDCQoKUXCVoRIEELAwlaGEjQ0osErQjQPLQw0Dy0MJCgpRcJWhEgDy0M5KGFgQQtvaRO0P7880/39ttvu6+++mqJ9f/884+bMWOG++STT+z/8jB9+nTXuXNn9+OPP8bfyvDKK6+4Rx55xP3222/xt7JGUgWNjuebb77JvObalHUuS4PPfPvtt+7vv/+Ov5V3QhW0zz//3L300kvx1XauJ0+e7Hr27OnuuOOO+NuJRYKWXlInaNzsl1xyibv11lvd4sWLM+tnz57t2rRp43r16rXE+rIgtETD+eKLL+JvZbjttttc27Zt3U8//RR/K2skNeT4zDPPuMsuuyzz+vXXX3dPPfVUZItlgxHSrVs3t2DBAjvHubx3lkWoIcdRo0a5vfbay/3111+ZdRht9957rzvssMPsGnDsxUJIgvbBBx+UaPtff/21++GHH9z8+fPtnn/zzTfdO++8Y395zf9Tpkyx/zG+eY3h8cYbb1g/xf7867feesv6n19//XWJ74BFixbZfthu0qRJ7v333zcDEiOwWEmdoHEznH766W7TTTd1DzzwgDVsLNWLL77Y1ahRw1166aXu559/tpvgpptucvvvv78bPny4mzlzpnkBn332mXWgPXr0cF26dHEbb7yxmzdvnh3zq6++6vbZZx/XuHFjWwd33XWXO++880rc1Nkknx7ap59+6mbNmmXeqW9ENMSJEyda4/X4xvrCCy9YB+PhHL733nt2ju+77z639dZb23oE6cADD3Qvvvii/Q98LtopffTRRyZgLBwHxzB37lxr3JzvOnXqWMfszz2eGw0ZrzvameeKUD007m/ueYTN8/TTT7vNNtvMHXPMMe722283Qw7oPLm3EUAMP67p2Wef7QYNGmTvP/roo65Zs2b2P/c8okhHGRKhCBr3On3KmDFjMuuI1Fx44YXWtyBWd955p7v88stdrVq13JVXXmkGMO2CfoPrsvnmm7sqVaq4M888096jj5kwYYLbZZddzChnXzvvvLNbY4013MKFCyPf7tw999zjtttuO+sX7r77bnfqqae6ddZZxz4bjWjQ3mhHUWif33333RLrfLtEkEtrT7Q7H93iL6INCCificI9+f333y+xzsN+ljfikjpB4yTTQNdbbz3zyLgJ6Bj32GMPEyduLiybHXbYwUTvgAMOcBtuuKHdUHy2efPmrnbt2u7444+3GwMh4cI/99xz9rpp06Zuzz33dFdffbV5etxU5557btEI2nHHHeeOPvpoO4cffvihCcZuu+3mNtlkE7f33ntnbkTO7fbbb2/nkIbpb+6BAwfa9nSgdJhbbbWVrecaYAzwOdYDYTI6Vh+GPOmkk8yboHM+6KCD3IknnmjeKY2ajqFSpUpum222sc6XewlDgu/iGubDawpV0KBfv35mrPlzybGutdZabvDgwWZINGnSxISpUaNGZmRgyNFGTj75ZNegQQO77rSLli1b2nnmOtNJ8dmPP/449m2FJSRB434YP358Zh2dO8LVtWvXjKeEgUdbwVDzeGE49NBDrQ3Rv3gw4OiP6F8QSF5zHTAeoyCMZ511Viasz/WjndB/eSMTo54IEtfZixpCy1AK7ZDhEgzCP/74w9oegkobRSAJZQP93/PPP+/OOOMM6+/4XfThbDN16lR3//3322cwhAGj9YorrrC+dvTo0eYkAPcf2yK8HHt0OKK8pFLQuMicNDpFbgYuAoJGR8nNxoWqWbOm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oKWXYAXNe2PRJ1SDRE2EigQtDCRo6SVYQUO4eFxMvIbjkEl945sKEQQStDCQoKWXYAUNELFrxra2v0yuZvn25wXxzYQIAglaGEjQ0kvQgubFzC8ImhChIkELAwlaegla0HjuWVTQCD8KESoStDCQoKWXoAWNMTNfxxFvTc9BEyEjQQsDCVp6CVrQABFDzIQIHQlaGEjQ0kvwggZkOwoROhK0MJCgpZdECJoQSUCCFgYStPQiQRMiS0jQwkCCll6CELQpH8ywZcyLk13/EY+VWDrdNbDEOhb/OSFCQIIWBhK09JIXQRsz8WXX6c57XdMLrnP9B/dyU169y338Vn/n5g/J+sK+Jz53h+vdr7trcWUX13vgA/HDESInFLOg/fnnn+63336Lrw4SCVp6ybmgTZn+UUbE4uKT62XhrIEmbm0693YLf/k1fmhCZJV8Ctrvv//uXn/9dTdixAg3evRo9+STT9r3jhw50r344ovxzVeYt99+27300kvun3/+ib8VHBK09JJzQWtzfdcSQpPvpdOtXdyDYx6NH5oQWSWfgvbNN9+4Sy65xO2yyy5u1113ddtvv73ba6+9XL169dxZZ50V33yFeeCBB9wdd9xhntrSQFwnTSp8RrIELb3kXtA63ejGjLzYderTwTU9/6q8hBzHjO37v5Bj+46u9x3t3ZSnz3X9HxoWPzQhsko+BS3KI4884lZZZZXMa0SnY8eOJnAsn3zyia0/99xz3Y033ujatGnjTjjhBDd+/Hj35ptvugMPPNDW4/Xdfffd7vLLL7fPN2nSxN1yyy3mlQ0fPtzdeeedtp9vv/3WNW3a1DVo0MAdf/zxJiDvvPOOq1y5slt33XVd586d3RdffOHuu+8+E1i+66mnnsocX66RoKWXvAia+/jszDJmxIWu/4D27tIuV5vAtbnuevOgEDoWxAhRWtby4IibM59hH03P72gC1qn3FbZ/RMx/pwRN5INCCRpiU6VKlczrF154we28887umGOOcY0aNTKPbdGiRW6dddZxa6+9tjvggAPcBhts4OrWreuOPvpot+2227o111zThACxq1mzpjv22GPdPvvs4+rUqWMCRiizX79+No6G6OEVnnbaaSaYhDvfe+89V6lSJbf55pubCLZt29Ztttlmtv+tttrK7b777pEjzi0StPSSd0ErxCJBE/mgUII2bNiwjKDNmTPH7b///u7iiy92vXv3dl26dHFVq1Z1ffr0sU4eoUGUOnXqZN4U42+ECREmhPC8884z4fP079/ffhchx7vuusu8v3nz5rlu3bq57t27u9NPP91dccUVbvHixW7DDTc0Tw9q1arljjvuONerVy/7ztVXX93Nnj07s99cIkFLLxI0IbJECIL26aefup122sm8Izwjlvr165sgbb311iZycM0115gAPfvss+7ll182QXv66afdOeecY+NxHsKZiNyQIUPcPffc47788kt37bXXui222MLCjnvvvbeFJxE0vD7OAay88spu/fXXd1tuuaXbZptt7LslaCLXSNCEyBIhCNpnn33mdtxxRxMfxrXIhBwzZoz76quvTOTwzPCyrr76auv0ETSyF/fcc0/7yzjbeuutl9k3iSB4dw8++KAbNGiQe+aZZ8yzGzhwoJs7d66936FDB/fHH39YeNJ7aBwPQvjWW2+55557zsKiv/6an0xjCVp6CUbQBnZrbDF4/t5zY0PXrsX2rtEe67nvJ59u79/SsUHm/Tuu28cd12Qz16Ft3RL7KW2RoIl8UChBw/taaaWVMq8JIeIZ7bHHHtaxX3nllTaGVrt2bXfqqae6n376yUQID4rEkOeff97GuPDu8NA23nhjS/bYYYcdzItDiB566CELP86YMcPCjNttt52NvRHeJKTJukMOOcQSQ/DgCDXyecR1tdVWcw0bNowccW6RoKWX4AQtuq5m9VXcacdsbf97QYu+X6PaKiX2U9oiQRP5oFCCNnXqVAv7Rbnttttcq1atbPwKrw1uuukmS+4gPEh4kfG1jz/+2M2cOdPGx2bNmmWfOeigg9ztt99u4kamIvAdCCUZj9OmTbNEE7IhGXfD2+vbt6+NxzGV4P777zdRwTM85ZRTXPv27W27fCFBSy9BC1rHdvXcyiuvZP+XJmhrr1G1xH5KWyRoIh8UStAQmb/++qvEup9//tnEy8M2f//9t/3PX16zHQuvv/76a/Pg8LqAz/rt/XYe9k2YEdgPYUze5290rhreYFlz13KBBC29BC1o74w6LrPOC9rqNavY36qrruzmvnxKif2UtkjQRD4olKBlC0QKT42EkSQjQUsvQQvaaw8dXULQ+P+P6a3d++NOcGvUquJmTmhRYl/xRYIm8kHSBQ0P64cffjBPLclI0NJL0IK2y7Zr28L/pYUc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>

[image2]: <data:image/png;base64,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>

[image3]: <data:image/png;base64,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>

[image4]: <data:image/png;base64,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>

[image5]: <data:image/png;base64,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>