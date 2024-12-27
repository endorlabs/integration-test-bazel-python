import asyncio

def runAsync(asyncFunc, url):
    asyncio.sleep(1)
    asyncio.run(asyncFunc(url))


if __name__ == "__main__":
    async def test():
        print("Hello World")
    runAsync(test)