#UKI COMPUTERS, projekat RoboBot
#Obični importi
from sys import platform
import time
import gc
from machine import Pin, freq
from print_error import print_error
import utime
#Protokoli
from nec import NEC_8, NEC_16
from sony import SONY_12, SONY_15, SONY_20
from philips import RC5_IR, RC6_M0
from mce import MCE
#Kraj protokola

p = Pin(16, Pin.IN)
relej1 = Pin(0, Pin.OUT)
relej2 = Pin(1, Pin.OUT)
relej3 = Pin(2, Pin.OUT)
relej4 = Pin(3, Pin.OUT)

relej1.value(1)
relej2.value(1)
relej3.value(1)
relej4.value(1)

def cb(data, addr, ctrl):
    if data < 0:
        print('Nije primljeno. Pokušajte ponovo.')
    else:
        print(data)
        #Podržava daljinski za digitalizaciju i običan iz seta
        if data == 21:
            relej1.value(0)
            relej2.value(0)
            relej3.value(1)
            relej4.value(1)
        if data == 72:
            relej1.value(0)
            relej2.value(0)
            relej3.value(1)
            relej4.value(1)
        if data == 216:
            relej1.value(0)
            relej2.value(0)
            relej3.value(1)
            relej4.value(1)
        if data == 70:
            relej1.value(1)
            relej2.value(1)
            relej3.value(0)
            relej4.value(0)
        if data == 68:
            relej1.value(1)
            relej2.value(1)
            relej3.value(0)
            relej4.value(0)
        if data == 146:
            relej1.value(1)
            relej2.value(1)
            relej3.value(0)
            relej4.value(0)
        if data == 64:
            relej1.value(1)
            relej2.value(1)
            relej3.value(1)
            relej4.value(1)
        if data == 6:
            relej1.value(1)
            relej2.value(1)
            relej3.value(1)
            relej4.value(1)
        if data == 155:
            relej1.value(1)
            relej2.value(1)
            relej3.value(1)
            relej4.value(1)
            
def test(proto=0):
    classes = (NEC_8, NEC_16, SONY_12, SONY_15, SONY_20, RC5_IR, RC6_M0, MCE)
    ir = classes[proto](p, cb)
    ir.error_function(print_error)  # Piše grešku
    try:
        while True:
            print('Pokrece se...')
            time.sleep(5)
            gc.collect()
    except KeyboardInterrupt:
        ir.close()

while True:
    test()
