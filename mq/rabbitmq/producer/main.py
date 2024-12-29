from datetime import datetime
import pika

import time

def send_message(message):
    with pika.BlockingConnection(pika.ConnectionParameters(host='mq')) as connection:
        channel = connection.channel()
        queue_name = 'hello'
        channel.queue_declare(queue=queue_name)
        message = 'Hello World! ' + str(datetime.now())
        channel.basic_publish(exchange='', routing_key=queue_name, body=message)
        print(f" [x] Sent '{message}' to '{queue_name}'")


def main():
    print("start producer")
    while True:
        message = f"Hello World! {datetime.now()}"
        send_message(message)

        time.sleep(1)

if __name__ == '__main__':
    main()
