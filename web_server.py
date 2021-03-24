from aiohttp import web
import asyncio
import aiohttp
app = web.Application()

async def hello(request):
    print(request.headers)
    return web.Response(text='Hello Kefir!', content_type='text/plain')

app.add_routes([web.get('/{tail:.*}', hello)])
web.run_app(app)