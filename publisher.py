import pika

input("Tekan [enter] untuk inisialisasi RMQ parameters.")
credential = pika.PlainCredentials('TMDG2022', 'TMDG2022')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='rmq2.pptik.id',
    port=5672,
    virtual_host='/TMDG2022',
    credentials=credential
))
print(">> Inisialisasi RMQ parameters berhasil!!")
print("=============================================================")

input("Tekan [enter] untuk membuka koneksi ke RMQ.")
channel = connection.channel()
print(">> Koneksi ke RMQ berhasil dibuka!!")
print("=============================================================")

print("Masukkan nama queue channel untuk mengirim pesan melalui RMQ.")
queue_name = input(">> channel: ")
channel.queue_declare(
    queue=queue_name,  # menentukan nama queue
    durable=True  # param untuk mempertahankan queue meskipun server rabbitMQ berhenti
)

# publish pesan (mengirim)
print("Masukkan pesan yang akan dikirim atau ketik 'exit' to close.")
print(f">> tujuan: {queue_name}")
while True:
    message = input(">> pesan: ")
    if message == 'exit':
        break

    channel.basic_publish(
        exchange='',
        routing_key=queue_name,  # nama queue
        body=message,  # isi pesan dari queue yang dikirim
        properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)  # pesan disimpan di cache
    )
    print(f" [x] Sent to {queue_name}")
connection.close()  # menutup koneksi setelah mengirim pesan
