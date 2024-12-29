import pika
import time


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='mq'))
    channel = connection.channel()

    def callback(ch, method, properties, body):
        time.sleep(5)
        print(f" [x] Received {body}")

    queue_name = 'hello'

    channel.queue_declare(queue=queue_name)
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    main()
