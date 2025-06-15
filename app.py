import streamlit as st
from generator import generate_code
from pathlib import Path

st.set_page_config(page_title="Prompt-to-App Generator", layout="wide")
st.title("🛠️ Prompt-to-App Generator")

prompt = st.text_area("🔧 Describe your app or component", height=150)

if st.button("Generate App"):
    if not prompt.strip():
        st.warning("⚠️ Please enter a prompt before generating.")
    else:
        with st.spinner("Generating code..."):
            code = generate_code(prompt)

        if not code or "<html" not in code:
            st.error("❌ No valid HTML generated. Try a different prompt.")
        else:
            st.success("✅ Code generated!")
            st.code(code, language="html")

            # Save to file
            out_dir = Path("output")
            out_dir.mkdir(exist_ok=True)
            file = out_dir / "generated_app.html"
            file.write_text(code)

            # Live preview
            st.markdown("### 👇 Live Preview")
            st.components.v1.html(code, height=500, scrolling=True)
