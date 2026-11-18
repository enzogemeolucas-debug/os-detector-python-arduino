import serial
import platform
import time

arduino = serial.Serial('/dev/ttyUSB0', 9600)

time.sleep(3)

sistema = platform.system()

if sistema == 'Linux':
    mensagem = "Linux"
elif sistema == 'Windows':
    versao = platform.win32_ver()[0]

    if versao == '10':
        mensagem = 'Windows 10'
    elif versao == '11':
        mensagem = 'Windows 11'
    else:
        mensagem = f'Windows {versao}'
elif sistema == 'Darwin':
    mensagem = "Mac OS"
else:
    mensagem = sistema

print("Enviando:", mensagem)

arduino.write((mensagem + '\n').encode())
arduino.flush()

time.sleep(1)
arduino.close()