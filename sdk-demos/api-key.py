import os
import asyncio
from lumino.sdk import LuminoSDK

async def main():
    # Fetch the API key from environment variables and create an SDK client
    async with LuminoSDK(os.environ.get("LUMINO_API_KEY")) as client:
        # Retrieve and print the current user information
        user = await client.user.get_current_user()
        print(user)

# Run the async main function
asyncio.run(main())