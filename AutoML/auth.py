# import streamlit as st

# # Neon-themed CSS
# css = """
# <style>
#     .stApp {
#         background-color: #121212;
#         background-image: 
#             linear-gradient(to right, rgba(0, 255, 0, 0.1) 1px, transparent 1px),
#             linear-gradient(to bottom, rgba(0, 255, 0, 0.1) 1px, transparent 1px);
#         background-size: 80px 80px;
#     }
    
#     .main-container {
#         max-width: 400px;
#         margin: 0 auto;
#         padding-top: 80px;
#         text-align: center;
#     }
    
#     .neon-header {
#         color: #00FF00;
#         font-size: 36px;
#         font-weight: bold;
#         margin-bottom: 30px;
#         text-shadow: 0 0 15px rgba(0, 255, 0, 0.8);
#     }
    
#     div[data-baseweb="input"] input {
#         background-color: rgba(50, 50, 50, 0.7) !important;
#         color: white !important;
#         border: 2px solid rgba(0, 255, 0, 0.7) !important;
#         border-radius: 6px !important;
#         height: 55px !important;
#         margin-bottom: 15px !important;
#         padding-left: 15px !important;
#         font-size: 18px !important;
#     }

#     .button-container {
#         display: flex;
#         justify-content: center;
#         margin-top: 20px;
#     }

#     .neon-button {
#         background: linear-gradient(90deg, #00FF00, #00AA00);
#         color: black !important;
#         font-weight: bold !important;
#         width: 50% !important;
#         height: 60px !important;
#         border: none !important;
#         border-radius: 10px !important;
#         font-size: 20px !important;
#         text-transform: uppercase;
#         cursor: pointer !important;
#         transition: 0.4s ease-in-out !important;
#         box-shadow: 0 0 15px rgba(0, 255, 0, 0.7);
#     }

#     .neon-button:hover {
#         background: linear-gradient(90deg, #00AA00, #00FF00);
#         box-shadow: 0 0 25px rgba(0, 255, 0, 1);
#         transform: scale(1.05);
#     }

#     #MainMenu, footer, header {
#         visibility: hidden;
#     }
    
#     .regression-container {
#         padding: 20px;
#         background-color: rgba(30, 30, 30, 0.9);
#         border-radius: 10px;
#         box-shadow: 0 0 15px rgba(0, 255, 0, 0.3);
#         margin-top: 20px;
#     }
# </style>
# """

# # Apply CSS globally
# st.markdown(css, unsafe_allow_html=True)

# # Session state initialization (called in app.py)
# def init_session_state():
#     if "logged_in" not in st.session_state:
#         st.session_state.logged_in = False
#     if "username" not in st.session_state:
#         st.session_state.username = ""
#     if "users" not in st.session_state:
#         st.session_state.users = {"testuser": "testpass"}  # Simple user store

# def login_page():
#     st.markdown('<div class="main-container">', unsafe_allow_html=True)
#     st.markdown('<div class="neon-header">SIGN IN</div>', unsafe_allow_html=True)

#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
#     show_password = st.checkbox("Show Password")

#     if show_password:
#         password = st.text_input("Password", type="text", value=password)

#     st.markdown('<div class="button-container">', unsafe_allow_html=True)
#     col1, col2 = st.columns([1, 1])
    
#     with col1:
#         login_clicked = st.button("Login", key="login_button")

#     with col2:
#         signup_clicked = st.button("Sign Up", key="signup_button")

#     st.markdown('</div>', unsafe_allow_html=True)

#     if login_clicked:
#         if username in st.session_state.users and st.session_state.users[username] == password:
#             st.session_state.logged_in = True
#             st.session_state.username = username
#             st.success("Login successful!")
#             st.rerun()
#         else:
#             st.error("Invalid username or password.")

#     if signup_clicked:
#         go_to_signup()

#     st.markdown('</div>', unsafe_allow_html=True)

