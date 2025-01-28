import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine
import rp2
import sys

ssid = 'xxx (2)'
password = 123456123456

def connect():
    # Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print(wlan.ifconfig())

connect()

def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket
    connection.bind(address)
    connection.listen(1)
    print(connection)

ip = connect()
open_socket(ip)