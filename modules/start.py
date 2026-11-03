import pygame,sys
pygame.init



def start(Button,get_font,play,leaderboard,typing,score,playerRoundsList):
    clock=pygame.time.Clock()
    start_screen=pygame.display.set_mode((1280,720))
    start_screen.fill("black")
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                pygame.quit() 
                sys.exit()

            if event.type==pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(event.pos):
                    play(Button,get_font,typing,playerRoundsList,score)
                if leaderboard_rect.collidepoint(event.pos):
                    leaderboard(Button,get_font,playerRoundsList)           
                
        pygame.display.set_caption("Type Master")
        title_text=get_font(100).render("TYPE MASTER", True,"#703be3")
        title_rect=title_text.get_rect(center=(640,150))
        start_screen.blit(title_text,title_rect)

        start_text=get_font(75).render("START",True,"#703be3")
        leaderboard_text=get_font(75).render("LEADERBOARD",True,"#703be3")

        start_button=Button(340,320,600,90,"white","#74698c",False)
        start_rect=start_button.GetRect()
        start_button.DrawRect(start_screen,start_rect)

        leaderboard_button=Button(340,470,600,90,"white","#74698c",False)
        leaderboard_rect=leaderboard_button.GetRect()
        leaderboard_button.DrawRect(start_screen,leaderboard_rect)

        if start_button.active==True:
            hover_start_text=get_font(75).render("START",True,"#bca2f2")
            start_screen.blit(hover_start_text,(start_button.x+180,start_button.y+15))
        else:
            start_screen.blit(start_text,(start_button.x+180,start_button.y+15))

        if leaderboard_button.active==True:
            hover_leaderboard_text=get_font(75).render("LEADERBOARD",True,"#bca2f2")
            start_screen.blit(hover_leaderboard_text,(leaderboard_button.x+30,leaderboard_button.y+15))
        else:
            start_screen.blit(leaderboard_text,(leaderboard_button.x+30,leaderboard_button.y+15))

        pygame.display.update()
        clock.tick(60)