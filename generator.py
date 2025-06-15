from transformers import pipeline

generator = pipeline("text-generation", model="replit/replit-code-v1-3b")

def generate_code(prompt: str) -> str:
    output = generator(f"Write HTML code for:\n{prompt}", max_new_tokens=256)[0]["generated_text"]
    return output
