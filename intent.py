def detect_intent(text):
    text = text.lower()
    intents = []

    # Create file (more flexible)
    if ("create" in text and "file" in text) or ("make" in text and "file" in text):
        intents.append("create_file")

    # Write code
    if ("write" in text and "code" in text) or ("generate" in text and "code" in text):
        intents.append("write_code")

    # Summarize
    if "summarize" in text or "summary" in text:
        intents.append("summarize")

    # Default
    if not intents:
        intents.append("chat")

    return intents