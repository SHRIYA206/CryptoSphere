import streamlit as st
st.set_page_config(
    page_title="CryptoSphere",
    layout='wide',
    initial_sidebar_state="expanded"
)

import News
import home
import Dashboard
import Chatbot
import UIC
from streamlit_option_menu import option_menu
import yaml
from streamlit_extras.stylable_container import stylable_container
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.exceptions import (LoginError, RegisterError)
import base64

global flag

def page2():
    app = option_menu(
        menu_title='',
        options=['Home', 'News', 'Dashboard', 'Chatbot', 'Predictions'],
        icons=['house', 'newspaper', 'coin', 'chat', 'bar-chart'],
        menu_icon='chat-text-fill',
        orientation='horizontal',
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": 'black'},
            "icon": {"color": "white", "font-size": "15px"},
            "nav-link": {"color": "white", "font-size": "15px", "text-align": "left", "margin": "0px", "width": "100%"},
            "nav-link-hover": {"background-color": "#200736"},
            "nav-link-selected": {"background-color": "#200736"}
        }
    )

    if app == "Home":
        home.app()
    elif app == "News":
        News.app()
    elif app == "Dashboard":
        Dashboard.app()
    elif app == "Chatbot":
        Chatbot.app()
    elif app == "Predictions":
        UIC.app()

button_style = """
    <style>
    .stButton > button {
        color: white;
        background-color: #200736; 
        border: none;
        border-radius: 15px;
        padding: 5px 15px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
    }
    .stButton:hover > button {
        color: white;
        background-color: #200736;
    }
    .nav-link:hover {
        background-color: #200736 !important;
    }
    </style>
"""
st.markdown(button_style, unsafe_allow_html=True)

