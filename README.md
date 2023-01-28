# Aplikasi Chatting dengan RabbitMQ

## Setup Projects

Projects ini dibuat dengan menggunakan <b>PyCharm</b>. Untuk melakukan setup project cukup lakukan clone pada menu Git>
Clone pada aplikasi PyCharm yang anda gunakan. Kemudian masukkan link URL yang ada pada
tombol <span><button style="background-color:#2ea043; border:2px solid #2ea043; border-radius: 5px; color: white">
Code</button></span> atau pada link di bawah ini.

```
https://github.com/twentiecker/chatting-rabbitmq-python.git
```

## Setup RabbitMQ libraries

```
pip install pika
```

Library ini digunakan untuk melakukan komunikasi dengan RabbitMQ melalui protocol <b>AMQP 0-9-1</b>. <br/><br/>
Dokumentasi lengkap mengenai library <b>pika</b> dapat dilihat pada link berikut: https://pika.readthedocs.io/en/stable/

## Setup PyInstaller libraries

```
pip install pyinstaller
```

Library ini digunakan untuk membuat executable file dari file python yang sudah kita buat. <br/><br>
Dokumentasi lengkap mengenai library <b>pyinstaller</b> dapat dilihat pada link
berikut: https://pyinstaller.org/en/stable/