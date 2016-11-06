import time
import asyncio
import signal
import sys


from post_writer import insert_post


async def get_status(res):
    while True:
        if res.ready():
            return res.status
        else:
            await asyncio.sleep(1)


async def insert(text):
    r = insert_post.delay(text)
    print('[{}] push to queue'.format(r.id))
    status = await get_status(r)
    print('[{}] task status: {}'.format(r.id, status))
    return status


def signal_handler(signal, frame): 
    loop.stop()
    sys.exit(0)


loop = asyncio.get_event_loop() 

texts = ['zgg1', 'zgg2', 'zgg3', 'zgg4', 'zgg5']

for t in texts:
    asyncio.ensure_future(insert(t)) 

# tasks = [insert(t) for t in texts]

signal.signal(signal.SIGINT, signal_handler)
loop.run_forever()