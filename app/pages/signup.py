from pages import ui

import streamlit as st
from pages.showroom import showroom
from pages.account_activation import (
    generate_token,
    account_activation,
    send_verification_token,
)
from utilities.db_conn import Session
from models import User
from models import Log
import pandas as pd

from sqlalchemy.sql import and_
from sqlalchemy.sql import or_
from sqlalchemy import func
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from pages.footnote import showHeader, showFooter

import bcrypt


def authenticate_signin():
    session = Session()
    res = False

    try:
        data = (
            session.query(User)
            .filter(or_(User.username == st.session_state.username, User.email == st.session_state.username))
            .one()
        )
        res = bcrypt.checkpw(st.session_state.password.encode("utf-8"), data.password)

    except (MultipleResultsFound, NoResultFound):
        pass

    if res is False:
        st.error("Incorrect username/email and/or password. Please try again.")
    else:
        st.session_state.activation_token = data.activation_token
        st.session_state.email = data.email
        st.session_state.username = data.username
        st.session_state.activated = data.is_activated

    session.close()
    return res


def authenticate_signup():
    session = Session()
    res = False
    warnmessage = ""

    try:
        (
            session.query(User)
            .filter(and_(User.username == st.session_state.username_signup))
            .one()
        )
        warnmessage = "Username already exists."
        st.error(warnmessage)

    except MultipleResultsFound:
        pass
    except NoResultFound:
        try:
            (
                session.query(User)
                .filter(and_(User.email == st.session_state.email))
                .one()
            )
            warnmessage = "Email already exists."
            st.error(warnmessage)

        except MultipleResultsFound:
            pass
        except NoResultFound:

            if st.session_state.username_signup == "":
                warnmessage = "Invalid username."
            elif st.session_state.password_signup == "":
                warnmessage = "Invalid password."
            elif st.session_state.firstname == "":
                warnmessage = "Invalid First Name."
            elif st.session_state.lastname == "":
                warnmessage = "Invalid Last Name."
            elif st.session_state.phonenumber == "":
                warnmessage = "Invalid Phone Number."
            elif st.session_state.email == "":
                warnmessage = "Invalid Email."
            elif st.session_state.organization == "":
                warnmessage = "Invalid Organization."
            elif st.session_state.industry == "-Select-":
                warnmessage = "Please select Industry."
            elif st.session_state.companysize == "-Select-":
                warnmessage = "Please select Company Size."
            elif st.session_state.department == "-Select-":
                warnmessage = "Please select Department."
            elif st.session_state.jobrole == "-Select-":
                warnmessage = "Please select Job Role."
            elif st.session_state.city == "":
                warnmessage = "Invalid City."
            elif st.session_state.country == "-Select-":
                warnmessage = "Please select Country."

            if warnmessage != "":
                st.error(warnmessage)

            else:
                __hashpw_signup = bcrypt.hashpw(
                    st.session_state.password_signup.encode("utf-8"), bcrypt.gensalt()
                )
                activation_token = generate_token(st.session_state.username_signup)
                session.add(
                    User(
                        username=st.session_state.username_signup,
                        password=__hashpw_signup,
                        firstname=st.session_state.firstname,
                        lastname=st.session_state.lastname,
                        phonenumber=st.session_state.phonenumber,
                        email=st.session_state.email,
                        organization=st.session_state.organization,
                        industry=st.session_state.industry,
                        companysize=st.session_state.companysize,
                        department=st.session_state.department,
                        jobrole=st.session_state.jobrole,
                        city=st.session_state.city,
                        country=st.session_state.country,
                        activation_token=activation_token,
                    )
                )
                session.commit()
                st.session_state.username = st.session_state.username_signup
                st.session_state.activation_token = activation_token
                res = True
    session.close()
    return res


def session_id():
    session = Session()
    try:
        max_id = (session.query(func.max(Log.session_id))).scalar()

        if max_id is not None:
            new_id = max_id + 1
        else:
            new_id = 1

    except Exception as e:
        pass
    session.close()
    return new_id


def redirect_signin():
    st.session_state.session_id = session_id()
    st.session_state.sidebar.render()
    st.session_state.sidebar.selected = "Data Science Showroom"
    showroom()


def signin():
    if st.session_state.authenticated is True:
        if st.session_state.activated is False:
            account_activation()
        else:
            redirect_signin()
    else:
        placeholder = st.empty()

        with placeholder.container():
            showHeader()
            showFooter()
            st.header("Sign In/ Sign Up")
            st.write("Sign up now to get trial access to our products!")

            tab1, tab2 = st.tabs(["Sign In", "Sign Up"])

            with tab1:
                st.write("Please enter your credentials.")
                col1, col2 = st.columns(2)

                with col1:
                    st.session_state.username = st.text_input("Username or email")

                with col2:
                    st.session_state.password = st.text_input(
                        "Password", type="password"
                    )

                btn_signin = st.button("Login")

            with tab2:

                ##Lookup tables
                BASE_PATH = 'app/data/lookup/'
                companysize = pd.read_csv(BASE_PATH+"companysize.csv")
                country = pd.read_csv(BASE_PATH+"country.csv")
                department = pd.read_csv(BASE_PATH+"department.csv")
                industry = pd.read_csv(BASE_PATH+"industry.csv")
                jobrole = pd.read_csv(BASE_PATH+"jobrole.csv")

                st.markdown("""#### Credentials""")
                col1, col2 = st.columns(2)
                with col1:
                    st.session_state.username_signup = st.text_input("Username ")

                with col2:
                    st.session_state.password_signup = st.text_input(
                        "Password ", type="password"
                    )

                st.markdown("""#### Contact Information""")
                col1, col2 = st.columns(2)
                with col1:
                    st.session_state.firstname = st.text_input("First Name")
                with col2:
                    st.session_state.lastname = st.text_input("Last Name")
                col1, col2 = st.columns(2)
                with col1:
                    st.session_state.phonenumber = st.text_input("Phone Number")
                with col2:
                    st.session_state.email = st.text_input("Email")

                st.markdown("""#### Company Information""")
                st.session_state.organization = st.text_input("Organization")

                contact1, contact2 = st.columns(2)
                with contact1:
                    st.session_state.industry = st.selectbox(
                        "Industry", ["-Select-"] + list(industry["industry"])
                    )
                    st.session_state.department = st.selectbox(
                        "Department", ["-Select-"] + list(department["department"])
                    )

                with contact2:
                    st.session_state.companysize = st.selectbox(
                        "Company Size", ["-Select-"] + list(companysize["companysize"])
                    )
                    st.session_state.jobrole = st.selectbox(
                        "Job Role", ["-Select-"] + list(jobrole["jobrole"])
                    )

                st.markdown("""#### Region Information""")
                col1, col2 = st.columns(2)
                with col1:
                    st.session_state.city = st.text_input("City")

                with col2:
                    st.session_state.country = st.selectbox(
                        "Country/Region", ["-Select-"] + list(country["country"])
                    )

                btn_signup = st.button("Sign Up")

            if btn_signin:
                st.session_state.authenticated = authenticate_signin()
            elif btn_signup:
                st.session_state.authenticated = authenticate_signup()

        if st.session_state.authenticated is True:
            placeholder.empty()
            if st.session_state.activated is False:
                send_verification_token()
                account_activation()
            else:
                redirect_signin()
