import streamlit as st
from explainer import explain_code

st.title("AI-Powered Code Explainer")

# Text area for user to paste code
code_input = st.text_area("Paste your code here:", height=200)

# Add a selectbox for explanation style
style = st.selectbox(
    "Select explanation style:",
    ["Brief", "Detailed", "Step-by-Step"],
    index=0
)

# Button to get explanation
if st.button("Explain Code"):
    if code_input.strip():
        explanation = explain_code(code_input, style)
        st.markdown("### 📝 Explanation")
        st.write(explanation)
    else:
        st.warning("⚠️ Please paste some code first.")
