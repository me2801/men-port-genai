# Email Drafting Agent

This project is my submission for GenAI Hackathon Mini Challenge #2. It implements an Email Drafting Agent that transforms bullet-point input into polished, professional emails.

## Overview

The agent takes minimal input in bullet-point format, such as:
- Recipient's name and/or role
- Purpose of the email
- Key points or details to include

It then returns a complete email containing:
- A subject line
- A respectful greeting
- A clear, concise body
- A professional closing

## Features

- Modular email construction logic
- Structured prompt templates
- Natural tone with fallback handling for missing data
- Easy deployment and integration with GenAI AgentOS

## Project Structure

```
02-email-drafting-agent/
├── main.py                # Entry point for local testing or agent execution
├── email_generator.py     # Core email generation logic
├── prompt_templates.py    # Templates for subject, greeting, and closing
├── agentos_config.yaml    # Required file to register the agent with AgentOS
├── requirements.txt       # Python dependencies
├── README.md              # This file
└── examples/
    ├── input_example.json
    └── output_example.txt
```

## Setup

Ensure you are using Python 3.8+.

1. Create and activate a virtual environment (optional but recommended):

```
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the script for testing:

```
python main.py
```

## AgentOS Registration

This agent includes an `agentos_config.yaml` file with the necessary metadata to register and run it using GenAI AgentOS. For details, see:

https://github.com/genai-works-org/genai-agentos

## Example Input

```json
{
  "recipient": "Hiring Manager",
  "purpose": "Job application follow-up",
  "points": [
    "Submitted my resume last week",
    "Excited about the role",
    "Happy to provide more information"
  ]
}
```

## Example Output

```
Subject: Following Up on My Application

Dear Hiring Manager,

I hope this message finds you well. I wanted to follow up regarding the job application I submitted last week. I'm very excited about the opportunity and would be happy to provide any additional information you may need.

Thank you for your time and consideration.

Best regards,  
Your Name
```

## Notes

- This agent is designed to handle partial or missing input gracefully.
- Templates can be customized easily in `prompt_templates.py`.

## Optional Deployment

For live testing via ngrok or other services, you can wrap `main.py` in a Flask or FastAPI server. This is optional and can be used to earn bonus points.

## License

This project is open source and free to use for educational purposes.
