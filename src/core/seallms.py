# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("SeaLLMs/SeaLLMs-v3-7B-Chat")
model = AutoModelForCausalLM.from_pretrained("SeaLLMs/SeaLLMs-v3-7B-Chat")



# Use a pipeline as a high-level helper
# from transformers import pipeline

# pipe = pipeline("text-generation", model="SeaLLMs/SeaLLMs-v3-7B-Chat")
# messages = [
#     {"role": "user", "content": "Who are you?"},
# ]
# pipe(messages)