# def signup_page():
#     st.markdown('<div class="main-container">', unsafe_allow_html=True)
#     st.markdown('<div class="neon-header">SIGN UP</div>', unsafe_allow_html=True)

#     new_username = st.text_input("New Username")
#     new_email = st.text_input("Email")
#     new_password = st.text_input("Password", type="password")
#     confirm_password = st.text_input("Confirm Password", type="password")

#     st.markdown('<div class="button-container">', unsafe_allow_html=True)
#     col1, col2 = st.columns([1, 1])
    
#     with col1:
#         register_clicked = st.button("Register", key="register_button")

#     with col2:
#         back_to_login = st.button("Back to Login", key="back_to_login")

#     st.markdown('</div>', unsafe_allow_html=True)

#     if register_clicked:
#         if new_username and new_email and new_password and confirm_password:
#             if new_password == confirm_password:
#                 if new_username not in st.session_state.users:
#                     st.session_state.users[new_username] = new_password
#                     st.success("Registration successful! You can now log in.")
#                     go_to_login()
#                 else:
#                     st.error("Username already exists.")
#             else:
#                 st.error("Passwords do not match.")
#         else:
#             st.error("Please fill all fields.")

#     if back_to_login:
#         go_to_login()

#     st.markdown('</div>', unsafe_allow_html=True)

# def go_to_signup():
#     st.session_state.page = "signup"
#     st.rerun()

# def go_to_login():
#     st.session_state.page = "login"
#     st.rerun()
import streamlit as st
import sqlite3
import bcrypt

# Neon-themed CSS
css = """
<style>
    .stApp {
        background-color: #121212;
        background-image: 
            linear-gradient(to right, rgba(0, 255, 0, 0.1) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(0, 255, 0, 0.1) 1px, transparent 1px);
        background-size: 80px 80px;
    }
    
    .main-container {
        max-width: 400px;
        margin: 0 auto;
        padding-top: 80px;
        text-align: center;
    }
    
    .neon-header {
        color: #00FF00;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 30px;
        text-shadow: 0 0 15px rgba(0, 255, 0, 0.8);
    }
    
    div[data-baseweb="input"] input {
        background-color: rgba(50, 50, 50, 0.7) !important;
        color: white !important;
        border: 2px solid rgba(0, 255, 0, 0.7) !important;
        border-radius: 6px !important;
        height: 55px !important;
        margin-bottom: 15px !important;
        padding-left: 15px !important;
        font-size: 18px !important;
    }

    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }

    .neon-button {
        background: linear-gradient(90deg, #00FF00, #00AA00);
        color: black !important;
        font-weight: bold !important;
        width: 50% !important;
        height: 60px !important;
        border: none !important;
        border-radius: 10px !important;
        font-size: 20px !important;
        text-transform: uppercase;
        cursor: pointer !important;
        transition: 0.4s ease-in-out !important;
        box-shadow: 0 0 15px rgba(0, 255, 0, 0.7);
    }

    .neon-button:hover {
        background: linear-gradient(90deg, #00AA00, #00FF00);
        box-shadow: 0 0 25px rgba(0, 255, 0, 1);
        transform: scale(1.05);
    }

    #MainMenu, footer, header {
        visibility: hidden;
    }
    
    .regression-container {
        padding: 20px;
        background-color: rgba(30, 30, 30, 0.9);
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(0, 255, 0, 0.3);
        margin-top: 20px;
    }
</style>
"""

# # Apply CSS globally
# st.markdown(css, unsafe_allow_html=True)

# # Database setup
# def init_db():
#     conn = sqlite3.connect('users.db')
#     c = conn.cursor()
#     c.execute('''CREATE TABLE IF NOT EXISTS users
#                  (username TEXT PRIMARY KEY, email TEXT, password TEXT)''')
#     conn.commit()
#     conn.close()

# # Initialize database on module load
# init_db()

# def hash_password(password):
#     # Generate a salt and hash the password
#     salt = bcrypt.gensalt()
#     hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
#     return hashed

