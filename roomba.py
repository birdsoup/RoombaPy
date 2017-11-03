import RPi.GPIO as GPIO
import serial
import time
import struct

class Roomba(object):
    SAFE = 131
    FULL = 132

    BAUD_RATES = [57600, 19200]

    def __init__(self, dd_pin=7, baud_rate=BAUD_RATES[0], time_out=3.0):
        self.dd_pin = dd_pin
        
        port = serial.Serial("/dev/ttyAMA0", baudrate=baud_rate, timeout=time_out)
        port.close()
        port.open()
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(7, GPIO.OUT)

    def turn_on(self):
        GPIO.output(7, GPIO.HIGH)
        time.sleep(.1)
        GPIO.output(7, GPIO.LOW)
        time.sleep(.5)
        GPIO.output(7, GPIO.HIGH)
        time.sleep(2)

    def set_mode(self, mode):
        turn_on()
        write_num(128)
        write_num(mode)
        time.sleep(1)

    def safe_mode(self):
        set_mode(SAFE)

    def full_mode(self):
        set_mode(FULL)

    def passive_mode(self):
        set_mode(PASSIVE)

    def set_digits(self, digit1, digit2, digit3, digit4):
        safe_mode()
        write_num(164)
        port.write(digit1)
        port.write(digit2)
        port.write(digit3)
        port.write(digit4)

    def set_digits_string(self, msg):
        set_digits(msg[0], msg[1], msg[2], msg[3])

    def clean(self):
        turn_on()
        write_num(135)

    def dock(self):
        turn_on()
        write_num(143)

    def power(self):
        write_num(133)

    #I think this should change the baud rate, untested
    def change_baudrate(self):
        power()
        turn_on()
        time.sleep(2)
        GPIO.output(7, GPIO.HIGH)
        time.sleep(0.250)
        GPIO.output(7, GPIO.LOW)
        time.sleep(0.250)
        GPIO.output(7, GPIO.HIGH)
        time.sleep(0.250)
        GPIO.output(7, GPIO.LOW)
        time.sleep(0.250)
        GPIO.output(7, GPIO.HIGH)
        time.sleep(0.250)
        GPIO.output(7, GPIO.LOW)
        time.sleep(0.250)
        GPIO.output(7, GPIO.HIGH)
        time.sleep(2)
    
    #todo: add drive, drive direct, led stuff, low side drivers (both methods), send ir, song, play song, sensors, query list, stream, pause/resume stream, script, play script, show script, wait time, wait distance, wait angle

    def write_num(num):
        port.write(struct.pack('!B', num))

