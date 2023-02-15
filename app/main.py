import socket
import asyncio

class EchoServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))

        print('Send: {!r}'.format(b'+PONG\r\n'))
        self.transport.write(b'+PONG\r\n')

async def main():
    print("Logs from your program will appear here!")
    loop = asyncio.get_running_loop()
    server = await loop.create_server(lambda: EchoServerProtocol(), 
        "localhost", 6379, reuse_port=True)
    async with server:
        await server.serve_forever()
    

if __name__ == "__main__":
    asyncio.run(main())
