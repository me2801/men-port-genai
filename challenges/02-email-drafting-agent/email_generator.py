def generate_email(recipient: str, purpose: str, points: list[str]) -> dict:
    body = " ".join(points)
    subject = f"{purpose.title()}"
    greeting = f"Dear {recipient},"
    closing = "Best regards,\nYour Name"

    email_text = f"{greeting}\n\n{body}\n\n{closing}"
    return {
        "subject": subject,
        "body": email_text
    }
