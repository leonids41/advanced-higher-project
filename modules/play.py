import pygame,sys
pygame.init


class Player_Round:
    def __init__(self):
        self.playerName=None
        self.wpm=None
        self.accuracyPercent=None
    
    def setPlayerName(self,enteredName):
        self.playerName=enteredName
    
    def setWPM(self,enteredWPM):
        self.wpm=enteredWPM
    
    def setAccuracy(self,enteredAccuracy):
        self.accuracyPercent=enteredAccuracy

    def displayPlayerRound(self):
        print("Player "+str(self.playerName)+" got a WPM of "+str(self.wpm)+" at an accuracy of "+str(self.accuracyPercent)+"%")

def play(Button,get_font,typing,playerRoundsList,score):
    clock=pygame.time.Clock()
    play_screen=pygame.display.set_mode((1280,720))
    play_screen.fill("black")
    entered_name=''
    running=True
    active=False

    duration=0
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                pygame.quit() 
                sys.exit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                if name_rect.collidepoint(event.pos):
                    active=True
                if thirtySecRect.collidepoint(event.pos):
                    duration=30
                if oneMinRect.collidepoint(event.pos):
                    duration=60
                if threeMinRect.collidepoint(event.pos):
                    duration=180
                if fiveMinRect.collidepoint(event.pos):
                    duration=300
                if confirmRect.collidepoint(event.pos):
                    typing(Button,get_font,currentPlayer,duration,score,playerRoundsList,Player_Round)



            if event.type==pygame.KEYDOWN:
                if active:
                    if event.key==pygame.K_BACKSPACE:
                        entered_name=entered_name[:-1]
                
                    elif event.key==pygame.K_RETURN:
                        entered_name=entered_name
                        active=False

                    else:
                        entered_name+=event.unicode

        detail1=False
        detail2=False
        enter_text=get_font(60).render("Please enter your name:", True,"#703be3")
        enter_rect=enter_text.get_rect(center=(640,70))
        play_screen.blit(enter_text,enter_rect)
        
        enter_duration=get_font(60).render("Select your game duration:", True,"#703be3")
        enter_duration_rect=enter_duration.get_rect(center=(640,300))
        play_screen.blit(enter_duration,enter_duration_rect)

        thirtySecText=get_font(50).render("30s",True,"#703be3")
        thirtySecButton=Button(270,365,120,120,"white","#7be385",False)
        thirtySecRect=thirtySecButton.GetRect()
        thirtySecButton.DrawRect(play_screen,thirtySecRect)
        play_screen.blit(thirtySecText,(thirtySecButton.x+15,thirtySecButton.y+35))

        oneMinText=get_font(50).render("1m",True,"#703be3")
        oneMinButton=Button(470,365,120,120,"white","#7be385",False)
        oneMinRect=oneMinButton.GetRect()
        oneMinButton.DrawRect(play_screen,oneMinRect)
        play_screen.blit(oneMinText,(oneMinButton.x+27,oneMinButton.y+35))

        threeMinText=get_font(50).render("3m",True,"#703be3")
        threeMinButton=Button(670,365,120,120,"white","#7be385",False)
        threeMinRect=threeMinButton.GetRect()
        threeMinButton.DrawRect(play_screen,threeMinRect)
        play_screen.blit(threeMinText,(threeMinButton.x+27,threeMinButton.y+35))

        fiveMinText=get_font(50).render("5m",True,"#703be3")
        fiveMinButton=Button(870,365,120,120,"white","#7be385",False)
        fiveMinRect=fiveMinButton.GetRect()
        fiveMinButton.DrawRect(play_screen,fiveMinRect)
        play_screen.blit(fiveMinText,(fiveMinButton.x+27,fiveMinButton.y+35))

        name_button=Button(390,135,500,90,"white","white",False)
        name_rect=name_button.GetRect()
        name_button.DrawRect(play_screen,name_rect)
        name_text = get_font(50).render(entered_name, True, ("black"))
        play_screen.blit(name_text,(name_rect.x+10,name_rect.y+10))

        confirmText=get_font(75).render("CONFIRM",True,"#703be3")
        confirmButton=Button(340,540,600,100,"white","white",False)
        confirmRect=confirmButton.GetRect()
        
        if len(entered_name) > 0 and active==False:
            name_button=Button(390,135,500,90,"#b5adb8","#b5adb8",False)
            name_button.DrawRect(play_screen,name_rect)
            play_screen.blit(name_text,(name_rect.x+10,name_rect.y+10))
            detail1=True

        if duration > 0:
            if duration==30:
                thirtySecButton=Button(270,365,120,120,"#b5adb8","#b5adb8",False)
                thirtySecButton.DrawRect(play_screen,thirtySecRect)
                play_screen.blit(thirtySecText,(thirtySecButton.x+15,thirtySecButton.y+35))
                detail2=True

            elif duration==60:
                oneMinButton=Button(470,365,120,120,"#b5adb8","#b5adb8",False)
                oneMinButton.DrawRect(play_screen,oneMinRect)
                play_screen.blit(oneMinText,(oneMinButton.x+27,oneMinButton.y+35))
                detail2=True

            elif duration==180:
                threeMinButton=Button(670,365,120,120,"#b5adb8","#b5adb8",False)
                threeMinButton.DrawRect(play_screen,threeMinRect)
                play_screen.blit(threeMinText,(threeMinButton.x+27,threeMinButton.y+35))
                detail2=True

            else:
                fiveMinButton=Button(870,365,120,120,"#b5adb8","#b5adb8",False)
                fiveMinButton.DrawRect(play_screen,fiveMinRect)
                play_screen.blit(fiveMinText,(fiveMinButton.x+27,fiveMinButton.y+35))
                detail2=True

        if detail1==True and detail2==True:
            confirmButton.DrawRect(play_screen,confirmRect)
            play_screen.blit(confirmText,(confirmButton.x+120,confirmButton.y+20))
            currentPlayer=Player_Round()
            currentPlayer.setPlayerName(entered_name)

        pygame.display.update()
        clock.tick(60)