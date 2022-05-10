from random import randint
from game_state import GameState


class Challenge:
    def __init__(self, id):
        self.id = id
        self.game = GameState()


    async def process_move(self, request_data, connection):
        self.game.update(request_data['data'])
        self.game.show()
        move = self.game.move()

        if move:
            move['game_id'] = self.id
            move['turn_token'] = request_data['data']['turn_token']
            await connection.send('move', move)

        else:
            await self.process_wall(request_data, connection)


    async def process_wall(self, request_data, connection):
        # self.game.update(request_data['data'])
        self.game.show()
        await connection.send(
            'wall',
            {
                'game_id': request_data['data']['game_id'],
                'turn_token': request_data['data']['turn_token'],
                'row': randint(0, 8),
                'col': randint(0, 8),
                'orientation': 'h' if randint(0, 1) == 0 else 'v'
            },
        )