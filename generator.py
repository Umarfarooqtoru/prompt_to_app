from transformers import pipeline

generator = pipeline("text-generation", model="replit/replit-code-v1-3b")

def generate_code(prompt: str) -> str:
    full_prompt = f"Write a simple HTML page for this request:\n{prompt}\nCode:\n"
    output = generator(full_prompt, max_new_tokens=256, temperature=0.2)[0]["generated_text"]
    return output
