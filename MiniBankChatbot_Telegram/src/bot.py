from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler

from src.home_loan import home_loan_inquiry, ask_property_value, calculate_loan
from src.bank_application import bank_application

ASK_INCOME, ASK_PROPERTY_VALUE = range(2)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a welcome message and displays buttons for user interaction."""
    keyboard = [
        [
            InlineKeyboardButton("Home Loan", callback_data='home_loan'),
            InlineKeyboardButton("Bank Application", callback_data='bank_application')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Hello! I'm your Mini Bank Chatbot. Please select an option:",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button presses."""
    query = update.callback_query
    await query.answer()  # Acknowledge button press

    # Check which button was pressed and respond accordingly
    if query.data == 'home_loan':
        await home_loan_inquiry(update, context)
        return ASK_INCOME  # Move to the next step of asking income
    elif query.data == 'bank_application':
        await bank_application(update, context)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a help message when the /help command is issued."""
    await update.message.reply_text("You can ask me about:\n - Home Loans\n - Bank Applications")

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Cancels and ends the conversation."""
    await update.message.reply_text("You have canceled the process.")
    return ConversationHandler.END