# def verify_password(password, hashed):
#     return bcrypt.checkpw(password.encode('utf-8'), hashed)

# def register_user(username, email, password):
#     conn = sqlite3.connect('users.db')
#     c = conn.cursor()
#     try:
#         c.execute("SELECT username FROM users WHERE username = ?", (username,))
#         if c.fetchone():
#             return False, "Username already exists."
#         hashed_password = hash_password(password)
#         c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, hashed_password))
#         conn.commit()
#         return True, "Registration successful! You can now log in."
#     except Exception as e:
#         return False, f"Error: {str(e)}"
#     finally:
#         conn.close()

# def login_user(username, password):
#     conn = sqlite3.connect('users.db')
#     c = conn.cursor()
#     try:
#         c.execute("SELECT password FROM users WHERE username = ?", (username,))
#         result = c.fetchone()
#         if result and verify_password(password, result[0]):
#             return True, "Login successful!"
#         return False, "Invalid username or password."
#     except Exception as e:
#         return False, f"Error: {str(e)}"
#     finally:
#         conn.close()

# def login_page():
#     st.markdown('<div class="main-container">', unsafe_allow_html=True)
#     st.markdown('<div class="neon-header">SIGN IN</div>', unsafe_allow_html=True)

#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")
#     show_password = st.checkbox("Show Password")

#     if show_password:
#         password = st.text_input("Password", type="text", value=password)

#     st.markdown('<div class="button-container">', unsafe_allow_html=True)
#     col1, col2 = st.columns([1, 1])
    
#     with col1:
#         login_clicked = st.button("Login", key="login_button")

#     with col2:
#         signup_clicked = st.button("Sign Up", key="signup_button")

#     st.markdown('</div>', unsafe_allow_html=True)

#     if login_clicked:
#         success, message = login_user(username, password)
#         st.write(message)
#         if success:
#             st.session_state.logged_in = True
#             st.session_state.username = username
#             st.rerun()

#     if signup_clicked:
#         go_to_signup()

#     st.markdown('</div>', unsafe_allow_html=True)

# def signup_page():
#     st.markdown('<div class="main-container">', unsafe_allow_html=True)
#     st.markdown('<div class="neon-header">SIGN UP</div>', unsafe_allow_html=True)

#     new_username = st.text_input("New Username")
#     new_email = st.text_input("Email")
#     new_password = st.text_input("Password", type="password")
#     confirm_password = st.text_input("Confirm Password", type="password")

#     st.markdown('<div class="button-container">', unsafe_allow_html=True)
#     col1, col2 = st.columns([1, 1])
    
#     with col1:
#         register_clicked = st.button("Register", key="register_button")

#     with col2:
#         back_to_login = st.button("Back to Login", key="back_to_login")

#     st.markdown('</div>', unsafe_allow_html=True)

#     if register_clicked:
#         if new_username and new_email and new_password and confirm_password:
#             if new_password == confirm_password:
#                 success, message = register_user(new_username, new_email, new_password)
#                 st.write(message)
#                 if success:
#                     go_to_login()
#             else:
#                 st.error("Passwords do not match.")
#         else:
#             st.error("Please fill all fields.")

#     if back_to_login:
#         go_to_login()

#     st.markdown('</div>', unsafe_allow_html=True)

# def go_to_signup():
#     st.session_state.page = "signup"
#     st.rerun()

# def go_to_login():
#     st.session_state.page = "login"
#     st.rerun()
import streamlit as st
import sqlite3
import bcrypt

