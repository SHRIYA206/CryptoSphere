

# # # import streamlit as st
# # # from langchain import HuggingFaceHub
# # # import re

# # # def app():
# # #     st.title("Cryptocurrency Expert")

# # #     # Initialize the HuggingFaceHub instance
# # #     llm = HuggingFaceHub(
# # #         repo_id='FahriBilici/crypto-gpt-neo-1.3B',
# # #         model_kwargs={'temperature': 0.5, 'max_length': 300},
# # #        
# # #     )

# # #     # Text input for user prompt
# # #     user_input = st.text_input("Enter your prompt:", "")

# # #     if st.button("Generate"):
# # #         if user_input:
# # #             # Generate text based on user input
# # #             generation = llm.generate(prompts=[user_input])
# # #             if generation:
# # #                 # Convert the LLMResult object to a string
# # #                 generation_str = str(generation)
# # #                 # Extract the generated text from the string
# # #                 generated_text = extract_text_from_generation(generation_str)
# # #                 if generated_text:
# # #                     generated_text.replace("\n", ", ")
# # #                     st.write("Generated Text:")
# # #                     st.write(generated_text + ".")
# # #                 else:
# # #                     st.write("Failed to extract text.")
# # #             else:
# # #                 st.write("Failed to generate text.")
# # #         else:
# # #             st.write("Please enter a prompt.")

# # # def extract_text_from_generation(generation_str):
# # #     # Use regular expressions to extract the generated text from the string representation of the LLMResult object
# # #     match = re.search(r'Generation\(text=\'(.*?)\'\)', generation_str)
    
# # #     #match = re.search(r'\n\n(.*?)\n\n', generation_str, re.DOTALL)
# # #    # match = re.search(r'Generation:.*?text:\'(.+?)\'', generation_str)

# # #     if match:
# # #         return match.group(1)
# # #     else:
# # #         return None

# # # if __name__ == "__main__":
# # #     app())
# from dotenv import load_dotenv
# import anthropic
# import streamlit as st
# import requests
# import os
# from streamlit_lottie import st_lottie

# def load_lottieurl(url: str):
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             return None
#     except requests.exceptions.RequestException as e:
#         st.error(f"Error fetching Lottie animation: {e}")
#         return None

# def get_typewriter_animation():
#     typewriter_animation = """
#                             <style>
#                                 @import url('https://fonts.googleapis.com/css2?family=Source+Code+Pro:wght@400..700&display=swap');

#                                 .title-font {
#                                     font-family: 'Source Code Pro', monospace;
#                                     font-size: 48px;
#                                     width: 100%;
#                                     overflow: hidden;
#                                     white-space: nowrap;
#                                     margin: 0 auto;
#                                     letter-spacing: 0em;
#                                     animation: typing 4s steps(40, end), blink-caret .75s step-end infinite;
#                                 }

#                                 @keyframes typing {
#                                     from { width: 0; }
#                                     to { width: 100%; }
#                                 }

#                                 @keyframes blink-caret {
#                                     from, to { border-color: transparent; }
#                                     50% { border-color: black; }
#                                 }
#                             </style>
#                             <h1 class="title-font">CryptoChatbot</h1>
#                             """
#     return typewriter_animation

# def generate_response(prompt):
#     api_key = os.getenv("ANTHROPIC_API_KEY")
#     client = anthropic.Anthropic(
#         api_key=api_key,
#     )

#     message = client.messages.create(
#         model="claude-3-opus-20240229",
#         max_tokens=1000,
#         temperature=0,
#         messages=[
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return message.content[0].text

# def main():
#     st.set_page_config(page_title="CryptoChatbot", layout="centered")
#     load_dotenv()

#     lottie_url = "https://lottie.host/6ebe5ec4-7e33-4ed0-8415-c3d37b7edeea/mYFm9A9W9h.json"
#     typewriter_animation = get_typewriter_animation()

#     cola, colb, colc = st.columns([1, 3, 1])
#     with colb:
#         st.markdown(typewriter_animation, unsafe_allow_html=True)
    
#     st_lottie(load_lottieurl(lottie_url), height=135, speed=1, loop=True, quality='high')

#     st.header("Welcome to CryptoChatbot")

#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     prompt = st.text_input("Ask me anything about cryptocurrencies:", key="chat_input")

#     if st.button("Generate Response"):
#         if prompt:
#             st.session_state.messages.append({"role": "user", "content": prompt})
#             with st.chat_message("user"):
#                 st.markdown(prompt)
            
#             response = generate_response(prompt)
#             st.session_state.messages.append({"role": "assistant", "content": response})
#             with st.chat_message("assistant"):
#                 st.markdown(response)

# if __name__ == "__main__":
#     main()
