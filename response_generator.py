def generate_response(email_body):
    if "cannot access" in email_body.lower():
        return "We’re sorry for the inconvenience. Our team is looking into your login issue and will update you shortly."
    return "Thank you for reaching out. We will assist you with your request soon."
    