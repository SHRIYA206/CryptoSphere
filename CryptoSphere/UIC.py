
import streamlit as st
import pandas as pd 
import numpy as np 
from sklearn.preprocessing import MinMaxScaler
import plotly.graph_objects as go
import yfinance as yf 
from datetime import date, timedelta
from tensorflow.keras.models import load_model
import plotly.express as px

# Load the model
model = load_model("CryptoSphere.keras")

def app():
    st.title('CryptoSphere 💻💰')
    st.write("Welcome to the Crypto price prediction app! This app allows you to predict the future crypto prices. This machine learning project aims to predict cryptocurrency prices using historical data and various predictive models, assisting investors in making informed decisions.")
    st.sidebar.title('Ticker')
    ticker = st.sidebar.text_input('Enter Crypto Ticker', 'BTC-USD')
    start_date = '2023-01-01'  # Adjusted start date
    end_date = date.today()  # Adjusted end date
    dates = pd.date_range(start=start_date, end=end_date)

    # Function to predict crypto prices
    def predict_crypto_prices(data):
        # Preprocess the data
        x_test = pd.DataFrame(data.Close)
        scaler = MinMaxScaler(feature_range=(0,1))
        scaled_data = scaler.fit_transform(x_test[['Close']])

        x_data = []
        for i in range(100, len(scaled_data)):
            x_data.append(scaled_data[i-100:i])

        x_data = np.array(x_data)
        predictions = model.predict(x_data)
        inv_pre = scaler.inverse_transform(predictions)

        # Create a DataFrame for predicted prices
        predicted_data = pd.DataFrame(inv_pre, columns=['Predicted Price'], index=data.index[100:])

        return predicted_data

    # Function to predict the next N days prices
    def predict_next_n_days(data, n):
        # Preprocess the data
        x_test = pd.DataFrame(data.Close)
        scaler = MinMaxScaler(feature_range=(0,1))
        scaled_data = scaler.fit_transform(x_test[['Close']])

        x_data = []
        for i in range(100, len(scaled_data)):
            x_data.append(scaled_data[i-100:i])

        x_data = np.array(x_data)

        # Predict the next N days
        predictions = []
        last_sequence = x_data[-1]  # Last sequence in the dataset
        for _ in range(n):
            prediction = model.predict(last_sequence.reshape(1, -1, 1))
            predictions.append(prediction[0][0])  # Append the prediction
            last_sequence = np.roll(last_sequence, -1)  # Shift the sequence by one step
            last_sequence[-1] = prediction  # Update the last element with the prediction

        # Inverse transform the predictions
        inv_pre = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))

        # Generate date range for the next N days starting from tomorrow
        next_n_days_dates = pd.date_range(start=data.index[-1] + timedelta(days=1), periods=n, freq='D')

        # Create a DataFrame for predicted prices with date index
        predicted_data = pd.DataFrame(inv_pre, columns=['Predicted Price'], index=next_n_days_dates)

        return predicted_data

    # Function to calculate investment recommendation
    def calculate_investment_recommendation(predicted_data):
        # Calculate the percentage change in predicted prices
        price_change = (predicted_data.iloc[-1]['Predicted Price'] - predicted_data.iloc[0]['Predicted Price']) / predicted_data.iloc[0]['Predicted Price'] * 100

        # Check volatility of predicted prices
        volatility = predicted_data['Predicted Price'].std()

        # Check recent price trend
        recent_trend = 'Increasing' if predicted_data.iloc[-1]['Predicted Price'] > predicted_data.iloc[-2]['Predicted Price'] else 'Decreasing'

        # Determine recommendation based on conditions
        if price_change > 5 and volatility < 10 and recent_trend == 'Increasing':
            recommendation = "Invest with Confidence"
            recommendation_details = "The predicted price is expected to increase by at least 5%, with low volatility and an increasing trend."
        elif price_change > 5 and volatility < 15 and recent_trend == 'Increasing':
            recommendation = "Invest with Caution"
            recommendation_details = "The predicted price is expected to increase by at least 5%, with moderate volatility and an increasing trend."
        elif recent_trend == 'Decreasing':
            recommendation = "Wait and Watch"
            recommendation_details = "The recent trend indicates a decreasing price. It is advisable to wait and observe before making any investment."
        else:
            recommendation = "Don't Invest"
            recommendation_details = "No clear trend or significant expected price change detected. It is not recommended to invest at this time."

        return recommendation, recommendation_details

    # Main Streamlit app
    # Fetch historical stock data
    data = yf.download(ticker, start=start_date, end=end_date)

    # Predict crypto prices
    predicted_data = predict_crypto_prices(data)

    # Display original and predicted prices on the same graph
    st.subheader("Original vs Predicted Values")
    combined_data = pd.concat([data['Close'], predicted_data], axis=1)
    combined_data.columns = ['Original Close Price', 'Predicted Close Price']

    fig = px.line(combined_data, 
                  x=combined_data.index, 
                  y=['Original Close Price', 'Predicted Close Price'], 
                  labels={'value': 'Price', 'variable': 'Series'},
                  color_discrete_sequence=['blue', 'red'])  # Set colors for lines
    fig.update_layout(title="Original vs Predicted Prices", xaxis_title="Date", yaxis_title="Price")
    st.plotly_chart(fig)

    # Predict prices for the next 30 days
    predicted_data_next_30_days = predict_next_n_days(data, 30)

    # Plot predicted data for the next 30 days
    fig_next_30_days = go.Figure()

    # Plot original data
    fig_next_30_days.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Original Data'))

    # Plot predicted data for the next 30 days
    fig_next_30_days.add_trace(go.Scatter(x=predicted_data_next_30_days.index, y=predicted_data_next_30_days['Predicted Price'], mode='lines', name='Predicted Data (Next 30 Days)', line=dict(color='orange')))

    # Update layout
    fig_next_30_days.update_layout(title=f'Crypto Price Prediction for the Next 30 Days', xaxis_title='Date', yaxis_title='Price')

    # Display the plot
    st.plotly_chart(fig_next_30_days)

    # Predict prices for the next 60 days
    predicted_data_next_60_days = predict_next_n_days(data, 60)

    # Plot predicted data for the next 60 days
    fig_next_60_days = go.Figure()

    # Plot original data
    fig_next_60_days.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Original Data'))

    # Plot predicted data for the next 60 days
    fig_next_60_days.add_trace(go.Scatter(x=predicted_data_next_60_days.index, y=predicted_data_next_60_days['Predicted Price'], mode='lines', name='Predicted Data (Next 60 Days)', line=dict(color='purple')))

    # Update layout
    fig_next_60_days.update_layout(title=f'Crypto Price Prediction for the Next 60 Days', xaxis_title='Date', yaxis_title='Price')

    # Display the plot
    st.plotly_chart(fig_next_60_days)

    # Calculate investment recommendation for the next 30 days
    recommendation_n_days, recommendation_details_n_days = calculate_investment_recommendation(predicted_data_next_30_days)

    # Display recommendation inside a glass card
    st.markdown(
        f"""
        <div style='
            background-color: #bbdefb;
            color: #333333;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            '>
            <h3 style="color: #333333;">Investment Recommendation</h3>
            <p>{recommendation_details_n_days}</p>
            <p><strong>{recommendation_n_days}</strong></p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    app()
