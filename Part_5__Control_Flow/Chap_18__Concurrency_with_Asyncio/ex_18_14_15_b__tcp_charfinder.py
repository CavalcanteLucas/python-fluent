# reference: https://github.com/fluentpython/example-code-2e/blob/aeee41988eb733a0e1423eec153c839c3840ba6b/18b-async-await/charfinder/tcp_charfinder.py

import asyncio
import sys
from urllib.parse import urlparse, parse_qs

from ex_A__charfinder import UnicodeNameIndex

CRLF = b'\r\n'
PROMPT = b'?>'

index = UnicodeNameIndex()


async def handle_queries(reader, writer):
    writer.write(PROMPT)  # can't yield from!
    await writer.drain()  # must yield from!
    data = await reader.readline()

    try:
        decoded_data = data.decode().strip()[:-9]  # remove trailing HTTP/1.1
        parsed_data = urlparse(decoded_data)
        query_items = parse_qs(parsed_data.query)
        query = ['{}'.format(item) for item in query_items['query']][0]
    except UnicodeDecodeError:
        query = '\x00'
    client = writer.get_extra_info('peername')
    print('Received from {}: {!r}'.format(client, query))
    if query:
        # if ord(query[:1]) < 32:
        #     break
        lines = list(index.find_description_strs(query))
        if lines:
            writer.writelines(line.encode() + CRLF for line in lines)
        writer.write(index.status(query, len(lines)).encode() + CRLF)

        await writer.drain()
        print('Sent {} results'.format(len(lines)))

    print('Close the client socket')
    writer.close()


async def main(address='127.0.0.1', port=2323):
    port = int(port)

    server = await asyncio.start_server(handle_queries, address, port)

    host = server.sockets[0].getsockname()
    print('Serving on {}. Hit CTRL-C to stop.'.format(host))

    async with server:
        await server.serve_forever()

    print('Server shutting down.')
    server.close()


if __name__ == '__main__':
    asyncio.run(main(*sys.argv[1:]))
