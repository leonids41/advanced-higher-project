import modules, sqlite3

#main
import pygame
pygame.init()
playerRoundsList=[]
connection=sqlite3.connect("Assets/leaderboard.db")
cursor = connection.cursor()
connection.execute("DROP TABLE IF EXISTS score;")
connection.close()
modules.start(modules.Button,modules.get_font,modules.play,modules.leaderboard, modules.typing,modules.score,playerRoundsList)
pygame.quit