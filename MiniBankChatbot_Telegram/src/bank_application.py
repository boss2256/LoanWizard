from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

async def bank_application(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles inquiries about bank applications."""
    keyboard = [
        [
            InlineKeyboardButton("Open New Account", callback_data='open_new_account'),
            InlineKeyboardButton("Close Existing Account", callback_data='close_existing_account')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.callback_query.edit_message_text(
        text="Would you like to open a new account or close an existing one?",
        reply_markup=reply_markup
    )
