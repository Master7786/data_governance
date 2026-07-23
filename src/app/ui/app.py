import streamlit as st
import requests
import os

client_id = os.environ.get("clientid")
client_secret = os.environ.get("secret")

workspace_host = "https://dbc-8fff8432-25ee.cloud.databricks.com"

response = requests.post(
    f"{workspace_host}/oidc/v1/token",
    data={
        "grant_type": "client_credentials",
        "scope": "all-apis",
    },
    auth=(client_id, client_secret),
)

print(response.status_code)
print(response.text)

print(f"Loaded Client ID: {client_id}")

st.set_page_config(page_title="Sample DAB App")

st.title("Databricks Apps")

st.write("Hello World!")
