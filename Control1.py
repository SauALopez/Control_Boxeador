import pygame
import serial


Incio=True
estado=1
tiempo=b'1'
caja = b'0'
ser = serial.Serial("COM6",115200)

pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption('Pygame Keyboard Test')
pygame.mouse.set_visible(0)
print ("Captando una funcion")
while Incio:
    if ser.inWaiting():
        lectura = ser.read()
        if(lectura == b'0'):
            print("ESTADO 0")
            estado=0
        if(lectura == b'1'):
            print("ESTADO 1")
            estado=1
        if(lectura == b'2'):
            print("ESTADO 2")
            estado=2           
    for event in pygame.event.get():
        if(estado == 0):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    ser.write(caja)
                    print("CAJA SELECCIONADA ENVIADA")
                if event.key == pygame.K_0:
                    caja = b'0'
                    print ("CAJA 0")      
                if event.key == pygame.K_1:
                    caja = b'1'
                    print ("CAJA 1")
                if event.key == pygame.K_2:
                    caja = b'2'
                    print ("CAJA 2")
        if(estado == 1):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    ser.write(b'W');
                    print ("W")      
                if event.key == pygame.K_s:
                    ser.write(b'S');
                    print ("S")
                if event.key == pygame.K_a:
                    ser.write(b'A');
                    print ("A")
                if event.key == pygame.K_d:
                    ser.write(b'D');
                    print ("D")      
                if event.key == pygame.K_r:
                    ser.write(b'R');
                    print ("R")
                if event.key == pygame.K_f:
                    ser.write(b'F');
                    print ("F")                    
        if(estado == 2):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    ser.write(tiempo)
                    print ("TIEMPO ENVIADO")
                if event.key == pygame.K_1:
                    tiempo=b'1'
                    print ("1 SEGUNDO")
                if event.key == pygame.K_2:
                    tiempo=b'2'
                    print ("2 SEGUNDOS")
                if event.key == pygame.K_3:
                    tiempo=b'3'
                    print ("3 SEGUNDOS")      
                if event.key == pygame.K_4:
                    tiempo=b'4'
                    print ("4 SEGUNDOS")
                if event.key == pygame.K_5:
                    tiempo=b'5'
                    print ("5 SEGUNDOS")
                if event.key == pygame.K_6:
                    tiempo=b'6'
                    print ("6 SEGUNDOS")      
                if event.key == pygame.K_7:
                    tiempo=b'7'
                    print ("7 SEGUNDOS")
                if event.key == pygame.K_8:
                    tiempo=b'8'
                    print ("8 SEGUNDOS")
                if event.key == pygame.K_9:
                    tiempo=b'9'
                    print ("9 SEGUNDOS")      
                   



                    
