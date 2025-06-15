import streamlit as st
from generator import generate_code
from pathlib import Path

st.set_page_config(page_title="Prompt-to-App Generator", layout="wide")
st.title("🛠️ Prompt-to-App Generator")

prompt = st.text_area("🔧 Describe your app or component (e.g., login form, contact page)", height=150)

if st.button("Generate App"):
    with st.spinner("Generating code..."):
        code = generate_code(prompt)

    if not code.strip():
        st.warning("⚠️ No code was generated. Try a more specific or simpler prompt.")
    else:
        st.success("✅ Code generated!")
        st.code(code, language="html")

        # Save HTML file
        out_dir = Path("output")
        out_dir.mkdir(exist_ok=True)
        file = out_dir / "generated_app.html"
        file.write_text(code)

        # Show live preview
        st.markdown("### 👇 Live Preview")
        st.components.v1.html(code, height=500, scrolling=True)

        # Download link
        st.markdown(f"🔗 [Download generated HTML](output/generated_app.html)", unsafe_allow_html=True)
