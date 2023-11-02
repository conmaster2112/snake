import app.ConAPI as ConAPI

Color = ConAPI.Color
base = Color(200,150,100)


def onStart():
    print("Start")
    
def onQuit():
    print("Exit")

def onKeyDown(key):
    if (key == ConAPI.ARROW_LEFT): 
        base.r-=30
    elif(key == ConAPI.ARROW_RIGHT): 
        base.r+=40
def onTick():
    pass
    

game = ConAPI.Game((600,400))


game.screen.setBackgroundColor(base)
game.events.onStart.subscribe(onStart)
game.events.onExit.subscribe(onQuit)
game.events.onKeyDown.subscribe(onKeyDown)
game.Start()