from rss_gen import channel_to_rss
import asyncio
import sys


async def cli_main():
    print(await channel_to_rss(sys.argv[1]))

if __name__ == "__main__":
    asyncio.run(cli_main())