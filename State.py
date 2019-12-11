from gpiozero import LED, MotionSensor
import gpiozero
import RPi.GPIO as GPIO
from time import sleep
from signal import pause
from aiohttp import web
import socketio
import asyncio
import signal
from Game import Game

import sys

class State:
    def __init__(self):
        self.game = Game("Sean", "Lauren", "Murderface", "Mitch")

    def redGoal(self):
       self.game.goal("red")
       red.on()

    def resetGame(self, game):
        #TODO: turn these into Players
        print("here")
        self.game = Game( "Sean", "Lauren", "Murderface", "Mitch")


redPIR = gpiozero.MotionSensor(4)
red = LED(18)

sio = socketio.AsyncServer(cors_allowed_origins='*', async_handlers=False)
app = web.Application()
sio.attach(app)

redPIR.when_motion = red.on
sio.emit
async def startMsg():
    await sio.emit('game start', 'game started')


async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html', headers={ 'Access-Control-Allow-Origin': 'http://localhost:3000/'})

@sio.event
async def connect(sid, environ):
    await sio.emit('sup', {'response': 'donk'})
    print('connect ', sid)

@sio.on('goal')
async def print_message(sid, message):
    await sio.emit('sup', {'response': 'weeoo'})
    print("Socket ID: " , sid)
    print(message)

@sio.on('start game')
async def startGame(g, players):
    print('start game event', players)
    game = Game(players['red_def'], players['red_off'], players['black_def'], players['black_off'], sio)
    
   # await sio.emit('start game', 'game started')
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    
    redPIR.when_motion = game.redgoal
    
app.router.add_get('/', index)

# We kick off our server
if __name__ == '__main__':
    web.run_app(app)
    