# THE PAGE 1 CONTENT IS HERE:-
def page1():
    with open('config_new.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['pre-authorized']
    )

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
        st.markdown(video_html + css_code, unsafe_allow_html=True)

    def display_animated_text(*texts):
        css = """
        @import url('https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@400..700&display=swap'); 
        @keyframes typing {
            from { width: 0 }
            to { width: 100% }
        }
        .typewriter {
            overflow: hidden;
            border-right: .15em solid transparent; 
            white-space: nowrap; 
            margin: 0 auto; 
            letter-spacing: .15em; 
            animation: typing 4.8s steps(45, end); 
            animation-fill-mode: forwards;
            margin: 0; 
            margin-left:35%;
            left: 10pxpx; 
            font-size: 65px; 
            font-family: "Pixelify Sans", sans-serif;
            font-weight: 400;
            font-style: normal;
        }
        """
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
        for text in texts:
            st.markdown(f"<div class='typewriter'>{text}</div>", unsafe_allow_html=True)

    def display_glass_card(*cards):
        css = """
        @import url('https://fonts.googleapis.com/css2?family=Recursive:wght@300..1000&display=swap');
        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(-10px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        .glass-morphism-card {
            animation-name: fadeIn;
            animation-duration: 1s;
            animation-timing-function: ease-in;
            animation-fill-mode: both;
            animation-delay: 2s;
            background: rgba(7, 25, 40, 0.45); 
            border-radius: 10px; 
            backdrop-filter: blur(10px);
            border: 1px solid rgba( 255, 255, 255, 0.18 );
            padding: 20px;
            position: relative; 
            z-index: 1;
        }
        .fonnt{
            font-family: "Recursive", sans-serif;
            font-optical-sizing: auto;
            font-size: 20px;
            font-weight: 700;
            font-style: normal;
            font-variation-settings:
            "slnt" 0,
            "CASL" 0,
            "CRSV" 0.5,
            "MONO" 0;
        }
        .fonnt2{
            font-family: "Recursive", sans-serif;
            font-optical-sizing: auto;
            font-weight: 400;
            font-style: normal;
            font-variation-settings:
            "slnt" 0,
            "CASL" 0,
            "CRSV" 0.5,
            "MONO" 0;
        }
        """
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
        st.markdown('<div style="position: relative;">', unsafe_allow_html=True)
        for card in cards:
            st.markdown(f"<div class='glass-morphism-card'>{card}</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    def main():
        video_url = "https://cdn.discordapp.com/attachments/1232741156664774700/1245097026887090176/Gen-2_1615789569_generate_a_video_whe_vidjpg_M_5.mp4?ex=66578277&is=665630f7&hm=2d86cf7ffc04734a87041c6a6af02f0be089e3cb95f9edd98d739c671ab0b0ff&"
        display_video_background(video_url)
        display_animated_text("CryptoSphere")
        display_glass_card(
            "<div><p class='fonnt'>CryptoSphere</p><p class='fonnt2'>Welcome to CryptoSphere, where we are revolutionizing the cryptocurrency landscape through cutting-edge technology and innovative solutions. Our platform provides real-time data, ensuring you have access to the latest market trends, price movements, and crucial metrics. With comprehensive visualizations, we transform complex information into easily understandable charts and graphs, facilitating informed decision-making. Our live news updates keep you abreast of the latest developments in the cryptocurrency world, from regulatory changes and technological advancements to market shifts and significant events. Additionally, our integrated chatbot offers instant support and answers to your queries, enhancing your user experience. One of our standout features is our predictive analytics, leveraging sophisticated algorithms and machine learning to forecast future trends and investment opportunities, giving you a strategic edge in the dynamic world of digital assets. At CryptoSphere, we are dedicated to empowering our users with unparalleled insights and tools, helping you navigate the complexities of the cryptocurrency market and make well-informed decisions. Join us as we reshape the future of digital finance.</p></div>"
        )

    if __name__ == "__main__":
        main()

    def toggle_sidebar():
        is_expanded = not st.session_state.sidebar_expanded
        st.session_state.sidebar_expanded = is_expanded

    if 'sidebar_expanded' not in st.session_state:
        st.session_state.sidebar_expanded = False

    col1, col2, col3 = st.columns(3)
    with col2:
        button_container = st.empty()
        with button_container.container():
            if st.button("🔑 Login or Register", use_container_width=True, type="primary"):
                toggle_sidebar()

    if st.session_state.sidebar_expanded:
        with st.sidebar:
            selected = option_menu("Register/Login", ["Register", 'Login', 'Logout'], 
                                    icons=['box-arrow-in-right', 'door-open-fill', 'box-arrow-in-left'], 
                                    menu_icon="file-person-fill",
                                    styles={
                                        "container": {"padding": "5!important", "background-color": 'black'},
                                        "icon": {"color": "white", "font-size": "15px"},
                                        "nav-link": {"color": "white", "font-size": "15px", "text-align": "left", "margin": "0px", "width": "100%"},
                                        "nav-link-hover": {"background-color": "#200736"},
                                        "nav-link-selected": {"background-color": "#200736"}
                                    })
        if selected == "Register":
            with st.sidebar:
                try:
                    (email_of_registered_user, username_of_registered_user, name_of_registered_user) = authenticator.register_user(pre_authorization=False)
                    if email_of_registered_user:
                        st.success('User registered successfully!!')
                        st.markdown('<h6 style="color:White; font-size: 16px"> **you can go to the login page and enter the site</h6>', unsafe_allow_html=True)
                except RegisterError as e:
                    st.error(e)
        if selected == "Login":
            with st.sidebar:
                try:
                    authenticator.login()
                except LoginError as e:
                    st.error(e)
                if st.session_state["authentication_status"]:
                    st.markdown('<h6 style="color:#0add08; font-size: 17px">The user has logged in, you can enter the site now!!</h6>', unsafe_allow_html=True)
                    if st.button("Double click to enter the site!", use_container_width=True):
                        st.session_state.current_function = "page2"
                        flag = 1
                elif st.session_state["authentication_status"] is False:
                    st.error('Username/password is incorrect')
        if selected == "Logout":
            with st.sidebar:
                if st.session_state["authentication_status"]:
                    with st.container(border=True):
                        st.subheader('Logout')
                        st.checkbox(f'Are you sure you want to log out, {st.session_state["name"]}?', key='verify_logout')
                        if st.session_state.verify_logout:
                            authenticator.logout()
                else:
                    st.success("User is logged out")

    with open('config_new.yaml', 'w', encoding='utf-8') as file:
        yaml.dump(config, file, default_flow_style=False)

    try:
        if flag == 1:
            page2()
    except Exception as e:
        print(e)

def main():
    if "current_function" not in st.session_state:
        st.session_state.current_function = "page1"
    if st.session_state.current_function == "page1":
        page1()
    elif st.session_state.current_function == "page2":
        if st.session_state["authentication_status"]:
            page2()
        else:
            page1()

if __name__ == "__main__":
    main()
# import streamlit as st
# st.set_page_config(
#     page_title="CryptoSphere",
#     layout='wide',
#     initial_sidebar_state="expanded"
# )

# import News
# import home
# import Dashboard
# import Chatbot
# import UIC
# from streamlit_option_menu import option_menu
# import yaml
# from streamlit_extras.stylable_container import stylable_container
# from yaml.loader import SafeLoader
# import streamlit_authenticator as stauth
# from streamlit_authenticator.utilities.exceptions import (LoginError, RegisterError)
# import base64

# global flag

# def page2():
#     app = option_menu(
#         menu_title='',
#         options=['Home', 'News', 'Dashboard', 'Chatbot', 'Predictions'],
#         icons=['house', 'newspaper', 'coin', 'chat', 'bar-chart'],
#         menu_icon='chat-text-fill',
#         orientation='horizontal',
#         default_index=0,
#         styles={
#             "container": {"padding": "5!important", "background-color": 'black'},
#             "icon": {"color": "white", "font-size": "15px"},
#             "nav-link": {"color": "white", "font-size": "15px", "text-align": "left", "margin": "0px", "width": "100%"},
#             "nav-link-hover": {"background-color": "#200736"},
#             "nav-link-selected": {"background-color": "#200736"}
#         }
#     )

#     if app == "Home":
#         home.app()
#     elif app == "News":
#         News.app()
#     elif app == "Dashboard":
#         Dashboard.app()
#     elif app == "Chatbot":
#         Chatbot.app()
#     elif app == "Predictions":
#         UIC.app()

# button_style = """
#     <style>
#     .stButton > button {
#         color: white;
#         background-color: #200736; 
#         border: none;
#         border-radius: 15px;
#         padding: 5px 15px;
#         text-align: center;
#         text-decoration: none;
#         display: inline-block;
#         font-size: 16px;
#         margin: 4px 2px;
#         cursor: pointer;
#     }
#     .stButton:hover > button {
#         color: white;
#         background-color: #200736;
#     }
#     .nav-link:hover {
#         background-color: #200736 !important;
#     }
#     </style>
# """
# st.markdown(button_style, unsafe_allow_html=True)

# # THE PAGE 1 CONTENT IS HERE:-
# def page1():
#     with open('config_new.yaml') as file:
#         config = yaml.load(file, Loader=SafeLoader)

#     authenticator = stauth.Authenticate(
#         config['credentials'],
#         config['cookie']['name'],
#         config['cookie']['key'],
#         config['cookie']['expiry_days'],
#         config['pre-authorized']
#     )

#     def display_video_background(video_url):
#         video_html = f"""
#         <video autoplay muted loop playsinline width="100%">
#             <source src="{video_url}" type="video/mp4">
#             Your browser does not support the video tag.
#         </video>
#         """
#         css_code = """
#         <style>
#         video {
#             position: fixed;
#             top: 0%;
#             left: 0%;
#             min-width: 100%;
#             min-height: 100%;
#             height: auto;
#         }
#         </style>
#         """
#         st.markdown(video_html + css_code, unsafe_allow_html=True)

#     def display_animated_text(*texts):
#         css = """
#         @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&display=swap');
#         @keyframes typing {
#             from { width: 0 }
#             to { width: 100% }
#         }
#         .typewriter {
#             overflow: hidden;
#             border-right: .15em solid transparent;
#             white-space: nowrap;
#             margin: 0 auto;
#             letter-spacing: .15em;
#             animation: typing 4.8s steps(45, end);
#             animation-fill-mode: forwards;
#             margin: 0;
#             font-size: 65px;
#             font-family: 'Cinzel', serif;
#             font-weight: 700;
#             text-align: center;
#             color: white;
#         }
#         """
#         st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
#         for text in texts:
#             st.markdown(f"<div class='typewriter'>{text}</div>", unsafe_allow_html=True)

#     def display_glass_card(*cards):
#         css = """
#         @import url('https://fonts.googleapis.com/css2?family=Recursive:wght@300..1000&display=swap');
#         @keyframes fadeIn {
#             from {
#                 opacity: 0;
#                 transform: translateY(-10px);
#             }
#             to {
#                 opacity: 1;
#                 transform: translateY(0);
#             }
#         }
#         .glass-morphism-card {
#             animation-name: fadeIn;
#             animation-duration: 1s;
#             animation-timing-function: ease-in;
#             animation-fill-mode: both;
#             animation-delay: 2s;
#             background: rgba(7, 25, 40, 0.45);
#             border-radius: 10px;
#             backdrop-filter: blur(10px);
#             border: 1px solid rgba( 255, 255, 255, 0.18 );
#             padding: 20px;
#             position: relative;
#             z-index: 1;
#         }
#         .fonnt{
#             font-family: "Recursive", sans-serif;
#             font-optical-sizing: auto;
#             font-size: 20px;
#             font-weight: 700;
#             font-style: normal;
#             font-variation-settings:
#             "slnt" 0,
#             "CASL" 0,
#             "CRSV" 0.5,
#             "MONO" 0;
#         }
#         .fonnt2{
#             font-family: "Recursive", sans-serif;
#             font-optical-sizing: auto;
#             font-weight: 400;
#             font-style: normal;
#             font-variation-settings:
#             "slnt" 0,
#             "CASL" 0,
#             "CRSV" 0.5,
#             "MONO" 0;
#         }
#         """
#         st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
#         st.markdown('<div style="position: relative;">', unsafe_allow_html=True)
#         for card in cards:
#             st.markdown(f"<div class='glass-morphism-card'>{card}</div>", unsafe_allow_html=True)
#         st.markdown('</div>', unsafe_allow_html=True)
#         st.markdown('</div>', unsafe_allow_html=True)

#     def main():
#         video_url = "https://cdn.discordapp.com/attachments/1232741156664774700/1245097026887090176/Gen-2_1615789569_generate_a_video_whe_vidjpg_M_5.mp4?ex=66578277&is=665630f7&hm=2d86cf7ffc04734a87041c6a6af02f0be089e3cb95f9edd98d739c671ab0b0ff&"
#         display_video_background(video_url)
#         display_animated_text("CryptoSphere")
#         display_glass_card(
#             "<div><p class='fonnt'>CryptoSphere</p><p class='fonnt2'>Welcome to CryptoSphere, where we are revolutionizing the cryptocurrency landscape through cutting-edge technology and innovative solutions. Our platform provides real-time data, ensuring you have access to the latest market trends, price movements, and crucial metrics. With comprehensive visualizations, we transform complex information into easily understandable charts and graphs, facilitating informed decision-making. Our live news updates keep you abreast of the latest developments in the cryptocurrency world, from regulatory changes and technological advancements to market shifts and significant events. Additionally, our integrated chatbot offers instant support and answers to your queries, enhancing your user experience. One of our standout features is our predictive analytics, leveraging sophisticated algorithms and machine learning to forecast future trends and investment opportunities, giving you a strategic edge in the dynamic world of digital assets. At CryptoSphere, we are dedicated to empowering our users with unparalleled insights and tools, helping you navigate the complexities of the cryptocurrency market and make well-informed decisions. Join us as we reshape the future of digital finance.</p></div>"
#         )

#     if __name__ == "__main__":
#         main()

#     def toggle_sidebar():
#         is_expanded = not st.session_state.sidebar_expanded
#         st.session_state.sidebar_expanded = is_expanded

#     if 'sidebar_expanded' not in st.session_state:
#         st.session_state.sidebar_expanded = False

#     col1, col2, col3 = st.columns(3)
#     with col2:
#         button_container = st.empty()
#         with button_container.container():
#             if st.button("🔑 Login or Register", use_container_width=True, type="primary"):
#                 toggle_sidebar()

#     if st.session_state.sidebar_expanded:
#         with st.sidebar:
#             selected = option_menu("Register/Login", ["Register", 'Login', 'Logout'], 
#                                     icons=['box-arrow-in-right', 'door-open-fill', 'box-arrow-in-left'], 
#                                     menu_icon="file-person-fill",
#                                     styles={
#                                         "container": {"padding": "5!important", "background-color": 'black'},
#                                         "icon": {"color": "white", "font-size": "15px"},
#                                         "nav-link": {"color": "white", "font-size": "15px", "text-align": "left", "margin": "0px", "width": "100%"},
#                                         "nav-link-hover": {"background-color": "#200736"},
#                                         "nav-link-selected": {"background-color": "#200736"}
#                                     })
#         if selected == "Register":
#             with st.sidebar:
#                 try:
#                     (email_of_registered_user, username_of_registered_user, name_of_registered_user) = authenticator.register_user(pre_authorization=False)
#                     if email_of_registered_user:
#                         st.success('User registered successfully!!')
#                         st.markdown('<h6 style="color:White; font-size: 16px"> **you can go to the login page and enter the site</h6>', unsafe_allow_html=True)
#                 except RegisterError as e:
#                     st.error(e)
#         if selected == "Login":
#             with st.sidebar:
#                 try:
#                     authenticator.login()
#                 except LoginError as e:
#                     st.error(e)
#                 if st.session_state["authentication_status"]:
#                     st.markdown('<h6 style="color:#0add08; font-size: 17px">The user has logged in, you can enter the site now!!</h6>', unsafe_allow_html=True)
#                     if st.button("Double click to enter the site!", use_container_width=True):
#                         st.session_state.current_function = "page2"
#                         flag = 1
#                 elif st.session_state["authentication_status"] is False:
#                     st.error('Username/password is incorrect')
#         if selected == "Logout":
#             with st.sidebar:
#                 if st.session_state["authentication_status"]:
#                     with st.container(border=True):
#                         st.subheader('Logout')
#                         st.checkbox(f'Are you sure you want to log out, {st.session_state["name"]}?', key='verify_logout')
#                         if st.session_state.verify_logout:
#                             authenticator.logout()
#                 else:
#                     st.success("User is logged out")

#     with open('config_new.yaml', 'w', encoding='utf-8') as file:
#         yaml.dump(config, file, default_flow_style=False)

#     try:
#         if flag == 1:
#             page2()
#     except Exception as e:
#         print(e)

# def main():
#     if "current_function" not in st.session_state:
#         st.session_state.current_function = "page1"
#     if st.session_state.current_function == "page1":
#         page1()
#     elif st.session_state.current_function == "page2":
#         if st.session_state["authentication_status"]:
#             page2()
#         else:
#             page1()

# if __name__ == "__main__":
#     main()
