import sys
import time
import random
from Adafruit_IO import MQTTClient

AIO_FEED_ID = ""
AIO_USERNAME = "tuanh"
<<<<<<< HEAD
AIO_KEY = "aio_AELL05qaVvxtcdQZzDiNRGN0qXdf"
=======
AIO_KEY = ""
>>>>>>> a40df31fd8adeb6e1079b21bbef8dd007d8189bf
AIO_IDs = ["button1", "button2"]


def connected(client):
    print("Ket noi thanh cong ...")
    client.subscribe(AIO_FEED_ID)
    for i in AIO_IDs:
        client.subscribe(i)

def subscribe(client, userdata, mid, granted_qos):
    print("Subscribe thanh cong ...")


def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit(1)


def message(client, feed_id, payload):
    print("Nhan du lieu: " + payload)


client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    time.sleep(5)
    value1 = random.randint(20, 70)
    value2 = random.randint(0, 100)
    value3 = random.randint(0, 1000)
    print("Updating ...")
    client.publish("sensor1", value1)
    client.publish("sensor2", value2)
    client.publish("sensor3", value3)
    pass
