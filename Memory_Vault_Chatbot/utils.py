def count_words(text):
    return len(text.split())


def count_characters(text):
    return len(text)


def format_chat(history):

    conversation = ""

    for chat in history:

        conversation += f"""
User:
{chat['user']}

Assistant:
{chat['ai']}

"""

    return conversation