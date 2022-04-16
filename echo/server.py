import asyncio
from echo import EchoBase, EchoRequest, EchoResponse, EchoStreamResponse
from grpclib.server import Server
from typing import AsyncIterator


class EchoService(EchoBase):
    async def echo(self, echo_request: "EchoRequest") -> "EchoResponse":
        return EchoResponse([echo_request.value for _ in range(echo_request.extra_times)])

    async def echo_stream(self, echo_request: "EchoRequest") -> AsyncIterator["EchoStreamResponse"]:
        for _ in range(echo_request.extra_times):
            yield EchoStreamResponse(echo_request.value)


async def main():
    server = Server([EchoService()])
    await server.start("127.0.0.1", 50051)
    await server.wait_closed()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())