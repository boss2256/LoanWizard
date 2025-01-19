def log_message(update, context):
    """Log user messages for debugging."""
    user = update.message.from_user
    logger.info(f"User {user.first_name} said: {update.message.text}")

def format_response(text):
    """Format responses before sending them to the user."""
    return f"🤖 {text}"
