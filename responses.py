def basic_responses(input_text):
    user_message = str(input_text).casefold()
    if user_message in ("hi", "hello"):
        return "Hello"