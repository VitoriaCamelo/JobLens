import streamlit as st

st.set_page_config(
  page_title="Minha conta",
  page_icon="😃",
)

st.write("# Minha conta")

st.markdown(
  """
  ### Informações da conta
  Nome:
  Streamlit is an open-source app framework built specifically for
  Machine Learning and Data Science projects.
  **👈 Select a demo from the sidebar** to see some examples
  of what Streamlit can do!
  ### Lista de habilidades
  - Check out [streamlit.io](https://streamlit.io)
  - Jump into our [documentation](https://docs.streamlit.io)
  - Ask a question in our [community
      forums](https://discuss.streamlit.io)
"""
)
