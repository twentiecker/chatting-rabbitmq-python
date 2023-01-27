import pika

print("Masukkan nama queue channel untuk mengirim pesan melalui RMQ")
queue_name = input(">> channel: ")
credential = pika.PlainCredentials('TMDG2022', 'TMDG2022')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='rmq2.pptik.id',
    port=5672,
    virtual_host='/TMDG2022',
    credentials=credential
))
channel = connection.channel()
channel.queue_declare(
    queue=queue_name,  # menentukan nama queue
    durable=True  # param untuk mempertahankan queue meskipun server rabbitMQ berhenti
)

# publish pesan (mengirim)
print("Masukkan pesan yang akan dikirim atau 'exit' to close.")
print(f">> tujuan: {queue_name}")
message = input(">> pesan: ")
channel.basic_publish(
    exchange='',
    routing_key=queue_name,  # nama queue
    body=message,  # isi pesan dari queue yang dikirim
    properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)  # pesan disimpan di cache
)
print(f" [x] Sent to {queue_name}")
connection.close()  # menutup koneksi setelah mengirim pesan
