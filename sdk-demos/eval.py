from transformers import AutoModelForCausalLM, AutoTokenizer
import json

# Load your fine-tuned model and tokenizer (replace with your model path or Hugging Face hub path)
model_path = "path_to_your_finetuned_model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

# Function to generate predictions from the model
def generate_answer(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs['input_ids'], max_length=50)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Load the evaluation dataset
with open("EvalTrivia.jsonl", "r", encoding="utf-8") as f:
    eval_data = [json.loads(line) for line in f]

correct_predictions = 0
total_predictions = len(eval_data)

# Evaluate the model
for example in eval_data:
    predicted_answer = generate_answer(example["instruction"]).strip()
    if predicted_answer == example["output"].strip():
        correct_predictions += 1
    else:
        print(f"Incorrect prediction:\nQuestion: {example['instruction']}\nExpected: {example['output']}\nGot: {predicted_answer}\n")

# Calculate accuracy
accuracy = (correct_predictions / total_predictions) * 100
print(f"Evaluation Complete. Accuracy: {accuracy:.2f}%")