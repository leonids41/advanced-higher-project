import pygame
pygame.init
class Button:
    def __init__(self,x,y,width,height,color,hoverColor,active):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color
        self.hoverColor=hoverColor
        self.active=active

    def GetRect(self):
        buttonRect=pygame.Rect(self.x,self.y,self.width,self.height)
        return buttonRect

    def DrawRect(self,screen,button):
            mouse_x,mouse_y=pygame.mouse.get_pos()
            if self.x<= mouse_x<=self.x+self.width and self.y<=mouse_y<=self.y+self.height:
                pygame.draw.rect(screen,self.hoverColor,button)
                self.active=True
            else:
                pygame.draw.rect(screen,self.color,button)
                self.active==False


