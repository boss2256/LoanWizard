# LoanWizard

**LoanWizard** is an intelligent loan eligibility predictor designed to assist banks and financial institutions in making informed lending decisions. Leveraging machine learning algorithms, LoanWizard provides accurate predictions of eligible loan amounts based on income, property value, credit rating, and more.

---

## Features

- **Loan Eligibility Prediction**  
  Uses advanced machine learning models (e.g., Random Forest and Linear Regression) to predict eligible loan amounts.

- **Scalability**  
  Efficiently processes multiple applications, ensuring rapid predictions.

- **Customizable Inputs**  
  Easily adapt the parameters such as income, property value, and credit rating for tailored results.

---

---

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - `scikit-learn` for machine learning
  - `joblib` for model persistence
  - `Telegram Bot API` for chatbot functionality
  - `pandas`, `numpy`, and `matplotlib` for data processing and visualization

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/boss2256/LoanWizard.git
   ```
2. Navigate to the project directory:
   ```bash
   cd LoanWizard
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Run the Telegram bot:
   ```bash
   python src/bot.py
   ```
2. Interact with the bot on Telegram to check loan eligibility.

---

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request on GitHub.

---

## License

This project is licensed under the [MIT License](LICENSE).
