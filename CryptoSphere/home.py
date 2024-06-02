
import streamlit as st
from pylivecoinwatch import LiveCoinWatchAPI
import pandas as pd
from PIL import Image
from urllib.request import urlopen
from io import BytesIO

# Initialize LiveCoinWatchAPI with your API key
lcw = LiveCoinWatchAPI("626ddd8f-5f9c-4028-9c31-1cb2d1211bc6")

# Function to get crypto data
def get_crypto_data():
    # Make the API request
    crypto_data = lcw.coins_list(limit=48, currency="USD", sort="rank", order="ascending", meta=True)
    return crypto_data

def app():
    # Check if the response has data
    crypto_data = get_crypto_data()
    css = """
    /* CSS to style the Streamlit app */
    .stApp {
        max-width: 1800px;
        /*background-color: #FFFFFF;  New background color */
    }

    .stTitle {
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 20px;
        font-color:#FF0000;
    }

    .stMarkdown {
        margin-top: 20px;
        margin-bottom: 20px;
    }

    .stImage {
        max-width: 200px;
        max-height: 200px;
        margin-bottom: 20px;
    }

    .stHeader {
        background-color: #f0f0f0;
        padding: 10px 20px;
        border-radius: 5px;
        margin-bottom: 20px;
    }

    .stSubheader {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .stInfo {
        margin-bottom: 10px;
    }

    .stInfo span {
        font-weight: bold;
    }

    .stData {
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
    }

    .stDataColumn {
        flex-basis: 30%;
        margin-bottom: 20px;
    }
    """

    # Apply the CSS using st.markdown()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    if crypto_data:
        # Convert the data to a DataFrame
        df = pd.DataFrame(crypto_data)

        # Drop columns with null values
        df = df.dropna(axis=1, how='any')

        # Display the DataFrame using Streamlit
        st.title("Live Cryptocurrency Data")

        # Display the details of each cryptocurrency
        col1, col2, col3, col4, col5, col6, col7 = st.columns(7, gap='medium')
        with col1:
            st.subheader("Name")
        with col2:
            st.subheader("Image")
        with col3:
            st.subheader("Symbol")
        with col4:
            st.subheader("Rate")
        with col5:
            st.subheader("Cap")
        with col6:
            st.subheader("Volume")
        with col7:
            st.subheader("Total Supply")
            
        for index, row in df.iterrows():
            with col1:
                st.markdown(f"<p style='color:white;'>{row['name']}</p>", unsafe_allow_html=True)

            with col2:
                st.text("")
                a = row['png32']
                u = urlopen(a)
                raw_data = u.read()
                u.close()
                im = Image.open(BytesIO(raw_data))
                resized_image = im.resize((33, 34))
                st.image(resized_image)
            with col3:
                st.write(row['code'])
            with col4:
                st.write(round(row['rate'], 2))
            with col5:
                st.write(row['cap'])
            with col6:
                st.write(row['volume'])
            with col7:
                st.write(row['totalSupply'])
        
    else:
        st.warning("No data to display.")

# Call the app function
if __name__ == "__main__":
    app()
