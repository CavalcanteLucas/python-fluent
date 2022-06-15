import sys
import asyncio

# ex_18_18__http_charfinder_home_function
def home(request):
    query = request.GET.get('query', '').strip()
    print('Query: {!r}'.format(query))
    if query:
        descriptions = list(index.find_description(query))
        res = '\n'.join(
            ROW_TPL.format(**vars(descr)) for descr in descriptions
        )
        msg = index.status(query, len(descriptions))
    else:
        descriptions = []
        res = ''
        msg = 'Enter words describing characters.'

    html = template.format(query=query, results=res, message=msg)
    print('Sending {} results'.format(len(descriptions)))
    return web.Response(content_type=CONTENT_TYPE, text=html)


# ex_18_17__http_charfinder_main_and_init_functions
@asyncio.coroutine
def init(loop, address, port):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', home)
    handler = app.make_handler()
    server = yield from loop.create_server(handler, address, port)

    return server.sockets[0].getsockname()


def main(address='127.0.0.1', port=8888):
    port = int(port)
    loop = asyncio.get_event_loop()
    host = loop.run_until_complete(init(loop, address, port))
    print('Serving on {}. Hit CTRL-C to stop.'.format(host))
    try:
        loop.run_forever()
    except KeyboardInterrupt:  # CTRL+C pressed
        pass
    print('Server shutting down.')
    loop.close()


if __name__ == '__main__':
    main(*sys.argv[1:])
