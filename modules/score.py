import pygame,sys, modules,sqlite3
pygame.init




def insertVaribleIntoTable(roundID, currentPlayer):
    try:
        sqliteConnection = sqlite3.connect("Assets/leaderboard.db")
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO score
                          (roundID, playerName, WPM, accuracyPercent) 
                          VALUES (?, ?, ?, ?);"""

        data_tuple = (roundID, currentPlayer.playerName, currentPlayer.wpm, currentPlayer.accuracyPercent)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into score table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")



def score(Button,get_font,currentPlayer,playerRoundsList,typing,Player_Round,duration,original_time):
    connection=sqlite3.connect("Assets/leaderboard.db")
    cursor = connection.cursor()
    createQuery="CREATE TABLE IF NOT EXISTS score (roundID integer NOT NULL, playerName varchar(30) NOT NULL, WPM smallint NOT NULL, accuracyPercent tinyint NOT NULL, PRIMARY KEY(roundID))"
    cursor.execute(createQuery)
    connection.close()
    clock=pygame.time.Clock()
    score_screen=pygame.display.set_mode((1280,720))
    score_screen.fill("black")
    pygame.draw.rect(score_screen,"#f8f5ff",pygame.Rect(290,200,700,270))
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                pygame.quit() 
                sys.exit()
            
            if event.type==pygame.MOUSEBUTTONDOWN:
                if restart_rect.collidepoint(event.pos):
                    insertVaribleIntoTable((len(playerRoundsList)),currentPlayer)
                    restart_name=currentPlayer.playerName

                    currentPlayer=Player_Round()
                    print("Duration now is "+str(duration))
                    print("Player name now is "+str(currentPlayer.playerName))
                    

                    currentPlayer.playerName=restart_name
                    duration=int(original_time*60)
                    print("Duration now is "+str(duration))
                    print("Player name now is "+str(currentPlayer.playerName))
                    
                    
                    typing(Button,get_font,currentPlayer,duration,score,playerRoundsList,Player_Round)
                    
                if quit_rect.collidepoint(event.pos):
                    insertVaribleIntoTable((len(playerRoundsList)),currentPlayer)
                    modules.start(Button,get_font,modules.play,modules.leaderboard,modules.typing,score,playerRoundsList)



        score_heading=get_font(60).render("Your scores:", True,"#703be3")
        score_h_rect=score_heading.get_rect(center=(640,130))
        score_screen.blit(score_heading,score_h_rect)
        name_text=get_font(40).render(("Player Name: "+str(currentPlayer.playerName)),True,"black")
        wpm_text=get_font(40).render(("WPM: "+str(currentPlayer.wpm)),True,"black")
        accuracy_text=get_font(40).render(("Accuracy: "+str(currentPlayer.accuracyPercent)+"%"),True,"black")
        score_screen.blit(name_text,pygame.Rect((350,230,600,400)))
        score_screen.blit(wpm_text,pygame.Rect((350,300,600,400)))
        score_screen.blit(accuracy_text,pygame.Rect((350,370,600,400)))
        quit_text=get_font(50).render("QUIT",True,"#703be3")
        quit_button=Button(290,520,300,100,"#f8f5ff","#f8f5ff",False)
        quit_rect=quit_button.GetRect()
        quit_button.DrawRect(score_screen,quit_rect)
        score_screen.blit(quit_text,(quit_button.x+78,quit_button.y+25))
        restart_text=get_font(50).render("RESTART",True,"#703be3")
        restart_button=Button(690,520,300,100,"#f8f5ff","#f8f5ff",False)
        restart_rect=restart_button.GetRect()
        restart_button.DrawRect(score_screen,restart_rect)
        score_screen.blit(restart_text,(restart_button.x+35,restart_button.y+25))


        pygame.display.update()
    clock.tick(60)