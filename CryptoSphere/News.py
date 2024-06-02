
# import streamlit as st
# import requests
# import pandas as pd

# def app():
#     def get_crypto_data():
#         url = "https://cryptocurrency-news2.p.rapidapi.com/v1/cointelegraph"

#         headers = {
#             "X-RapidAPI-Key": "39f4027ae7msha30498ecd756420p13b666jsnfd4e1d3ff06e",
#             "X-RapidAPI-Host": "cryptocurrency-news2.p.rapidapi.com"
#         }

#         response = requests.get(url, headers=headers)
#         return response.json()

#     crypto_data = get_crypto_data()

#     st.title("Crypto News")

#     # Styling for the title
#     st.markdown('---')
#     st.subheader("Latest News")
#     st.markdown('---')

#     # Displaying news articles
#     for item in crypto_data['data']:
#         st.write(f"**Title:** {item['title']}")
#         st.image(item['thumbnail'], caption=item['description'], use_column_width=True)
#         st.write(f"**URL:** [{item['url']}]({item['url']})")
#         st.write(f"**Published At:** {item['createdAt']}")
#         st.markdown('---')

# if __name__ == '__main__':
#     app()

import streamlit as st
import requests

def app():
    def get_crypto_data():
        url = "https://cryptocurrency-news2.p.rapidapi.com/v1/cointelegraph"

        headers = {
            "X-RapidAPI-Key": "39f4027ae7msha30498ecd756420p13b666jsnfd4e1d3ff06e",
            "X-RapidAPI-Host": "cryptocurrency-news2.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)
        return response.json()

    crypto_data = get_crypto_data()

    st.title("Crypto News")

    # Styling for the title
    st.markdown('---')
    st.subheader("Latest News")
    st.markdown('---')

    # Displaying news articles
    for item in crypto_data['data']:
        st.markdown(f"**Title:** {item['title']}")
        st.image(item['thumbnail'], use_column_width=True)
        st.markdown(f"*Description:* {item['description']}")
        st.markdown(f"[Read more]({item['url']})")
        st.markdown(f"*Published At:* {item['createdAt']}")
        st.markdown('---')

if __name__ == '__main__':
    app()
