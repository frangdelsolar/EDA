import json
import websockets
import time
import os
from random import randint
from game_state import GameState


class ConnectionManager:
    def __init__(self):
        self.websocket = None

    async def start(self, auth_token):
        uri = "wss://4yyity02md.execute-api.us-east-1.amazonaws.com/ws?token={}".format(auth_token)
        while True:
            try:
                print('connection to {}'.format(uri))
                async with websockets.connect(uri) as websocket:
                    self.websocket = websocket
                    await self.play()
            
            except KeyboardInterrupt:
                print('Exiting...')
                break
            
            except Exception:
                print('connection error!')
                time.sleep(3)

    
    async def play(self):
        while True:
            try:
                request = await self.websocket.recv()
                # os.system('CLS')
                print(f"< {request} >")
                request_data = json.loads(request)
                
                if request_data['event'] == 'update_user_list':
                    pass

                if request_data['event'] == 'game_over':
                    await self.process_game_over(request_data)

                if request_data['event'] == 'challenge':
                    # if request_data['data']['opponent'] == 'frangdelsolar@gmail.com':
                    await self.process_challenge(request_data)

                if request_data['event'] == 'your_turn':
                    await self.process_your_turn(request_data)

            except KeyboardInterrupt:
                print('Exiting...')
                break

            except Exception as e:
                print('error {}'.format(str(e)))
                break 


    async def process_game_over(self, request_data):
        request_data['algorithm'] = 'minimax_no_bfs'
        print('Processing game over')
        with open('logs/game_over.txt', 'a') as file:
            file.write(json.dumps(request_data) + '\n')
            file.close()


    async def process_challenge(self, request_data):
        await self.send(
            'accept_challenge',
            {
                'challenge_id': request_data['data']['challenge_id'],
            },
        )


    async def process_your_turn(self, request_data):
        ''' Decides to play a move or a wall according to Game State '''
        game = GameState(request_data['data'])
        game.show()

        action = None
        result = None
        if game.walls > 0:
        # if randint(0, 10) > 4:
            action, result = self.process_wall(game)

        if not result:
            action, result = self.process_move(game)
            if not result:
                action, result = self.process_wall(game)

        await self.send(action, result)

    def process_move(self, game):
        ''' Gets the best possible move and sends it to the socket '''
        # move = game.move_minimax(1)
        move = game.move_shortest()
        return ('move', move)


    def process_wall(self, game):
        wall = game.new_wall()
        return ('wall', wall)

    async def send(self, action, data):
        message = json.dumps(
            {
                'action': action,
                'data': data,
            }
        )
        print(message)
        await self.websocket.send(message)