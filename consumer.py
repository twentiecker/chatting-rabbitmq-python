import pika


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)  # mempertahankan pesan di rabbitMQ walaupun receiver meninggoy


credential = pika.PlainCredentials('TMDG2022', 'TMDG2022')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='rmq2.pptik.id',
    port=5672,
    virtual_host='/TMDG2022',
    credentials=credential
))
channel = connection.channel()
print("Masukkan nama queue channel untuk menerima pesan melalui RMQ.")
queue_name = input(">> channel: ")
channel.queue_declare(
    queue=queue_name,  # nama queue
    durable=True  # untuk mempertahankan queue meskipun server rabbitMQ berhenti
)

# consume pesan (menerima)
channel.basic_qos(prefetch_count=1)  # hanya akan memberikan satu tugas dulu sampe selesai
channel.basic_consume(
    queue=queue_name,  # nama queue
    on_message_callback=callback  # memanggil fungsi callback
)

print('Menunggu pesan masuk...')
channel.start_consuming()  # bersifat standby
