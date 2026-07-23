import streamlit as st

import os

client_id = os.environ.get("client-id")
client_secret = os.environ.get("client-secret")

print(f"Loaded Client ID: {client_id}")

st.set_page_config(page_title="Sample DAB App")

st.title("Databricks Apps")

st.write("Hello World!")
