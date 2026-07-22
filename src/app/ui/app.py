import streamlit as st

import os

client_id = os.environ.get("MY_CLIENT_ID")
client_secret = os.environ.get("MY_CLIENT_SECRET")

print(f"Loaded Client ID: {client_id}")

st.set_page_config(page_title="Sample DAB App")

st.title("Databricks Apps")

st.write("Hello World!")
