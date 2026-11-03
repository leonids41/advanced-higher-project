import pygame,sys
pygame.init


def ReadFileIntoParagraphs(filename):
        
    strip = "\n"
    with open(filename) as readfile:
        everything = readfile.read()
        paragraphs = everything.split(strip)
            
    return paragraphs


def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = 6
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1
        if y + fontHeight > rect.bottom:
            break

        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1
    
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        text = text[i:]
        pygame.display.update()


def typing(Button,get_font,currentPlayer,duration,score,playerRoundsList,Player_Round):
    clock=pygame.time.Clock()
    typing_screen=pygame.display.set_mode((1280,720))
    typing_screen.fill("black")
    font = pygame.font.Font("Assets/font.ttf", 35)
    running=True
    started=False
    wrong=0
    total=0
    original_time=duration/60
    time_delay = 1000
    timer_event = pygame.USEREVENT
    pygame.time.set_timer(timer_event , time_delay )
    letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T',
             'U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n',
             'o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8',
             '9','0','-',' ','.',',','?']
    index=0
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                pygame.quit() 
                sys.exit()

            elif event.type==timer_event:
                total_mins = duration//60
                total_sec = duration-(60*(total_mins))
                pygame.draw.rect(typing_screen,"black",(260,20,1000,100))
                text = font.render(("Time left: "+str(total_mins)+":"+str(total_sec)), True, "#703be3")
                typing_screen.blit(text, (460, 20))
                pygame.display.update(260,20,1000,100)
                duration=duration-1
                if duration<-1:
                    current_wpm=int((total/5)/(original_time))
                    if total>0:
                        current_accuracy=int(((total-wrong)/total)*100)
                    else:
                        current_accuracy=0
                    currentPlayer.setWPM(current_wpm)
                    currentPlayer.setAccuracy(current_accuracy)
                    playerRoundsList.append(currentPlayer)
                    score(Button,get_font,currentPlayer,playerRoundsList,typing,Player_Round,duration,original_time)
            
            if event.type==pygame.KEYDOWN:
                if started==False:
                    size=len(paragraphs[index])
                    count=0
                    started=True
                
                if started==True:
                    if (event.unicode in letters) and count<size:
                        current_letter=(paragraphs[index])[count]
                        
                        if event.unicode==current_letter:
                            count=count+1
                            total=total+1
                            drawText(typing_screen,(paragraphs[index])[0:count],"gray",pygame.Rect(100,150,1050,700),font)
                            
                        if event.unicode!=current_letter:
                            count=count+1
                            total=total+1
                            wrong=wrong+1
                            drawText(typing_screen,(paragraphs[index])[0:count],"gray",pygame.Rect(100,150,1050,700),font)
                            

                    elif count==size:
                        index=index+1
                        started=False
                        pygame.draw.rect(typing_screen,"black",pygame.Rect(100,150,1500,700))
                        pygame.display.update((100,150,1500,700))

        paragraphs=ReadFileIntoParagraphs("Assets/paragraph_list.txt")
        if started==False:
            drawText(typing_screen,paragraphs[index],"white",pygame.Rect(100,150,1050,700),font)

        
        

        pygame.display.update()
        clock.tick(60)