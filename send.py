#! /usr/bin/python3
import time
import sys
import glob
import serial
import binascii

def serial_ports():
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result
if __name__ == '__main__':
    print("\nPuertos disponibles :\n")
    print(serial_ports())
    time.sleep(0.1)
    print("\nEscriba el puerto que desea utilizar\n")
    time.sleep(0.1)
    puerto = input()
    print("\nUsted selecciono el puerto: " + puerto +"\n")
    ser = serial.Serial(puerto, 19200)
    time.sleep(1)
try:
    ser.write(b"+++")
    time.sleep(2)
    ser.write(b'+++')
    time.sleep(2)
    ser.write(b'+++\r\n')
    time.sleep(2)
    ser.write(b'ATO70\r\n')
    time.sleep(2)
    ser.write(b'AT$SF=12\r\n')
    time.sleep(5)
    while True:
            print("Escriba el mensaje o exit() para salir\n")
            time.sleep(0.1)
            mensaje = input()
            if mensaje == "exit()":
                 break
            mensajeh =binascii.hexlify(mensaje.encode())
            print("\nEnviando " + mensaje + " a: " + puerto + ". porfavor espere ...\n")
            mensajef=(b'AT$SF='+mensajeh+b'\r\n')
            ser.write(mensajef)
            time.sleep(5)
            print("Mensaje enviado\n")
finally:
    ser.write(b'ATQ\r\n')
    ser.close()