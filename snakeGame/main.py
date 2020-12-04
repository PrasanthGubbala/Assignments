import tkinter
import constants
import game
import sqlite3 as sql

if __name__ == "__main__":
  
    root = tkinter.Tk()
    root.title("Snake Game")

    game = game.Master(root)
    game.grid(column=1, row=0, rowspan=3)

    root.bind("<Key>", game.redirect)

    buttons = tkinter.Frame(root, width=35, height=3 * constants.layout["size"] / 5)

    tkinter.Button(buttons, text='Start', command=game.start).grid()
    tkinter.Button(buttons, text='Stop', command=game.clean).grid()
    tkinter.Button(buttons, text='Quit', command=root.destroy).grid()
    tkinter.Button(buttons, text='Pause', command=game.pause).grid()
    tkinter.Button(buttons, text='Play', command=game.play).grid()

    buttons.grid(column=0, row=0)

    scoreboard = tkinter.Frame(root, width=35, height=2 * constants.layout["size"] / 5)

    tkinter.Label(scoreboard, text='Game Score').grid()
    tkinter.Label(scoreboard, textvariable=game.score.counter).grid()
    tkinter.Label(scoreboard, text='High Score').grid()
    tkinter.Label(scoreboard, textvariable=game.score.maximum).grid()
    tkinter.Label(scoreboard, text='Leader Board').grid()
    tkinter.Label(scoreboard, textvariable=game.score.leaderBoard).grid()

    scoreboard.grid(column=0, row=2)

    root.mainloop()
