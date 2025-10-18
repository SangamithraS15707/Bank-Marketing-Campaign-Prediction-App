# Bank Marketing Campaign Prediction App

This project is a web application built using Streamlit that predicts whether a client will subscribe to a term deposit based on various input features related to a bank marketing campaign.

## Project Structure

```
bank-marketing-app
├── src
│   ├── app.py                # Main application code
│   ├── pipeline.pkl          # Serialized model with preprocessing steps
│   └── utils
│       └── __init__.py       # Initialization file for utils package
├── requirements.txt          # Python dependencies
├── .gitignore                # Files and directories to ignore by Git
└── README.md                 # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd bank-marketing-app
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
streamlit run src/app.py
```

This will start a local web server, and you can access the application in your web browser at `http://localhost:8501`.

## Usage

- Input the required features in the web interface.
- Click the "Predict" button to see if the client is likely to subscribe to a term deposit.

## License

This project is licensed under the MIT License.