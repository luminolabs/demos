import os
import asyncio
from lumino.sdk import LuminoSDK

async def main():
    async with LuminoSDK(os.environ.get("LUMINO_API_KEY")) as client:
        job_details = await client.fine_tuning.get_fine_tuning_job("industrial-finetune")
        print(job_details)

asyncio.run(main())