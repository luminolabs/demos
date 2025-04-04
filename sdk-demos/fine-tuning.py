import os
import asyncio
from lumino.sdk import LuminoSDK
from lumino.models import (
    FineTuningJobCreate,FineTuningJobParameters
)

async def main():
    async with LuminoSDK(os.environ.get("LUMINO_API_KEY")) as client:
        job = await client.fine_tuning.create_fine_tuning_job(FineTuningJobCreate(
            base_model_name="llm_llama3_1_8b",
            dataset_name="encyclopedia-dataset",
            name="encyclopedia-demo-decen",
            type="LORA",
            parameters=FineTuningJobParameters(
                batch_size=2,
                shuffle=True,
                num_epochs=1,
                lr=0.1,
                seed=42
            ),
            provider="LUM"
        ))

        print(job)

        # jobs = await client.fine_tuning.list_fine_tuning_jobs()
        # print(jobs)
        #
        # job_details = await client.fine_tuning.get_fine_tuning_job(job.name)
        # print(job_details)

asyncio.run(main())