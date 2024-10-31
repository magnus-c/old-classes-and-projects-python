#using async
'''
To run a function on a thread, put the function in a Future:

    futureFunc = Future( longRunningFunction, arg1, arg2 ...)

The thread will start running in idle-mode until the result of your 
function is needed. The result is acquired by calling the Future 
like a function:

    print( futureFunc( ... ) )

If the futureFunc has completed executing, the call returns the results. 
If it is still running, then the call blocks until the futureFunc completes. 
The result of the function is stored in the Future, so subsequent calls 
to it return immediately.
'''

import asyncio
import random

async def producer(cookiejar, n):
    for x in range(1, n + 1):
        print('marge {}/{}'.format(x, n))
        print("<<marge waiting>>")
        await asyncio.sleep(random.random())
        print(">>marge put<<")
        item = str(x)
        print("$marge "+item)
        await cookiejar.put(item)
    await cookiejar.put(None)

async def consumer(cookiejar):
    while True:
        print("<<homer waiting>>")
        item = await cookiejar.get()
        print(">>homer get<<")
        if item is None:
            break
        print('@homer {}...'.format(item))
        await asyncio.sleep(random.random())

eventloop = asyncio.get_event_loop()
cookiejar = asyncio.Queue()
for i in range(10):
    marge = producer(cookiejar, i)
    homer = consumer(cookiejar)
eventloop.run_until_complete(asyncio.gather(marge, homer))
eventloop.run_until_complete
eventloop.close()