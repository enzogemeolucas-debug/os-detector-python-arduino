import serial
import platform
import time

arduino = serial.Serial('/dev/ttyUSB0', 9600) #you can change to your serial port and baud

time.sleep(3)

sistema = platform.system()

if sistema == 'Linux':
    distrubuicao = platform.freedesktop_os_release()["PRETTY_NAME"]
    if len(distrubuicao) > 16:
        mensagem = 'Linux'
    else:
        mensagem = distrubuicao
elif sistema == 'Windows':
    versao = platform.win32_ver()[0]

    if versao == '10':
        mensagem = 'Windows 10'
    elif versao == '11':
        mensagem = 'Windows 11'
    else:
        mensagem = f'Windows {versao}'
elif sistema == 'Darwin':
    mensagem = "MacOS"
else:
    mensagem = sistema

print("Enviando:", mensagem)

arduino.write((str(mensagem) + '\n').encode())
arduino.flush()
time.sleep(1)
arduino.close()
