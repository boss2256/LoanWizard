import pandas as pd
import joblib
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton


ASK_INCOME, ASK_PROPERTY_VALUE, ASK_AGE, ASK_EMPLOYMENT_STATUS, ASK_CREDIT_RATING = range(5)

# Load the model
model_path = 'src/loan_eligibility_model.joblib'
model = joblib.load(model_path)

async def home_loan_inquiry(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Initiate loan inquiry by asking for monthly income."""
    await update.callback_query.edit_message_text("Please enter your monthly income (e.g., 3000):")
    return ASK_INCOME

async def ask_property_value(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    income = update.message.text
    if not income.isdigit():
        await update.message.reply_text("Please enter a valid number for income.")
        return ASK_INCOME

    context.user_data['income'] = int(income)
    await update.message.reply_text("Thank you! Now, please enter the property value (e.g., 500000):")
    return ASK_PROPERTY_VALUE

async def ask_age(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    property_value = update.message.text
    if not property_value.isdigit():
        await update.message.reply_text("Please enter a valid number for property value.")
        return ASK_PROPERTY_VALUE

    context.user_data['property_value'] = int(property_value)
    await update.message.reply_text("Enter your age:")
    return ASK_AGE  # Move to ASK_AGE state

async def ask_employment_status(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    age = update.message.text
    if not age.isdigit():
        await update.message.reply_text("Please enter a valid age.")
        return ASK_AGE

    context.user_data['age'] = int(age)
    keyboard = [
        [InlineKeyboardButton("Salaried", callback_data='salaried')],
        [InlineKeyboardButton("Self-employed", callback_data='self-employed')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Select your employment status:", reply_markup=reply_markup)
    return ASK_EMPLOYMENT_STATUS  # Move to ASK_EMPLOYMENT_STATUS state

async def ask_credit_rating(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    context.user_data['employment_status'] = query.data

    keyboard = [
        [InlineKeyboardButton("Excellent", callback_data='excellent')],
        [InlineKeyboardButton("Good", callback_data='good')],
        [InlineKeyboardButton("Average", callback_data='average')],
        [InlineKeyboardButton("Poor", callback_data='poor')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("Select your credit rating:", reply_markup=reply_markup)
    return ASK_CREDIT_RATING

async def calculate_loan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    query = update.callback_query
    await query.answer()
    context.user_data['credit_rating'] = query.data

    # Get all user inputs
    income = context.user_data.get('income')
    property_value = context.user_data.get('property_value')
    age = context.user_data.get('age')
    employment_status = context.user_data.get('employment_status')
    credit_rating = context.user_data.get('credit_rating')

    # Map text inputs to numeric values
    employment_map = {'salaried': 1, 'self-employed': 0}
    credit_map = {'excellent': 3, 'good': 2, 'average': 1, 'poor': 0}

    # Prepare data for prediction
    input_data = pd.DataFrame({
        'Monthly Income': [income],
        'Age': [age],
        'Employment Status': [employment_map[employment_status]],
        'Property Value': [property_value],
        'Credit Rating': [credit_map[credit_rating]]
    })

    # Make prediction
    predicted_loan_amount = model.predict(input_data)[0]

    await query.edit_message_text(
        f"Based on your details, your eligible loan amount is approximately: SGD {predicted_loan_amount:.2f}"
    )
    return ConversationHandler.END
