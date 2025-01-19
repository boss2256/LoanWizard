from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters, ConversationHandler
)
from src.bot import start, help_command, button, cancel
from src.home_loan import (
    home_loan_inquiry, ask_property_value, ask_age,
    ask_employment_status, ask_credit_rating, calculate_loan,
    ASK_INCOME, ASK_PROPERTY_VALUE, ASK_AGE, ASK_EMPLOYMENT_STATUS, ASK_CREDIT_RATING
)
import logging
from config import TELEGRAM_BOT_TOKEN
from warnings import filterwarnings
from telegram.warnings import PTBUserWarning

# Suppress PTBUserWarnings about per_message
filterwarnings(action="ignore", message=r".*CallbackQueryHandler", category=PTBUserWarning)

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='logs/bot.log'
)

logger = logging.getLogger(__name__)

def main():
    # Create the Application and pass it the bot's token.
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Define the conversation handler with the states for each user input
    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(button)],
        states={
            ASK_INCOME: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_property_value)],
            ASK_PROPERTY_VALUE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_age)],
            ASK_AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_employment_status)],
            ASK_EMPLOYMENT_STATUS: [CallbackQueryHandler(ask_credit_rating)],
            ASK_CREDIT_RATING: [CallbackQueryHandler(calculate_loan)],
        },
        fallbacks=[CommandHandler('cancel', cancel)],
        # per_message=False (default), allows mix of MessageHandler and CallbackQueryHandler
    )

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Add the conversation handler to the application
    application.add_handler(conv_handler)

    # Start polling
    application.run_polling()

if __name__ == '__main__':
    main()
