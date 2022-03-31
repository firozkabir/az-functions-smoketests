#!/usr/bin/env python3
import json
import time
import configparser
from azure.servicebus import ServiceBusClient, ServiceBusMessage
import pandas as pd
import uuid


def get_config(config_file='config.ini'):
    config = configparser.ConfigParser()
    config.read(config_file)
    connection_string = config['DEFAULT']['CONNECTION_STR'].strip(
        '"').strip("'")
    queue_name = config['DEFAULT']['QUEUE_NAME'].strip('"').strip("'")
    return connection_string, queue_name


def send_single_message(sender, item):

    message_body = json.dumps(item)
    message = ServiceBusMessage(message_body)
    sender.send_messages(message)
    print(f"sent {message_body}")


def get_data_dict(file="./demo_profile.csv"):
    df = pd.read_csv(file)
    df['birthdate'] = df['birthdate'].apply(str)
    df['requestid'] = df.apply(lambda _: str(uuid.uuid4()), axis=1)
    del df['sisid']
    dict_list = df.to_dict(orient='records')
    return dict_list


def main():

    CONNECTION_STR, QUEUE_NAME = get_config()

    print(
        f" *** producing messages to queue {QUEUE_NAME}, waiting 5 seconds between each message *** ")

    dict_list = get_data_dict()
    servicebus_client = ServiceBusClient.from_connection_string(
        conn_str=CONNECTION_STR, logging_enable=True)
    with servicebus_client:
        sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
        with sender:
            for item in dict_list:
                send_single_message(sender, item)
                # time.sleep(5)

    print(f"=== done producing to queue {QUEUE_NAME} ===")


if __name__ == '__main__':
    main()
