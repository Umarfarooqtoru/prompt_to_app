from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

MODEL_ID = "bigcode/starcoder2-7b"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID, trust_remote_code=True, device_map="auto"
)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_code(prompt: str) -> str:
    full_prompt = (
        "You are a helpful assistant generating full web app code. "
        f"User request:\n{prompt}\n\nProvide complete code (HTML/CSS/JS or React):\n"
    )
    out = generator(full_prompt, max_new_tokens=512, temperature=0.2)[0]["generated_text"]
    return out.split("Provide complete code")[-1].strip()