import pygame,sys, modules
pygame.init


def leaderboard(Button,get_font,playerRoundsList):
    clock=pygame.time.Clock()
    leaderboard_screen=pygame.display.set_mode((1280,720))
    leaderboard_screen.fill("black")
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                pygame.quit() 
                sys.exit()
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(event.pos):
                    modules.start(Button,get_font,modules.play,modules.leaderboard,modules.typing,modules.score,playerRoundsList)
                
                if arrow_rect.collidepoint(event.pos):
                    modules.leaderboard2(Button,get_font,playerRoundsList)
                    
                    
        pygame.draw.rect(leaderboard_screen,"#f8f5ff",pygame.Rect(100,130,1050,485))
        listsize = len(playerRoundsList)
        swapped = True
        while swapped and listsize  >= 0:
            swapped = False
            for i in range(listsize-1):
                if playerRoundsList[i].wpm < playerRoundsList[i+1].wpm:
                    temp = playerRoundsList[i]
                    playerRoundsList[i] = playerRoundsList[i+1]
                    playerRoundsList[i+1] = temp
                    swapped = True
                elif playerRoundsList[i].wpm==playerRoundsList[i+1].wpm:
                    if playerRoundsList[i].accuracyPercent<playerRoundsList[i+1].accuracyPercent:
                        temp = playerRoundsList[i]
                        playerRoundsList[i]= playerRoundsList[i+1]
                        playerRoundsList[i+1] = temp
                        swapped = True
            listsize -= 1
        title=get_font(60).render("Top WPMs of all time",True,"#703be3")
        title_rect=title.get_rect(center=(640,60))
        leaderboard_screen.blit(title,title_rect)
        heading=get_font(55).render("Name                  WPM             Accuracy",True,"#703be3")
        heading_rect=heading.get_rect(center=(610,170))
        leaderboard_screen.blit(heading,heading_rect)
        back_text=get_font(45).render("BACK",True,"#703be3")
        back_button=Button(515,628,250,80,"#f8f5ff","#f8f5ff",False)
        back_rect=back_button.GetRect()
        back_button.DrawRect(leaderboard_screen,back_rect)
        arrow_button=Button(1180,260,60,60,"#f8f5ff","#f8f5ff",False)
        arrow_rect=arrow_button.GetRect()
        arrow_button.DrawRect(leaderboard_screen,arrow_rect)
        pygame.draw.polygon(leaderboard_screen, ("#703be3"), ((1200,320),(1200,260),(1220,290)))
        leaderboard_screen.blit(back_text,(back_button.x+60,back_button.y+20))
        for loop in range(len(playerRoundsList)):
            shift=37
            current_name=get_font(25).render(str(playerRoundsList[loop].playerName),True,"#703be3")
            current_wpm=get_font(25).render(str(playerRoundsList[loop].wpm),True,"#703be3")
            current_accuracy=get_font(25).render((str(playerRoundsList[loop].accuracyPercent)+"%"),True,"#703be3")
            current_name_rect=current_name.get_rect(center=(210,220+(shift*loop)))
            current_wpm_rect=current_wpm.get_rect(center=(570,220+(shift*loop)))
            current_accuracy_rect=current_accuracy.get_rect(center=(900,220+(shift*loop)))
            leaderboard_screen.blit(current_name,current_name_rect)
            leaderboard_screen.blit(current_wpm,current_wpm_rect)
            leaderboard_screen.blit(current_accuracy,current_accuracy_rect)
            if loop==9:
                break
        
        pygame.display.update()
    clock.tick(60)