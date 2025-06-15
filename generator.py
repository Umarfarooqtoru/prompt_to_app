from transformers import pipeline

generator = pipeline("text-generation", model="replit/replit-code-v1-3b")

def generate_code(prompt: str) -> str:
    base_prompt = f"Write a simple HTML page for: {prompt}\n\nCode:\n"
    result = generator(base_prompt, max_new_tokens=512, temperature=0.2)[0]["generated_text"]
    if "<html" in result:
        result = result[result.find("<html"):]
    return result.strip()
