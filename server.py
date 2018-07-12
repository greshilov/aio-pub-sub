import os
import logging

from aiohttp import web, WSMsgType
from settings import PORT, REGISTER_REGEXP, HOST, ROOT, PB_DEBUG

logger = logging.getLogger('aio-pub-sub')


async def transfer(request):
    client_id = request.match_info.get('id')
    if client_id in request.app.clients:
        data = await request.read()
        ws = request.app.clients[client_id]
        if request.content_type == 'application/octet-stream':
            await ws.send_bytes(data)
        else:
            await ws.send_str(str(data, 'utf-8', errors='ignore'))
        raise web.HTTPOk
    raise web.HTTPNotFound


async def web_socket_subscriber(request):
    ws = web.WebSocketResponse()
    client_id = None
    await ws.prepare(request)
    async for msg in ws:
        if msg.type == WSMsgType.TEXT:
            if '$register' in msg.data:
                match = REGISTER_REGEXP.match(msg.data)
                if match:
                    client_id = match.group(1)
                    request.app.clients[client_id] = ws
                    logger.debug('Registered user with id: {}'.format(client_id))
        elif msg.type == WSMsgType.ERROR:
            logger.error(ws.exception())

    logger.debug('Client id {} connection closed'.format(client_id))
    if client_id is not None and client_id in app.clients:
        del app.clients[client_id]

    return ws


if __name__ == '__main__':
    app = web.Application()
    # TODO: Use redis?
    app.clients = dict()
    app.add_routes([web.get('/ws', web_socket_subscriber),
                    web.post(r'/client/{id:[0-9A-z]{8}}', transfer)])
    if PB_DEBUG:
        logging.basicConfig(level=logging.DEBUG)
        app.router.add_static('/', os.path.join(ROOT, 'static'))

    web.run_app(app, host=HOST, port=PORT)
