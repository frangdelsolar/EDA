import json
import websockets
import time
from random import randint
from challenge import Challenge


class ConnectionManager:
    def __init__(self):
        self.challenges = []
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
                print(f"< {request} >")
                request_data = json.loads(request)
                
                if request_data['event'] == 'update_user_list':
                    pass

                if request_data['event'] == 'game_over':
                    await self.process_game_over(request_data)

                if request_data['event'] == 'challenge':
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
        print('Processing game over')
        with open('logs/game_over.txt', 'a') as file:
            file.write(json.dumps(request_data))
            file.close()


    async def process_challenge(self, request_data):
        await self.send(
            'accept_challenge',
            {
                'challenge_id': request_data['data']['challenge_id'],
            },
        )

        self.append_challenge(request_data['data']['challenge_id'])


    async def process_your_turn(self, request_data):
        challenge = self.get_or_create_challenge(request_data['data']['game_id'])
        if randint(0, 10) > 3:
            await challenge.process_move(request_data, self)
        else:
            await challenge.process_wall(request_data, self)


    async def send(self, action, data):
        message = json.dumps(
            {
                'action': action,
                'data': data,
            }
        )
        print(message)
        await self.websocket.send(message)


    def append_challenge(self, challenge_id):
        challenge = Challenge(challenge_id)
        self.challenges.append(challenge)
        return challenge


    def get_or_create_challenge(self, challenge_id):
        for challenge in self.challenges:
            if challenge.id == challenge_id:
                return challenge

        return self.append_challenge(challenge_id)


