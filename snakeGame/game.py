import collections
import tkinter
import random
import constants
import shapes
import utils
import sqlite3 as sql
import pygame


class Master(tkinter.Canvas):
    """create the game canvas, the snake, the obstacle, keep track of the score"""
    def __init__(self, boss):
        super().__init__(boss)
        self.configure(
            width=constants.layout["size"],
            height=constants.layout["size"],
            bg=constants.layout["background_color"],
        )
        self.running = False
        self.score = Scores(boss)

    def start(self):
        """start snake game"""
        if not self.running:
            self.snake = Snake(self)
            self.obstacle = shapes.Obstacle(self)
            self.mover = Movement(self, random.choice(list(constants.direction_vectors.values())))
            self.running = True

    def clean(self):
        """restarting the game"""
        if self.running:
            self.score.reset()
            self.mover.stop()
            self.obstacle.delete()
            for block in self.snake.blocks:
                block.delete()
            self.running = False

    def redirect(self, event):
        """taking keyboard inputs and moving the snake accordingly"""
        if self.running and event.keysym in constants.direction_vectors:
            vector = constants.direction_vectors[event.keysym]
            if not utils.same_axis(self.mover.vector, vector):
                self.mover.stop()
                self.mover = Movement(self, vector)

    def pause(self):
        """start snake game"""
        self.running = False

    def play(self):
        """start snake game"""
        if not self.running:
            # self.snake = Snake(self)
            # self.obstacle = shapes.Obstacle(self)
            # self.mover = Movement(self, random.choice(list(constants.direction_vectors.values())))
            self.mover = Movement(self, random.choice(list(constants.direction_vectors.values())))
            self.running = True

scr = []
class Scores:
    """Objects that keep track of the score and high score"""
    def __init__(self, master=None):
        self.counter = tkinter.StringVar(master, "0")
        self.maximum = tkinter.StringVar(master, "0")
        self.leaderBoard = tkinter.StringVar(master, "0")

    def increment(self):
        conn = sql.connect('leaderBoard.db')
        cors = conn.cursor()
        cors.execute('select * from leader_board')
        res = cors.fetchall()
        m = []
        for x in res:
            m.append(x[0])
        conn.close()
        m.sort(reverse=True)
        self.leaderBoard.set(str(m[0]))

        score = int(self.counter.get()) + 1
        maximum = max(score, int(self.maximum.get()))
        leaderBoard = int(self.leaderBoard.get())

        self.counter.set(str(score))
        self.maximum.set(str(maximum))

        conn = sql.connect('leaderBoard.db')
        cors = conn.cursor()
        cors.execute("insert into leader_board values(?)",(maximum,))
        conn.commit()
        conn.close()

    def reset(self):
        self.counter.set("0")


class Snake:
    def __init__(self, master):
        self.master = master
        x, y = utils.random_coordinates()
        self.blocks = collections.deque([shapes.Block(master, x, y)])
        self.block_coords = set([(x, y)])

    def move(self, vx, vy):
        """an elementary step consisting of putting the tail of the snake in the first position"""
        head = self.blocks[-1]
        x = (head.x + constants.step_len * vx) % constants.layout["size"]
        y = (head.y + constants.step_len * vy) % constants.layout["size"]
        if x == self.master.obstacle.x and y == self.master.obstacle.y:
            # found the food
            self.master.score.increment()
            self.master.obstacle.delete()
            self.blocks.append(shapes.Block(self.master, x, y))
            self.block_coords.add((x, y))
            self.master.obstacle = shapes.Obstacle(self.master)
        elif (x, y) in self.block_coords:
            # hit body part, game over
            self.master.clean()
        else:
            tail = self.blocks.popleft()
            self.block_coords.remove((tail.x, tail.y))
            tail.modify(x, y)
            self.block_coords.add((x, y))
            self.blocks.append(tail)


class Movement:
    """object that enters the snake into a perpetual state of motion in a predefined direction"""
    def __init__(self, master, vector):
        self.flag = True
        self.master = master
        self.vector = vector
        self.begin()

    def begin(self):
        """start the perpetual motion"""
        if self.flag:
            self.master.snake.move(*self.vector)
            self.master.after(constants.refresh_ms, self.begin)

    def stop(self):
        """stop the perpetual movement"""
        self.flag = False


