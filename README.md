# Bank Marketing Campaign Prediction App

This project is a web application built using Streamlit that predicts whether a client will subscribe to a term deposit based on various input features related to a bank marketing campaign using logistic regression.

## Project Structure

```
bank-marketing-app

├── app.py                          # Main application code
├── log_reg_model (2).joblib        #model to make predictions
├──preprocessor (2).joblib          # preprocessing steps to make the data perfect for prediction
├──__init__.py                      # Initialization file for utils package
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/SangamithraS15707/Bank-Marketing-Campaign-Prediction-App.git
   cd Bank-Marketing-Campaign-Prediction-App
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Streamlit application, execute the following command in your terminal:
```
streamlit run app.py
```

This will start a local web server, and you can access the application in your web browser at `http://localhost:8501`.

## Usage

- Input the required features in the web interface.
- Click the "Predict" button to see if the client is likely to subscribe to a term deposit.

## License

This project is licensed under the MIT License.
