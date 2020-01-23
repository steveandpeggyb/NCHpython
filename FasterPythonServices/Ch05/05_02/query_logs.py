"""Using asyncio to query logs"""

from aiohttp import web
import asyncpg
from http import HTTPStatus
from io import StringIO
import csv

pg_pool = None


async def query_handle(request):
    resp = web.StreamResponse(status=HTTPStatus.OK)
    await resp.prepare(request)

    io = StringIO()
    writer = csv.writer(io)

    query = await request.text()

    async with pg_pool.acquire() as conn:
        async with conn.transaction():
            async for row in conn.cursor(query):
                io.truncate(0)
                io.seek(0, 0)
                writer.writerow(row)
                await resp.write(io.getvalue().encode('utf-8'))
                await resp.drain()

    return resp


async def init_pool():
    global pg_pool

    pg_pool = await asyncpg.create_pool(host='localhost', user='postgres')


app = web.Application()
app.router.add_post('/query', query_handle)

if __name__ == '__main__':
    import asyncio

    asyncio.get_event_loop().run_until_complete(init_pool())
    web.run_app(app)
