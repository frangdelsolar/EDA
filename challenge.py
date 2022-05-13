from random import randint
from game_state import GameState


class Challenge:
    def __init__(self, id):
        self.id = id

    def __repr__(self) -> str:
        return f'Challenge {self.id}'

    async def process_move(self, request_data, connection):
        game = GameState(request_data['data'])
        # move = game.move()

        # {
        #     "event": "your_turn",
        #     "data": {
        #         "player_2": "uno",
        #         "player_1": "dos",
        #         "score_2": 0.0,
        #         "walls": 10.0,
        #         "score_1": 0.0,
        #         "side": "N",
        #         "remaining_moves": 50.0,
        #         "board": "  N     N     N                                                                                                                                                                                                                                                                   S     S     S  ",
        #         "turn_token": "087920d0-0e6b-4716-9e77-add550a006aa",
        #         "game_id": "ab16e71c-caeb-11eb-975e-0242c0a80004"
        #     }
        # }

        # move = {
            #     'game_id': request_data['data']['game_id'],
            #     'turn_token': request_data['data']['turn_token'],
            #     'from_row': from_row,
            #     'from_col': from_col,
            #     'to_row': to_row,
            #     'to_col': to_col,
            # }

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