import streamlit as st
from flask import Flask, send_file
from threading import Thread
import time

# File path for the raw text file
RAW_TEXT_FILE = "state.txt"

# Flask app for serving raw text
flask_app = Flask(__name__)

@flask_app.route("/rawtext")
def rawtext():
    """Serve the raw text file."""
    return send_file(RAW_TEXT_FILE, mimetype="text/plain")

def start_flask():
    """Run the Flask app."""
    flask_app.run(host="0.0.0.0", port=5000)

# Streamlit app
st.title("Streamlit with Raw Text Page")

if st.button("Press Me"):
    # Update text file to "true"
    with open(RAW_TEXT_FILE, "w") as file:
        file.write("true")
    st.success("Text updated to 'true'. It will revert to 'false' in 3 seconds.")
    time.sleep(3)
    # Revert to "false"
    with open(RAW_TEXT_FILE, "w") as file:
        file.write("false")

st.write("The raw text file is accessible at [Raw Text Page](http://localhost:5000/rawtext).")

# Start Flask in a separate thread
Thread(target=start_flask, daemon=True).start()
