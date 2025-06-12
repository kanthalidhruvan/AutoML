# # import streamlit as st
# # import numpy as np
# # from multipage import MultiPage
# # from Pages import clf, intro, reg, ann, cnn
# # from auth import init_session_state, login_page, signup_page, go_to_signup, go_to_login

# # # Set page config
# # st.set_page_config(
# #     page_title="Enhanced AutoML Learning App",
# #     page_icon="🧊",
# #     layout="wide",
# #     initial_sidebar_state="expanded",
# #     menu_items={
# #         'Get Help': 'https://www.extremelycoolapp.com/help',
# #         'Report a bug': "https://www.extremelycoolapp.com/bug",
# #         'About': "# An Enhanced AutoML app"
# #     }
# # )

# # # Initialize session state for authentication
# # init_session_state()

# # # Create an instance of the app
# # app = MultiPage()

# # # Add all your application pages here
# # app.add_page("Introduction", intro.app)
# # app.add_page("Classification", clf.app)
# # app.add_page("Regression", reg.app)
# # app.add_page("ANN", ann.app)
# # app.add_page("CNN", cnn.app)

# # # Main logic: Authentication check
# # if not st.session_state.logged_in:
# #     if "page" not in st.session_state:
# #         st.session_state.page = "login"
# #     if st.session_state.page == "login":
# #         login_page()
# #     else:
# #         signup_page()
# # else:
# #     # Run the multi-page app if logged in
# #     app.run()

# #     # Logout button
# #     if st.button("Logout", key="logout_button"):
# #         st.session_state.logged_in = False
# #         st.session_state.username = ""
# #         st.rerun()
# import streamlit as st

# # Set page config - this MUST be the first Streamlit command
# #from here once again if error 
# st.set_page_config(
#     page_title="Enhanced AutoML Learning App",
#     page_icon="🧊",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     menu_items={
#         'Get Help': 'https://www.extremelycoolapp.com/help',
#         'Report a bug': "https://www.extremelycoolapp.com/bug",
#         'About': "# An Enhanced AutoML app"
#     }
# )

# # Now import other modules
# import numpy as np
# from multipage import MultiPage
# from Pages import clf, intro, reg, ann, cnn
# from auth import init_session_state, login_page, signup_page, go_to_signup, go_to_login

# # Initialize session state for authentication
# init_session_state()

# # Create an instance of the app
# app = MultiPage()

# # Add all your application pages here
# app.add_page("Introduction", intro.app)
# app.add_page("Classification", clf.app)
# app.add_page("Regression", reg.app)
# app.add_page("ANN", ann.app)
# app.add_page("CNN", cnn.app)

# # Main logic: Authentication check
# if not st.session_state.logged_in:
#     if "page" not in st.session_state:
#         st.session_state.page = "login"
#     if st.session_state.page == "login":
#         login_page()
#     else:
#         signup_page()
# else:
#     # Run the multi-page app if logged in
#     app.run()

#     # Logout button
#     if st.button("Logout", key="logout_button"):
#         st.session_state.logged_in = False
#         st.session_state.username = ""
#         st.rerun()
# import streamlit as st
# import numpy as np
# from multipage import MultiPage
# from Pages import clf, intro, reg, ann, cnn
# from auth import login_page, signup_page, go_to_signup, go_to_login

# # Set page config
# st.set_page_config(
#     page_title="Enhanced AutoML Learning App",
#     page_icon="🧊",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     menu_items={
#         'Get Help': 'https://www.extremelycoolapp.com/help',
#         'Report a bug': "https://www.extremelycoolapp.com/bug",
#         'About': "# An Enhanced AutoML app"
#     }
# )

# # Initialize session state for authentication
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False
# if "username" not in st.session_state:
#     st.session_state.username = ""
# if "page" not in st.session_state:
#     st.session_state.page = "login"

# # Create an instance of the app
# app = MultiPage()

# # Add all your application pages here
# app.add_page("Introduction", intro.app)
# app.add_page("Classification", clf.app)
# app.add_page("Regression", reg.app)
# app.add_page("ANN", ann.app)
# app.add_page("CNN", cnn.app)

# # Main logic: Authentication check
# if not st.session_state.logged_in:
#     if st.session_state.page == "login":
#         login_page()
#     else:
#         signup_page()
# else:
#     # Run the multi-page app if logged in
#     app.run()

#     # Logout button
#     if st.button("Logout", key="logout_button"):
#         st.session_state.logged_in = False
#         st.session_state.username = ""
#         st.rerun()
import streamlit as st

# Set page config as the first Streamlit command
st.set_page_config(
    page_title="Enhanced AutoML Learning App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# An Enhanced AutoML app"
    }
)

# Now import other modules and initialize logic
import numpy as np
from multipage import MultiPage
from Pages import clf, intro, reg, ann, cnn
from auth import login_page, signup_page, go_to_signup, go_to_login

# Initialize session state for authentication
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "page" not in st.session_state:
    st.session_state.page = "login"

# Create an instance of the app
app = MultiPage()

# Add all your application pages here
app.add_page("Introduction", intro.app)
app.add_page("Classification", clf.app)
app.add_page("Regression", reg.app)
app.add_page("ANN", ann.app)
app.add_page("CNN", cnn.app)

# Main logic: Authentication check
if not st.session_state.logged_in:
    if st.session_state.page == "login":
        login_page()
    else:
        signup_page()
else:
    # Run the multi-page app if logged in
    app.run()

    # Logout button
    if st.button("Logout", key="logout_button"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.rerun()