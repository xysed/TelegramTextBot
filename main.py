import asyncio
import logging
import os
from pyrogram.client import Client
from config import BOTS


logging.basicConfig(level=logging.WARN,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)

async def create_client(
    session_name: str, api_id: int, api_hash: str
) -> Client:
    print(f"Initializing {session_name} session")
    client = Client(
        name=session_name,
        api_id=api_id,
        api_hash=api_hash,
        workdir="sessions/"
    )
    await client.start()
    return client


async def bot_worker(bot):
    config = bot[0]
    client: Client = bot[1]

    while True:
        for action in config["actions"]:
            match action["type"]:
                case "chat_message":
                    logger.info(f"{config['session_name']} chat_message")
                    await client.send_message(int(action["chat_id"]), text=action["text"])
                case "sleep":
                    logger.info(f"{config['session_name']} sleep {action['duration']}s")
                    await asyncio.sleep(int(action["duration"]))


async def main():
    if not os.path.exists("sessions"):
        os.makedirs("sessions")

    bots = []

    for bot in BOTS:
        client = await create_client(
            bot["session_name"], bot["API_ID"], bot["API_HASH"]
        )
        bots.append((bot, client))

    await asyncio.gather(*[asyncio.create_task(bot_worker(bot)) for bot in bots])


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Interrupted")
