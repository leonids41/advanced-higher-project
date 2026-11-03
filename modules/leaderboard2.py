import pygame,sys, modules,sqlite3
pygame.init


def leaderboard2(Button,get_font,playerRoundsList):
    clock=pygame.time.Clock()
    leaderboard2_screen=pygame.display.set_mode((1280,720))
    leaderboard2_screen.fill("black")
    pygame.draw.rect(leaderboard2_screen,"#f8f5ff",pygame.Rect(100,130,1050,485))
    connection=sqlite3.connect("Assets/leaderboard.db")
    cursor=connection.cursor()
    createQuery="CREATE TABLE IF NOT EXISTS score (roundID integer NOT NULL, playerName varchar(30) NOT NULL, WPM smallint NOT NULL, accuracyPercent tinyint NOT NULL, PRIMARY KEY(roundID))"
    cursor.execute(createQuery)
    connection.commit()

    cursor.execute("SELECT playerName, MAX(WPM), accuracyPercent FROM score GROUP BY playerName ORDER BY WPM DESC, accuracyPercent DESC, playerName ASC;")
    results=(cursor.fetchall())
    connection.commit()
    print("Query ran successfully")
    connection.close()
    clicked=False
    x=0
    count=0
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                pygame.quit() 
                sys.exit()
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                if arrow_rect.collidepoint(event.pos):
                    modules.leaderboard(Button,get_font,playerRoundsList)

                if back_rect.collidepoint(event.pos):
                    modules.start(Button,get_font,modules.play,modules.leaderboard,modules.typing,modules.score,playerRoundsList)

                if down_rect.collidepoint(event.pos):
                    clicked=True
                    pygame.draw.rect(leaderboard2_screen,"#f8f5ff",pygame.Rect(100,200,1050,390))
                    pygame.display.update((100,230,1050,300))
                    
        title=get_font(60).render("Each player's highest WPM",True,"#703be3")
        title_rect=title.get_rect(center=(640,60))
        leaderboard2_screen.blit(title,title_rect)
        heading=get_font(55).render("Name                  WPM             Accuracy",True,"#703be3")
        heading_rect=heading.get_rect(center=(610,170))
        leaderboard2_screen.blit(heading,heading_rect)
        back_text=get_font(45).render("BACK",True,"#703be3")
        back_button=Button(515,628,250,80,"#f8f5ff","#f8f5ff",False)
        back_rect=back_button.GetRect()
        back_button.DrawRect(leaderboard2_screen,back_rect)
        down_button=Button(600,590,90,20,"#f8f5ff","#f8f5ff",False)
        down_rect=down_button.GetRect()
        down_button.DrawRect(leaderboard2_screen,down_rect)
        arrow_button=Button(15,260,60,60,"#f8f5ff","#f8f5ff",False)
        arrow_rect=arrow_button.GetRect()
        arrow_button.DrawRect(leaderboard2_screen,arrow_rect)
        pygame.draw.polygon(leaderboard2_screen, ("#703be3"), ((30,290),(50,260),(50,320)))
        pygame.draw.polygon(leaderboard2_screen, ("#703be3"), ((640,610),(615,600),(665,600)))
        leaderboard2_screen.blit(back_text,(back_button.x+60,back_button.y+20))
        if x==0 or clicked==True:
            for loop in range(x,len(results)):
                shift=37
                current_name=get_font(25).render(str(results[loop][0]),True,"#703be3")
                current_wpm=get_font(25).render(str(results[loop][1]),True,"#703be3")
                current_accuracy=get_font(25).render((str(results[loop][2])+"%"),True,"#703be3")
                current_name_rect=current_name.get_rect(center=(210,220+(shift*count)))
                current_wpm_rect=current_wpm.get_rect(center=(570,220+(shift*count)))
                current_accuracy_rect=current_accuracy.get_rect(center=(900,220+(shift*count)))
                leaderboard2_screen.blit(current_name,current_name_rect)
                leaderboard2_screen.blit(current_wpm,current_wpm_rect)
                leaderboard2_screen.blit(current_accuracy,current_accuracy_rect)
                count=count+1
                clicked=False
                if loop==x+9 or count==len(results):
                    shift=37
                    x=loop
                    count=0
                    clicked=False
                    break
        pygame.display.update()
    clock.tick(60)