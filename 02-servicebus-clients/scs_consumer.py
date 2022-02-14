#!/usr/bin/env python3
import json
import time 
import configparser
from azure.servicebus import ServiceBusClient, ServiceBusMessage


def get_config(config_file='config.ini'):
    config = configparser.ConfigParser()
    config.read(config_file)
    connection_string  = config['DEFAULT']['CONNECTION_STR'].strip('"').strip("'")
    queue_name = config['DEFAULT']['QUEUE_NAME'].strip('"').strip("'")
    return connection_string, queue_name


def send_single_message(sender, index):
    
    message_body = json.dumps( { "sisid": f"{index + 999111222}"} )
    message = ServiceBusMessage(message_body)
    sender.send_messages(message)
    print(f"sent {message_body}")


def main():

    CONNECTION_STR, QUEUE_NAME = get_config()

    print(f" *** consuming from queue {QUEUE_NAME} *** ")

    servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)

    with servicebus_client:
        receiver = servicebus_client.get_queue_receiver(queue_name=QUEUE_NAME, max_wait_time=30)
        with receiver:
            for msg in receiver:
                print("Received: " + str(msg))
                receiver.complete_message(msg)
    
    print(f"=== done consuming from queue {QUEUE_NAME} ===")




if __name__ == '__main__':
    main()            