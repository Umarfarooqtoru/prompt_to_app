import streamlit as st
from generator import generate_code
from pathlib import Path

st.set_page_config(page_title="Prompt-to-App Generator", layout="wide")
st.title("🛠️ Prompt-to-App Generator")

prompt = st.text_area("🔧 Describe your app or component (e.g., contact form)", height=150)

if st.button("Generate App"):
    with st.spinner("Generating code..."):
        code = generate_code(prompt)
    st.success("✅ Code generated!")
    st.code(code, language="html")

    out_dir = Path("output")
    out_dir.mkdir(exist_ok=True)
    file = out_dir / "generated_app.html"
    file.write_text(code)
    st.markdown(f"🔗 [Download or open the generated app]({file})", unsafe_allow_html=True)