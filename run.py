from app import channel_to_rss
import asyncio
import sys

async def cli_main():
    if len(sys.argv) != 2:
        print("Missing arguements")
        sys.exit(1)
    
    try:
        rss_feed = await channel_to_rss(sys.argv[1])
        print(rss_feed)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(cli_main())