import streamlit as st
import readme_generator as rg

st.title("README Generator")
uploaded_file = st.file_uploader("Upload File")
if uploaded_file is not None:
    content = uploaded_file.read().decode()
    response = rg.ask(f"{content}\n\nRead the above code and generate a README.md for it in markdown format.")
    st.markdown("""---""")
    st.subheader("Response")
    st.text(response)
    st.markdown("""---""")
    st.subheader("Preview")
    st.markdown(response)
    