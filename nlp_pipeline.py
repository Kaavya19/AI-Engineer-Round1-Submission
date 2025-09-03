def analyze_email(email):
    body = email['body'].lower()
    sentiment = "Negative" if "cannot" in body or "issue" in body else "Neutral"
    priority = "Urgent" if "cannot" in body or "immediately" in body else "Not urgent"
    email['sentiment'] = sentiment
    email['priority'] = priority
    return email
    