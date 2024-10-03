import json

dataset = [
    {"instruction": "What is the capital of France?", "output": "The capital of France is Paris."},
    {"instruction": "Who wrote the novel '1984'?", "output": "The novel '1984' was written by George Orwell."},
    {"instruction": "What is the speed of light?", "output": "The speed of light is approximately 299,792 kilometers per second."}
]

formatted_data = []
for example in dataset:
    formatted_data.append({
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": example["instruction"]},
            {"role": "assistant", "content": example["output"]}
        ]
    })

with open("formatted-trivia.jsonl", "w", encoding="utf-8") as f:
    for item in formatted_data:
        f.write(json.dumps(item) + "\n")
