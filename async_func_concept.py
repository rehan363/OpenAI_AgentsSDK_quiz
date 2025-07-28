import asyncio
import time 
print("i am here")
async def test1():
    print("test1 started")
    # time.sleep(2)
    asyncio.sleep(2)
    print(time.time())
    print("test1 done")
    return "heloo"

async def test2():
    print("test2 started")
    # time.sleep(3)
    await asyncio.sleep(3)
    print("test2 done")
    return "world"

async def main():
    start_time = time.time()
    # await test1()
    # await test2()
    await asyncio.gather(test1(), test2())
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")

if __name__ == "__main__":
    asyncio.run(main())
    # main()
    # print("main done")