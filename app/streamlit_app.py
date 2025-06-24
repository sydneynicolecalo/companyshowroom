import streamlit as st
from traceback import print_exc

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "activated" not in st.session_state:
    st.session_state.activated = False

st.set_page_config(
    page_title="MDI Novare Data Science Showroom",
    page_icon=r"app/images/cropped-logo_refresh-32x32.png",
    layout="centered",
)
    
with open(r"app/style.css") as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)


from pages import Sidebar
from pages.account_activation import decode_token, invalid_activation, valid_activation
from pages.signup import redirect_signin

if "session_sidebar" not in st.session_state:
    sidebar = Sidebar()
    #sidebar.render()
    st.session_state.sidebar = sidebar

data = st.experimental_get_query_params()

if (
    st.session_state.authenticated is False
    and data
    and isinstance(data, dict)
    and data.get("activation") is not None
):
    user, has_expired = decode_token(data["activation"][0])
    if user:
        if valid_activation(user, has_expired):
            if has_expired:
                invalid_activation(has_expired=has_expired)
            else:
                redirect_signin()
        else:
            # something went wrong while signing in the user
            print_exc()
            invalid_activation()
    else:        
        #print_exc()
        invalid_activation()
else:
    st.session_state.sidebar.render()
    st.session_state.sidebar.menu_options[st.session_state.sidebar.selected]["function"]()
    
from utilities.db_conn import Session
from models import Log

if st.session_state.authenticated is True and "session_id" in st.session_state:
    session = Session()
    session.add(
        Log(
            username=st.session_state.username,
            page=st.session_state.sidebar.selected,
            session_id=st.session_state.session_id,
        )
    )
    session.commit()
    session.close()