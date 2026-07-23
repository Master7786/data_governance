import streamlit as st
import requests
import os

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

workspace_host = "https://dbc-8fff8432-25ee.cloud.databricks.com"

response = requests.post(
    f"{workspace_host}/oidc/v1/token",
    auth=(client_id, client_secret),
    data={
        "grant_type": "client_credentials",
        "scope": "all-apis",
    },
)

print(response.status_code)
print(response.text)

st.set_page_config(page_title="Sample DAB App")

st.title("Databricks Apps")

st.write("Hello World!")
