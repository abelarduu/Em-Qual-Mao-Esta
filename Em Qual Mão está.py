###################
#Em Qual Mão Está?#
###################
import pyxel

class Hand(object):
    def __init__(self, x=int, y=int, imgx=int, imgy=int, w=int, h=int):
        self.x, self.y= x,y
        self.w, self.h= w,h
        self.imgx, self.imgy= imgx,imgy
        self.ring= pyxel.rndi(0,1)

    #Método de interação com as mãos
    def verClick(self):
        if pyxel.mouse_x >= self.x+4 and pyxel.mouse_x <= self.x +self.w-4:
            if pyxel.mouse_y >= self.y and pyxel.mouse_y <= self.y +self.h-7:
                self.imgx= 32       #Troca de sprite
                if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                    if self.ring:
                        self.imgx= 128  #Troca de sprite(com o anel)
                    else:self.imgx= 96  #Troca de sprite(sem o anel)
                elif pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
                    self.ring=pyxel.rndi(0,1)
        else: self.imgx=0    #Troca de sprite
 
    #Método de atualização da mão na interface
    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.imgx, self.imgy, self.w, self.h)

class Game:
    def __init__(self):
        pyxel.init(90,140,"Em Qual Mão está?")
        #Declarando variaveis
        self.play= False
        self.rightHand= Hand(10,50,0,0,32,32)#13
        self.leftHand= Hand(42,50,0,32,32,32)#45
        self.handsList= [self.rightHand,self.leftHand]
        pyxel.load("resources/Em_Qual_Mão_Está.pyxres")
        pyxel.run(self.update, self.draw)

    #Método de verificação de interação a cada quadro
    def update(self):
        #se o botão play for apertado:
        if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT): self.play=True

        if self.play:
            #Evitando que o anel surja nas 2 mãos
            if self.rightHand.ring == 1: self.leftHand.ring= 0
            if self.rightHand.ring== 0:  self.leftHand.ring= 1
            #if self.leftHand.ring == 1: self.rightHand.ring= 0
            #if self.leftHand.ring== 0:  self.rightHand.ring= 1
            
            #Verificando interação com os Objetos
            for hand in self.handsList:
                hand.verClick()
        else: pass
    #Método de atualização da interface
    def draw(self):
        pyxel.cls(0)
        pyxel.mouse(True)
        if self.play:
            #Iserindo/Desenhando Objetos na tela
            for hand in self.handsList:
                hand.draw()
        else:
            pyxel.blt(0,0,1,0,0,90,90)
            pyxel.text(3,110,"Clique para continuar", pyxel.frame_count % 8)
#Verificação de execução direta do módulo
if __name__ == "__main__":
    Game()