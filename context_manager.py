# import asyncio

# async def gen_all_users(
#     db: asyncpg.pool.Pool
# ) -> AysncIterator[asyncpg.Record]:
#     async with dn.acquire() as conn:
#         async with conn.transaction():
#             async with conn.transaction():
#                 async for record in conn.cursor('SELECT * FROM ia5_users'):
#                     yield record

# async def entrypoint() -> None:
#     async with asyncpg.create_pool(
#         'localhost'
#     ) as db:
#         async for record in gen_all_users(db):
#             print(record)
#             if record['name'] == 'steve':
#                 break

import asyncio
import aiomysql

loop = asyncio.get_event_loop()


async def test_example():
    conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                       user='root', password='fear1234', db='mysql',
                                       loop=loop)

    cur = await conn.cursor()
    await cur.execute("SELECT * FROM test.users")
    # print(cur.description)
    r = await cur.fetchall()
    print(r)
    await cur.close()
    conn.close()
