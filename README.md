# Aplikasi Chatting dengan RabbitMQ

## Setup Projects

Projects ini dibuat dengan menggunakan <b>PyCharm</b>. Untuk melakukan setup project cukup lakukan clone pada
menu <code>Git > Clone</code> pada aplikasi <b>PyCharm</b> yang anda gunakan. Kemudian masukkan link URL yang ada di
bawah ini.

```
https://github.com/twentiecker/chatting-rabbitmq-python.git
```

## Demo Aplikasi

Aplikasi ini menghasilkan dua aplikasi, yaitu consumer.exe dan producer.exe. Producer berperan sebagai pengirim pesan
sedangkan Consumer berperan sebagai penerima pesan. Aplikasi demo berada pada folder <code>dist/</code>.

## Setup RabbitMQ libraries

```
pip install pika
```

Library ini digunakan untuk melakukan komunikasi dengan RabbitMQ melalui protocol <b>AMQP 0-9-1</b>. <br/>
Dokumentasi lengkap mengenai library <b>pika</b> dapat dilihat pada link berikut: https://pika.readthedocs.io/en/stable/

## Setup PyInstaller libraries

```
pip install pyinstaller
```

Library ini digunakan untuk membuat executable file dari file python yang sudah kita buat. <br/>
Dokumentasi lengkap mengenai library <b>pyinstaller</b> dapat dilihat pada link
berikut: https://pyinstaller.org/en/stable/