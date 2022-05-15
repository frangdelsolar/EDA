from random import randint
from game_state import GameState


class Challenge:
    def __init__(self, id):
        self.id = id

    def __repr__(self) -> str:
        return f'Challenge {self.id}'

    async def process_move(self, request_data, connection):
        game = GameState(request_data['data'])
        # move = game.move_shortest()
        game.show()
        move = game.move_minimax(1)

        if move:
            await connection.send('move', move)

        else:
            await self.process_wall(request_data, connection)


    async def process_wall(self, request_data, connection):

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