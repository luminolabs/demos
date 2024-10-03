import os
import asyncio
from lumino.sdk import LuminoSDK
from lumino.models import DatasetCreate


async def main():
    async with LuminoSDK(os.environ.get("LUMINO_API_KEY")) as client:
        files = await client.dataset.list_datasets()
        await client.dataset.upload_dataset("formatted-encyclopedia.jsonl", DatasetCreate(name="encyclopedia-dataset", description="encyclopedia dataset"))

        print(files)

asyncio.run(main())