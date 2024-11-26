import streamlit as st
import time
from github import Github

# Load the GitHub token from secrets
GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]
REPO_NAME = "Isaiahensley/pico-gate-opener"  # Replace with your repo name

def update_state_file(content):
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)
    contents = repo.get_contents("state.txt", ref="main")  # Adjust branch if necessary

    # Update the file
    repo.update_file(contents.path, "Update state.txt via Streamlit app", content, contents.sha, branch="main")

st.title("State Changer")

# Style the button to be large
button_style = """
    <style>
    .stButton button {
        height: 100px;
        width: 100%;
        font-size: 24px;
    }
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)

if st.button("Open Gate"):
    # Set state.txt to "true"
    update_state_file("true")
    st.write("State is now true")
    # Wait for 3 seconds
    time.sleep(3)
    # Set state.txt back to "false"
    update_state_file("false")
    st.write("State is now false")