# Neon-themed CSS
css = """
<style>
    .stApp {
        background-color: #121212;
        background-image: 
            linear-gradient(to right, rgba(0, 255, 0, 0.1) 1px, transparent 1px),
            linear-gradient(to bottom, rgba(0, 255, 0, 0.1) 1px, transparent 1px);
        background-size: 80px 80px;
    }
    
    .main-container {
        max-width: 400px;
        margin: 0 auto;
        padding-top: 80px;
        text-align: center;
    }
    
    .neon-header {
        color: #00FF00;
        font-size: 36px;
        font-weight: bold;
        margin-bottom: 30px;
        text-shadow: 0 0 15px rgba(0, 255, 0, 0.8);
    }
    
    div[data-baseweb="input"] input {
        background-color: rgba(50, 50, 50, 0.7) !important;
        color: white !important;
        border: 2px solid rgba(0, 255, 0, 0.7) !important;
        border-radius: 6px !important;
        height: 55px !important;
        margin-bottom: 15px !important;
        padding-left: 15px !important;
        font-size: 18px !important;
    }

    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }

    .neon-button {
        background: linear-gradient(90deg, #00FF00, #00AA00);
        color: black !important;
        font-weight: bold !important;
        width: 50% !important;
        height: 60px !important;
        border: none !important;
        border-radius: 10px !important;
        font-size: 20px !important;
        text-transform: uppercase;
        cursor: pointer !important;
        transition: 0.4s ease-in-out !important;
        box-shadow: 0 0 15px rgba(0, 255, 0, 0.7);
    }

    .neon-button:hover {
        background: linear-gradient(90deg, #00AA00, #00FF00);
        box-shadow: 0 0 25px rgba(0, 255, 0, 1);
        transform: scale(1.05);
    }

    #MainMenu, footer, header {
        visibility: hidden;
    }
    
    .regression-container {
        padding: 20px;
        background-color: rgba(30, 30, 30, 0.9);
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(0, 255, 0, 0.3);
        margin-top: 20px;
    }
</style>
"""

# Apply CSS globally
st.markdown(css, unsafe_allow_html=True)

# Database setup
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, email TEXT, password TEXT)''')
    conn.commit()
    conn.close()

# Initialize database on module load
init_db()

def hash_password(password):
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def register_user(username, email, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        c.execute("SELECT username FROM users WHERE username = ?", (username,))
        if c.fetchone():
            return False, "Username already exists."
        hashed_password = hash_password(password)
        c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, hashed_password))
        conn.commit()
        return True, "Registration successful! You can now log in."
    except Exception as e:
        return False, f"Error: {str(e)}"
    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    try:
        c.execute("SELECT password FROM users WHERE username = ?", (username,))
        result = c.fetchone()
        if result and verify_password(password, result[0]):
            return True, "Login successful!"
        return False, "Invalid username or password."
    except Exception as e:
        return False, f"Error: {str(e)}"
    finally:
        conn.close()

def login_page():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown('<div class="neon-header">SIGN IN</div>', unsafe_allow_html=True)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    
    with col1:
        login_clicked = st.button("Login", key="login_button")

    with col2:
        signup_clicked = st.button("Sign Up", key="signup_button")

    st.markdown('</div>', unsafe_allow_html=True)

    if login_clicked:
        success, message = login_user(username, password)
        st.write(message)
        if success:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.rerun()

    if signup_clicked:
        go_to_signup()

    st.markdown('</div>', unsafe_allow_html=True)

def signup_page():
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown('<div class="neon-header">SIGN UP</div>', unsafe_allow_html=True)

    new_username = st.text_input("New Username")
    new_email = st.text_input("Email")
    new_password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1])
    
    with col1:
        register_clicked = st.button("Register", key="register_button")

    with col2:
        back_to_login = st.button("Back to Login", key="back_to_login")

    st.markdown('</div>', unsafe_allow_html=True)

    if register_clicked:
        if new_username and new_email and new_password and confirm_password:
            if new_password == confirm_password:
                success, message = register_user(new_username, new_email, new_password)
                st.write(message)
                if success:
                    go_to_login()
            else:
                st.error("Passwords do not match.")
        else:
            st.error("Please fill all fields.")

    if back_to_login:
        go_to_login()

    st.markdown('</div>', unsafe_allow_html=True)

def go_to_signup():
    st.session_state.page = "signup"
    st.rerun()

def go_to_login():
    st.session_state.page = "login"
    st.rerun()