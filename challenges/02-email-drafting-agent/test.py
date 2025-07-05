import json
import uuid
import requests
from websocket import create_connection
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Load test credentials
username = os.getenv("TEST_LOGIN_USERNAME")
password = os.getenv("TEST_LOGIN_PASSWORD")

if not username or not password:
    raise Exception("Missing TEST_LOGIN_USERNAME or TEST_LOGIN_PASSWORD in .env file.")

# Your ngrok-exposed router frontend URL
#ws_url_base = "wss://5ad5-31-184-80-141.ngrok-free.app/frontend/ws"

# Local development WebSocket URL
ws_url_base = "ws://localhost:8000/frontend/ws"

# Get JWT using the API
try:
    login_url = "http://localhost:8000/api/login/access-token"
    login_data = {
        "grant_type": "password",
        "username": username,
        "password": password
    }
    headers = {"accept": "application/json"}

    response = requests.post(login_url, data=login_data, headers=headers)
    response.raise_for_status()

    user_jwt = response.json().get("access_token")
    if not user_jwt:
        raise Exception("No access_token found in login response.")

    print(f"Obtained JWT: {user_jwt}")

except Exception as e:
    print(f"Failed to get JWT token: {e}")
    exit(1)

# Hardcoded JWT (for reference)
# user_jwt = (
#     "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
#     "eyJzdWIiOiJhNDI5ZjZkMi03ZGZmLTQ0MjYtOWVlOC1lOThmZjc5MjcxYjYiLCJleHAiOjE3NTE3NTc3MjR9."
#     "9EIhXM2qynKkJBLz1lBFU_ZtT65CQfglXPJ0cU8g9jE"
# )

# Generate a test session ID
session_id = str(uuid.uuid4())

# Build the full WebSocket URL
ws_url = f"{ws_url_base}?token={user_jwt}&session_id={session_id}"

# Full message structure
message = {
    "message": (
        "Please draft a professional email introducing myself to the hiring manager. "
        "The recipient is the Hiring Manager of a quantitative trading firm. "
        "The purpose is to express my interest in a Quant Developer role. "
        "Include the following key points:\n"
        "- I am an experienced quantitative developer with expertise in algorithmic trading systems.\n"
        "- I have strong skills in Python and C++, and I specialize in low-latency real-time data processing.\n"
        "- I am passionate about financial markets and enjoy solving complex problems collaboratively.\n"
        "End the email with a polite closing, expressing interest in hearing from them."
    ),
    "llm_name": "admin",
    "provider": "openai",
    "files": []
}

def extract_draft_email(data):
    """Extracts the draft email from the agent_response JSON."""
    agents_trace = data.get("response", {}).get("agents_trace")

    if not isinstance(agents_trace, list):
        print("Error: 'agents_trace' is missing or not a list.")
        return None

    for entry in agents_trace:
        if entry.get("name") == "email_drafter":
            translation = entry.get("output", {}).get("translation")
            if translation:
                return translation
            else:
                print("Error: 'translation' missing in email_drafter output.")
                return None

    print("Error: No 'email_drafter' entry found in agents_trace.")
    return None



try:
    print(f"Connecting to {ws_url} ...")
    ws = create_connection(ws_url)
    print("Connection established.")

    # Send your message
    ws.send(json.dumps(message))
    print("Message sent.")

    # Keep listening for responses until the final answer arrives





    while True:
        response = ws.recv()

        try:
            data = json.loads(response)
            msg_type = data.get("type")

            if msg_type in ["agent_response", "final_response"]:
                outer_response = data.get("response", {})

                # Try to extract using the helper
                draft_email = extract_draft_email(outer_response)

                if draft_email:
                    print("Final Answer:")
                    print(draft_email)
                else:
                    print("Final Answer (raw):")
                    # Fall back to print the outer response if no draft email found
                    print(json.dumps(outer_response, indent=2))

                break

            else:
                print("Received intermediate message:")
                print(json.dumps(data, indent=2))

        except json.JSONDecodeError:
            print("Received non-JSON response:")
            print(response)




    ws.close()

except Exception as e:
    print(f"Connection failed: {e}")
