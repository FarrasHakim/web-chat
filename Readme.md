## Assignment 3 
### Nama: Muhammad Farras Hakim
### NPM: 1706024513

### 1. Web Server
Aplikasi ini terletak pada folder web. Web server dibuat dengan menggunakan framework django.

Cara menjalankan:

1. Pastikan python, pip, dan rabbitmq sudah terinstall di komputer (Selama pengembangan versi yang digunakan adalah python 3.8 dan rabbitmq 3.8.14)
2. Pastikan python dan rabbitmq dapat dipanggil dari terminal
3. Buat env baru dengan syntax `python -m venv env`
4. Activate env tersebut
5. Install requirements dengan `pip install -r requirements.txt`
6. Masuk ke folder web
7. Jalankan `python manage.py runserver`

### 2. Jam Service 

Cara menjalankan:

1. Pastikan python, pip, dan rabbitmq sudah terinstall di komputer (Selama pengembangan versi yang digunakan adalah python 3.8 dan rabbitmq 3.8.14)
2. Pastikan python dan rabbitmq dapat dipanggil dari terminal
3. Nyalakan rabbitmq
4. Jalankan syntax `python jam-service.py`
   
### Cara kerja aplikasi:
- Saat pengguna mengirim text message, backend akan publish message tersebut ke queue di rabbitmq
- Saat di queue tersebut ada message yang masuk, frontend akan consume message tersebut karena sudah subscribe ke queue tersebut
- Dalam message tersebut terdapat sessionId pengirim dan messagenya sehingga frontend dapat membedakan mana message dari pengirim dan mana message yang dari pengguna dan message tersebut akan ditampilkan dengan tmapilan yang sesuai dengan pengirimnya