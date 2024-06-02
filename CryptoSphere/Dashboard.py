
import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
import plotly.express as px
import numpy as np

# Function to fetch cryptocurrency data from Yahoo Finance
def fetch_crypto_data(ticker):
    try:
        crypto_data = yf.download(ticker, start="2023-07-01", end="2024-04-01")
        return crypto_data
    except Exception as e:
        st.error(f"An error occurred while fetching data for {ticker}: {str(e)}")
        return None
    

def display_video_background(video_url):
        video_html = f"""
        <video autoplay muted loop playsinline width="100%">
            <source src="{video_url}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        """
        css_code = """
        <style>
        video {
            position: fixed;
            top: 0%;
            left: 0%;
            min-width: 100%;
            min-height: 100%;
            height: auto;
        }
        </style>
        """
        # Display the video background and the Streamlit app content
        st.markdown(video_html + css_code, unsafe_allow_html=True)
 # Display video background
video_url = "https://cdn.discordapp.com/attachments/1232741156664774700/1238759907029811211/Gen-2_4219217298_logo_should_not_be_s_okjpg_M_5_1.mp4?ex=66407490&is=663f2310&hm=81878a4ff0f807f43dc3cc6a1241d5fdbda874287e64b80fe95102d12bc2f8fb&"  
display_video_background(video_url)

# Function to calculate MACD indicators
def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    short_ema = data['Close'].ewm(span=short_window, min_periods=1, adjust=False).mean()
    long_ema = data['Close'].ewm(span=long_window, min_periods=1, adjust=False).mean()
    macd_line = short_ema - long_ema
    signal_line = macd_line.ewm(span=signal_window, min_periods=1, adjust=False).mean()
    macd_histogram = macd_line - signal_line
    return macd_line, signal_line, macd_histogram

# Function to plot MACD indicator
def plot_macd(data, macd_line, signal_line, macd_histogram):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=macd_line, mode='lines', name='MACD Line'))
    fig.add_trace(go.Scatter(x=data.index, y=signal_line, mode='lines', name='Signal Line'))
    fig.add_trace(go.Bar(x=data.index, y=macd_histogram, marker=dict(color=np.where(macd_histogram > 0, 'green', 'red')),
                         name='MACD Histogram'))
    fig.update_layout(title='MACD Indicator', xaxis_title='Date', yaxis_title='MACD')
    fig.update_traces(showlegend=True)
    return fig

# Function to plot OHLC chart
def plot_ohlc(data):
    fig_ohlc = go.Figure()
    fig_ohlc.add_trace(go.Scatter(x=data.index, y=data['Open'], mode='lines', name='Open'))
    fig_ohlc.add_trace(go.Scatter(x=data.index, y=data['High'], mode='lines', name='High'))
    fig_ohlc.add_trace(go.Scatter(x=data.index, y=data['Low'], mode='lines', name='Low'))
    fig_ohlc.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close'))
    fig_ohlc.update_layout(title='OHLC Over Time', xaxis_title='Date', yaxis_title='Price')
    fig_ohlc.update_traces(showlegend=True)
    return fig_ohlc

# Function to plot volume chart
def plot_volume_chart(data):
    fig_volume = go.Figure()
    fig_volume.add_trace(go.Scatter(x=data.index, y=data['Volume'], fill='tozeroy', mode='lines', name='Volume', line=dict(color='blue')))
    fig_volume.update_layout(title='Volume Over Time', xaxis_title='Date', yaxis_title='Volume')
    return fig_volume

# Function to plot scatter chart
def plot_scatter_chart(data):
    x_col_options = data.columns.tolist()
    y_col_options = data.columns.tolist()
    x_col = st.selectbox('Select X-Axis:', options=x_col_options, index=0)
    y_col = st.selectbox('Select Y-Axis:', options=y_col_options, index=1)
    fig = px.scatter(data, x=x_col, y=y_col, title=f'{y_col} vs {x_col}', 
                     labels={'x': x_col, 'y': y_col})
    return fig

# Main application function
def app():
    # Page title
    st.title('Cryptocurrency Analytics')

    # Sidebar for user input
    st.sidebar.title('Select Analytics Type:')
    selected_graph = st.sidebar.radio('', 
                                      ['OHLC Chart', 'Volume Chart', 'MACD Indicator', 'Scatter Plot'])

    # Ticker dropdown menu
    st.sidebar.title('Select Cryptocurrency:')
    ticker_options = {
    'Bitcoin (BTC)': 'BTC-USD',
    'Ethereum (ETH)': 'ETH-USD',
    'Ripple (XRP)': 'XRP-USD',
    'Litecoin (LTC)': 'LTC-USD',
    'Cardano (ADA)': 'ADA-USD',
    'Polkadot (DOT)': 'DOT-USD',
    'Chainlink (LINK)': 'LINK-USD',
    'Dogecoin (DOGE)': 'DOGE-USD',
    'Tezos (XTZ)': 'XTZ-USD',
    'EOS (EOS)': 'EOS-USD',
    'VeChain (VET)': 'VET-USD'
}

    ticker = st.sidebar.selectbox('', options=list(ticker_options.keys()))

    # Plotting selected chart
    st.markdown('---')
    try:
        if selected_graph == 'OHLC Chart':
            crypto_data = fetch_crypto_data(ticker_options[ticker])
            if crypto_data is not None:
                st.subheader('OHLC Chart Over Time:')
                ohlc_fig = plot_ohlc(crypto_data)
                st.plotly_chart(ohlc_fig)

        elif selected_graph == 'Volume Chart':
            crypto_data = fetch_crypto_data(ticker_options[ticker])
            if crypto_data is not None:
                st.subheader('Volume Chart Over Time:')
                volume_fig = plot_volume_chart(crypto_data)
                st.plotly_chart(volume_fig)

        elif selected_graph == 'MACD Indicator':
            crypto_data = fetch_crypto_data(ticker_options[ticker])
            if crypto_data is not None:
                st.subheader('MACD Indicator:')
                macd_line, signal_line, macd_histogram = calculate_macd(crypto_data)
                macd_fig = plot_macd(crypto_data, macd_line, signal_line, macd_histogram)
                st.plotly_chart(macd_fig)

        elif selected_graph == 'Scatter Plot':
            crypto_data = fetch_crypto_data(ticker_options[ticker])
            if crypto_data is not None:
                st.subheader('Scatter Plot:')
                scatter_fig = plot_scatter_chart(crypto_data)
                st.plotly_chart(scatter_fig)

    except Exception as e:
        st.error(f"An error occurred while fetching or plotting data for {ticker}: {str(e)}")

if __name__ == "__main__":
    app()
