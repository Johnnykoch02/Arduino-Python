from numpy import int256


HIGH = 1
LOW = 0
INPUT = 0
OUTPUT = 1
PI = 3.1415926535897932384626433832795
def radians(deg):
    return deg * PI / 180
def degrees(rad):
    return rad * 180 / PI
def pinMode(pin, mode):
    print(pin, mode)
def digitalWrite(pin, val):
    print(pin, val)
def digitalRead(pin):
    pass
def analogRead(pin):
    pass
def analogWrite(pin, val):
    print(pin, val)
def pulseIn(pin, state, timeout) -> int256:
    return 0
def delay(millis):
    pass
def delayMicroseconds(micros):
    pass
def millis() ->int:
    return 0

class Serial(object):
    def __new__(cls):
        if not hasattr(cls,'instance'):
            cls.instance = super(Serial, cls).__new__(cls)
        return cls.instance
    def begin(self, baudrate):
        pass
    def print(self, data):
        pass
    def println(self, data):
        pass


