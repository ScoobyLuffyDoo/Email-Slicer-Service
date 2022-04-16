import asyncio
import resources

from grpclib.client import Channel


async def main():
    channel = Channel(host ='localhost' Port=50051)
    service = resources.EmailhandlerStub(channel)
    response = await service.email(resources.EmailRequest(email_address ="jc.smal626@gmail.com"))
    print(response)

    channel.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())