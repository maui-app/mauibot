from message_handlers.login_complete import login_complete
from utilities.actions import get_latest as get_latest_action

def message_handler(update, context):
    chat_id = str(update.effective_chat.id)
    latest_action = get_latest_action()

    if latest_action is "login":
        return login_complete(update, context)

    text = "Hmmm. I'm sorry. I don't think we have communicated before."
    return context.bot.send_message(chat_id=chat_id, text=text)