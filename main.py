import os
import asyncio
from dotenv import load_dotenv

from connection_manager import ConnectionManager


CONNECTION = ConnectionManager()

if __name__ == '__main__':
    load_dotenv()
    bot = input('1. Official; 2. Pruebas')
    if bot == '1':
        auth_token = os.getenv("OFFICIAL_BOT")
    else:
        auth_token = os.getenv("BOTFGS_TOKEN")

    if auth_token:
        asyncio.get_event_loop().run_until_complete(CONNECTION.start(auth_token))
    else:
        print('please provide your auth_token')