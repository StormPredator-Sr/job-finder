# Import the query helpers
from google import google_query
from indeed import indeed_query
from naukri import naukri_query

# To measure time
import time

# Performing asynchronously
import asyncio

# Import the chrome driver which is a headless browser
from driver import driver

# For pretty printing
import json

async def main():
    keyword = input()
    
    # create tasks to run the queries in the background
    tasks = [
        asyncio.create_task(google_query(driver, keyword)),
        asyncio.create_task(indeed_query(driver, keyword)),
        asyncio.create_task(naukri_query(driver, keyword))
    ]
    
    # wait for all tasks to complete and get their results as a list
    results = await asyncio.gather(*tasks)

    jobs = []

    for result in results:
        jobs.extend(result)

    print(json.dumps(jobs,indent=4))

start = time.time()
asyncio.run(main())
end = time.time()

print(f"Time taken to crawl is: {end - start}")