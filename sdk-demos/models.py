import os
import asyncio
from lumino.sdk import LuminoSDK


async def main():
    async with LuminoSDK(os.environ.get("LUMINO_API_KEY")) as client:
        models = await client.model.list_base_models()
        print(models)

asyncio.run(main())