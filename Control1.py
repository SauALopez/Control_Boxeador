import pygame
import serial

Incio=True
estado=2
tiempo=b'1'
caja = b'0'
ser = serial.Serial("COM6",115200)

pygame.init()
screen = pygame.display.set_mode((300,300))
screen.fill((245,230,170))
pygame.display.set_caption('CONTROL BOXEADOR')
fuente = pygame.font.SysFont('comicsans',40)
fuenteD = pygame.font.SysFont('comicsans',25)

print ("Captando una funcion")


class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,screen,outline=None):

        if outline:
            pygame.draw.rect(screen, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)
        pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)

        if self.text!='':
            font = pygame.font.SysFont('comicsans',20)
            text = font.render(self.text,1,(0,0,0))
            screen.blit(text,(self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
            
    def isOver (self,pos):

        if pos[0] > self.x and  pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

def Window0():
    screen.fill((245,230,170))
    caja1Button.draw(screen)
    caja2Button.draw(screen)
    caja3Button.draw(screen)
    textEstado = fuente.render("ESTADO 0",0,(0,0,0))
    screen.blit(textEstado,(80,40))
    txt = fuenteD.render("SELECCIONE CAJA:",0,(0,0,0))
    screen.blit(txt, (80,150))
    

def Window1():
    screen.fill((187,230,170))
    ButtonW.draw(screen)
    ButtonS.draw(screen)
    ButtonA.draw(screen)
    ButtonD.draw(screen)
    ButtonR.draw(screen)
    ButtonF.draw(screen)
    textEstado = fuente.render("ESTADO 1",0,(0,0,0))
    screen.blit(textEstado,(80,40))
    txt = fuenteD.render("BASE",0,(0,0,0))
    screen.blit(txt, (30,165))
    txt = fuenteD.render("BRAZO",0,(0,0,0))
    screen.blit(txt, (115,165))
    txt = fuenteD.render("MANO",0,(0,0,0))
    screen.blit(txt, (210,165))
    
def Window2():
    screen.fill((215,230,170))
    ButtonTime.draw(screen)
    textEstado = fuente.render("ESTADO 2",0,(0,0,0))
    screen.blit(textEstado,(80,40))
    txt = fuenteD.render("Tiempo en segundos de:",0,(0,0,0))
    screen.blit(txt, (60,130))

    
caja1Button = button((255,255,255), 20, 200, 80, 50, 'CAJA 1')
caja2Button = button((255,255,255), 110, 200, 80, 50, 'CAJA 2')
caja3Button = button((255,255,255), 200, 200, 80, 50, 'CAJA 3')

ButtonW = button((255,255,255), 20, 100, 80, 50, 'W')
ButtonS = button((255,255,255), 20, 200, 80, 50, 'S')
ButtonA = button((255,255,255), 110, 100, 80, 50, 'A')
ButtonD = button((255,255,255), 110, 200, 80, 50, 'D')
ButtonR = button((255,255,255), 200, 100, 80, 50, 'R')
ButtonF = button((255,255,255), 200, 200, 80, 50, 'F')

ButtonTime = button((255,255,255), 120, 160, 80, 50, '1')

while Incio:
    if estado == 0:
            Window0()
            pygame.display.update()        
    if estado == 1:
            Window1()
            pygame.display.update() 
    if estado == 2:
            Window2()
            pygame.display.update()
            
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
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            Incio =False
            pygame.quit()
            quit()
                          
        if(estado == 0):
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if caja1Button.isOver(pos):
                    print('CAJA 1')
                    ser.write(b'1')
                if caja2Button.isOver(pos):
                    print('CAJA 2')
                    ser.write(b'2')
                if caja3Button.isOver(pos):
                    print('CAJA 3')
                    ser.write(b'3')
                    
            if event.type == pygame.MOUSEMOTION:
                if caja1Button.isOver(pos):
                    caja1Button.color = (0,180,250)
                else:
                    caja1Button.color = (255,255,255)

                if caja2Button.isOver(pos):
                    caja2Button.color = (0,180,250)
                else:
                    caja2Button.color = (255,255,255)

                if caja3Button.isOver(pos):
                    caja3Button.color = (0,180,250)
                else:
                    caja3Button.color = (255,255,255)
                 
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    ser.write(caja)
                    print("CAJA SELECCIONADA ENVIADA")
                if event.key == pygame.K_1:
                    caja = b'1'
                    print ("CAJA 1")      
                if event.key == pygame.K_2:
                    caja = b'2'
                    print ("CAJA 2")
                if event.key == pygame.K_3:
                    caja = b'3'
                    print ("CAJA 3")
                    
        if(estado == 1):

            if event.type == pygame.MOUSEBUTTONDOWN:
                if ButtonW.isOver(pos):
                    print('W')
                    ser.write(b'W')
                if ButtonS.isOver(pos):
                    print('S')
                    ser.write(b'S')
                if ButtonA.isOver(pos):
                    print('A')
                    ser.write(b'A')
                if ButtonD.isOver(pos):
                    print('D')
                    ser.write(b'D')
                if ButtonR.isOver(pos):
                    print('R')
                    ser.write(b'R')
                if ButtonF.isOver(pos):
                    print('F')
                    ser.write(b'F')    
                    
            if event.type == pygame.MOUSEMOTION:
                if ButtonW.isOver(pos):
                    ButtonW.color = (0,180,250)
                else:
                    ButtonW.color = (255,255,255)

                if ButtonS.isOver(pos):
                    ButtonS.color = (0,180,250)
                else:
                    ButtonS.color = (255,255,255)

                if ButtonA.isOver(pos):
                    ButtonA.color = (0,180,250)
                else:
                    ButtonA.color = (255,255,255)

                if ButtonD.isOver(pos):
                    ButtonD.color = (0,180,250)
                else:
                    ButtonD.color = (255,255,255)

                if ButtonR.isOver(pos):
                    ButtonR.color = (0,180,250)
                else:
                    ButtonR.color = (255,255,255)

                if ButtonF.isOver(pos):
                    ButtonF.color = (0,180,250)
                else:
                    ButtonF.color = (255,255,255)    
            
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
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ButtonTime.isOver(pos):
                    print('TIEMPO ENVIADO')
                    
            if event.type == pygame.MOUSEMOTION:
                if ButtonTime.isOver(pos):
                    ButtonTime.color = (0,180,250)
                else:
                    ButtonTime.color = (255,255,255)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER:
                    ser.write(tiempo)
                    print ("TIEMPO ENVIADO")
                if event.key == pygame.K_1:
                    ButtonTime.text = '1'
                    tiempo=b'1'
                    print ("1 SEGUNDO")
                if event.key == pygame.K_2:
                    ButtonTime.text = '2'
                    tiempo=b'2'
                    print ("2 SEGUNDOS")
                if event.key == pygame.K_3:
                    ButtonTime.text = '3'
                    tiempo=b'3'
                    print ("3 SEGUNDOS")      
                if event.key == pygame.K_4:
                    ButtonTime.text = '4'
                    tiempo=b'4'
                    print ("4 SEGUNDOS")
                if event.key == pygame.K_5:
                    ButtonTime.text = '5'
                    tiempo=b'5'
                    print ("5 SEGUNDOS")
                if event.key == pygame.K_6:
                    ButtonTime.text = '6'
                    tiempo=b'6'
                    print ("6 SEGUNDOS")      
                if event.key == pygame.K_7:
                    ButtonTime.text = '7'
                    tiempo=b'7'
                    print ("7 SEGUNDOS")
                if event.key == pygame.K_8:
                    ButtonTime.text = '8'
                    tiempo=b'8'
                    print ("8 SEGUNDOS")
                if event.key == pygame.K_9:
                    ButtonTime.text = '9'
                    tiempo=b'9'
                    print ("9 SEGUNDOS")      
                   



                    
