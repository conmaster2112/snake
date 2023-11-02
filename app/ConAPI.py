import pygame as pg
import math
import asyncio

pg.init()
ARROW_DOWN = 1073741905
ARROW_UP = 1073741906
ARROW_LEFT = 1073741904
ARROW_RIGHT = 1073741903
class Screen:
    def __init__(self, size):
        self.size = size
        self.screen = pg.display.set_mode(self.size)
        self.color = Color(230,230,230)
        self.fps = 20
    def setBackgroundColor(self,color):
        self.color = color
    def getScreen(self):
        return self.screen
    def setTitle(self, title):
        pg.display.set_caption(title)
    def __tick__(self):
        self.screen.fill(self.color.toNativeColor())
        pg.display.flip()

class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.entities = []
    def addEntity(self, entity):
        self.entities.append(entity)
    def getEntities(self):
        return self.entities
    def flip(self):
        for a in self.entities:
            a.render(self.screen)
class Entity:
    def __init__(self, type):
        self.type = type
        self.location = Vector2()
        self.velocity = Vector2()
    def render(self,screen: Screen):
        pass
class ShapeTypes:
    CYRCLE = "cyrcle"
    RECT = "rectangle"
class BallEntity(Entity):
    def __init__(self,radius,color):
        Entity.__init__(self,ShapeTypes.CYRCLE)
        self.radius = radius
        self.color = color
    def setColor(self, color):
        self.color = color
    def setRadius(self, radius):
        self.radius = radius
    def render(self,screen: Screen):
        pg.draw.cyrcle(screen.getScreen(),self.color,self.location.toList(),self.radius)
class Color:
    def __init__(self,r,g,b):
        self._r = r
        self._g = g
        self._b = b
    def toNativeColor(self):
        return (self._r,self._g,self._b)
    
    @property
    def r(self): 
        return self._r
    @property
    def g(self): 
        return self._g
    @property
    def b(self): 
        return self._b

    @r.setter
    def r(self,v):
        if(v < 0): self._r = 0
        elif(v > 255): self._r = 255
        else: self._r = v    
    @g.setter
    def g(self,v):
        if(v < 0): self._g = 0
        elif(v > 255): self._g = 255
        else: self._g = v
    @b.setter
    def b(self,v):
        if(v < 0): self._b = 0
        elif(v > 255): self._b = 255
        else: self._b = v

class Game:
    def __init__(self):
        self.clock = pg.time.Clock()
        self.screen = Screen((1200,800))
        self.events = Events()
        self.exit = False
        self.events.onExit.subscribe(self.onExit)
    def Start(self):
        self.events.onStart.execute()
        while True:
            self.events.__tick__()
            if(self.exit):
                return
            self.screen.__tick__()
            self.clock.tick(self.screen.fps)
    def onExit(self):
        self.exit = True


class Events:
    def __init__(self):
        self.onExit = Event()
        self.onKeyDown = Event()
        self.onStart = Event()
        self.onTick = Event()
    def __tick__(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.onExit.execute()
            elif event.type == pg.KEYDOWN:
                self.onKeyDown.execute(event.key)
        self.onTick.execute()
class Event:
    def __init__(self):
        self.__methods__ = set()
    def subscribe(self, delegate):
        self.__methods__.add(delegate)
        return delegate
    def unsubscribe(self, delegate):
        self.__methods__.remove(delegate)
        return delegate
    def execute(self,*params):
        for method in self.__methods__:
            method(*params)
        


class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector2()
        else:
            return Vector2(self.x / mag, self.y / mag)
    def dot(self, other) -> float:
        return self.x * other.x + self.y * other.y
    def cross(self, other) -> float:
        return self.x * other.y - self.y * other.x
    def distance_to(self, other) -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    def toList(self)->list:
        return  [self.x,self.y]
    @staticmethod
    def add(v1, v2):
        return Vector2(v1.x + v2.x, v1.y + v2.y)

    @staticmethod
    def subtract(v1, v2):
        return Vector2(v1.x - v2.x, v1.y - v2.y)

    @staticmethod
    def multiply(v1, scalar):
        return Vector2(v1.x * scalar, v1.y * scalar)

    @staticmethod
    def divide(v1, scalar):
        return Vector2(v1.x / scalar, v1.y / scalar)