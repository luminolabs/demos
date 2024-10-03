import os
import asyncio
from lumino.sdk import LuminoSDK

async def main():
    async with LuminoSDK(os.environ.get("LUMINO_API_KEY")) as client:
        jobs = await client.fine_tuning.list_fine_tuning_jobs()
        print(jobs)
        print(f"Listed {len(jobs.data)} fine-tuning jobs")

        # jobs = await client.fine_tuning.list_fine_tuning_jobs()
        # print(jobs)

asyncio.run(main())