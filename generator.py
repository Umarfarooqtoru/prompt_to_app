from transformers import pipeline

# Use a lightweight, fast code model
generator = pipeline("text-generation", model="replit/replit-code-v1-3b")

def generate_code(prompt: str) -> str:
    system_prompt = (
        "You are an expert frontend developer.\n"
        "Generate a complete HTML page with inline CSS and basic JavaScript if needed.\n"
        f"Task: {prompt}\n"
        "Return ONLY the HTML code without explanation.\n"
    )
    result = generator(system_prompt, max_new_tokens=512, temperature=0.2)[0]['generated_text']
    
    # Extract from first <html> if present
    if "<html" in result:
        result = result[result.find("<html"):]

    return result.strip()
