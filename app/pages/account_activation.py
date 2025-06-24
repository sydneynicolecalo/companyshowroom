from pages import ui

import datetime
import streamlit as st
import smtplib
import ssl
import jwt

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import BASE_URL, SECRET_KEY, SMTP_USERNAME, SMTP_PASSWORD

from pages.footnote import *

from utilities.db_conn import Session
from models import User
from sqlalchemy import update
from sqlalchemy.sql import and_
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from traceback import print_exc
from dateutil import tz


session = Session()

EMAIL_TEMPLATE = """
<!DOCTYPE html>
<html lang="en" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml">

<head>
    <title></title>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
    <meta content="width=device-width, initial-scale=1.0" name="viewport" />
    <style>
    * {{
        box-sizing: border-box;
    }}

    body {{
        margin: 0;
        padding: 0;
    }}

    a[x-apple-data-detectors] {{
        color: inherit !important;
        text-decoration: inherit !important;
    }}

    #MessageViewBody a {{
        color: inherit;
        text-decoration: none;
    }}

    p {{
        line-height: inherit
    }}

    .desktop_hide,
    .desktop_hide table {{
        mso-hide: all;
        display: none;
        max-height: 0px;
        overflow: hidden;
    }}

    @media (max-width:700px) {{
        .desktop_hide table.icons-inner {{
            display: inline-block !important;
        }}

        .icons-inner {{
            text-align: center;
        }}

        .icons-inner td {{
            margin: 0 auto;
        }}

        .row-content {{
            width: 100% !important;
        }}

        .mobile_hide {{
            display: none;
        }}

        .stack .column {{
            width: 100%;
            display: block;
        }}

        .mobile_hide {{
            min-height: 0;
            max-height: 0;
            max-width: 0;
            overflow: hidden;
            font-size: 0px;
        }}

        .desktop_hide,
        .desktop_hide table {{
            display: table !important;
            max-height: none !important;
        }}
    }}
    </style>
</head>

<body style="background-color: #e1f0f1; margin: 0; padding: 0; -webkit-text-size-adjust: none; text-size-adjust: none;">
    <table border="0" cellpadding="0" cellspacing="0" class="nl-container" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #e1f0f1;" width="100%">
        <tbody>
            <tr>
                <td>
                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 680px;" width="680">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
                                                    <table border="0" cellpadding="0" cellspacing="0" class="icons_block block-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                                                        <tr>
                                                            <td class="pad" style="vertical-align: middle; color: #000000; font-family: inherit; font-size: 14px; text-align: center; padding-top: 35px;">
                                                                <table align="center" cellpadding="0" cellspacing="0" class="alignment" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                                                                    <tr>
                                                                        <td style="vertical-align: middle; text-align: center; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px;"><img src="https://i.ibb.co/xhztFXr/mdinovarelogo.png" align="center" alt="Company Logo" class="icon" height="64" src="https://i.ibb.co/xhztFXr/mdinovarelogo.png" style="display: block; height: auto; margin: 0 auto; border: 0;" width="200" /></td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 680px;" width="680">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="16.666666666666668%">
                                                    <div class="spacer_block" style="height:10px;line-height:5px;font-size:1px;"> </div>
                                                </td>
                                                <td class="column column-2" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="66.66666666666667%">
                                                    <table border="0" cellpadding="0" cellspacing="0" class="heading_block block-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                                                        <tr>
                                                            <td class="pad" style="padding-left:10px;padding-right:10px;text-align:center;width:100%;padding-top:5px;">
                                                                <h1 style="margin: 0; color: #010101; direction: ltr; font-family: Arial, Helvetica Neue, Helvetica, sans-serif; font-size: 51px; font-weight: normal; letter-spacing: normal; line-height: 120%; text-align: center; margin-top: 0; margin-bottom: 0;"><strong>Activate your account</strong></h1>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table border="0" cellpadding="0" cellspacing="0" class="text_block block-3" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
                                                        <tr>
                                                            <td class="pad" style="padding-bottom:15px;padding-left:10px;padding-right:10px;padding-top:10px;">
                                                                <div style="font-family: sans-serif">
                                                                    <div class="txtTinyMce-wrapper" style="font-size: 14px; mso-line-height-alt: 21px; color: #393d47; line-height: 1.5; font-family: Arial, Helvetica Neue, Helvetica, sans-serif;">
                                                                        <p style="margin: 0; font-size: 14px; text-align: center; mso-line-height-alt: 24px;"><span style="font-size:16px;">Click on the link below to start using our showroom</span></p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                                <td class="column column-3" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="16.666666666666668%">
                                                    <div class="spacer_block" style="height:10px;line-height:5px;font-size:1px;"> </div>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-3" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 680px;" width="680">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
                                                    <table border="0" cellpadding="0" cellspacing="0" class="button_block block-1" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                                                        <tr>
                                                            <td class="pad" style="padding-bottom:70px;padding-left:10px;padding-right:10px;padding-top:10px;text-align:center;">
                                                                <div align="center" class="alignment"><a href="{activation_link}" style="text-decoration:none;display:inline-block;color:#010101;background-color:transparent;border-radius:4px;width:auto;border-top:1px solid #010101;font-weight:undefined;border-right:1px solid #010101;border-bottom:1px solid #010101;border-left:1px solid #010101;padding-top:5px;padding-bottom:5px;font-family:Arial, Helvetica Neue, Helvetica, sans-serif;text-align:center;mso-border-alt:none;word-break:keep-all;" target="_blank"><span style="padding-left:40px;padding-right:40px;font-size:16px;display:inline-block;letter-spacing:normal;"><span style="word-break: break-word; line-height: 32px;">Activate</span></span></a>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-4" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #010101;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 680px;" width="680">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; padding-top: 5px; padding-bottom: 5px; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="100%">
                                                    <div class="spacer_block" style="height:65px;line-height:65px;font-size:1px;"> </div>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-5" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #010101;" width="100%">
                        <tbody>
                            <tr>
                                <td>
                                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row-content stack" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; color: #000000; width: 680px;" width="680">
                                        <tbody>
                                            <tr>
                                                <td class="column column-1" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="33.333333333333336%">
                                                    <table border="0" cellpadding="0" cellspacing="0" class="icons_block block-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                                                        <tr>
                                                            <td class="pad" style="vertical-align: middle; color: #000000; font-family: inherit; font-size: 14px; padding-left: 10px; text-align: left; padding-top: 5px;">
                                                                <table align="left" cellpadding="0" cellspacing="0" class="alignment" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;">
                                                                    <tr>
                                                                        <td style="vertical-align: middle; text-align: center; padding-top: 5px; padding-bottom: 5px; padding-left: 5px; padding-right: 5px;"><img src="https://i.ibb.co/T2xDd9V/logo.png" align="center" alt="Company Logo" class="icon" height="64" src="https://i.ibb.co/T2xDd9V/logo.png" style="display: block; height: auto; margin: 0 auto; border: 0;" width="100" /></td>
                                                                    </tr>
                                                                </table>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table border="0" cellpadding="0" cellspacing="0" class="text_block block-3" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
                                                        <tr>
                                                            <td class="pad" style="padding-bottom:25px;padding-left:10px;padding-right:10px;padding-top:10px;">
                                                                <div style="font-family: sans-serif">
                                                                    <div class="txtTinyMce-wrapper" style="font-size: 14px; mso-line-height-alt: 25.2px; color: #fbfbfb; line-height: 1.8; font-family: Arial, Helvetica Neue, Helvetica, sans-serif;">
                                                                        <p style="margin: 0; font-size: 14px; text-align: left;">For over 30 years we have helped companies realize their growth potential.</p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                                <td class="column column-2" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="33.333333333333336%">
                                                    <table border="0" cellpadding="0" cellspacing="0" class="heading_block block-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                                                        <tr>
                                                            <td class="pad" style="padding-bottom:20px;padding-left:10px;padding-right:10px;text-align:center;width:100%;padding-top:5px;">
                                                                <h1 style="margin: 0; color: #ffffff; direction: ltr; font-family: Arial, Helvetica Neue, Helvetica, sans-serif; font-size: 18px; font-weight: normal; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0;"><strong>Links</strong></h1>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table border="0" cellpadding="0" cellspacing="0" class="text_block block-3" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
                                                        <tr>
                                                            <td class="pad" style="padding-bottom:20px;padding-left:10px;padding-right:10px;padding-top:10px;">
                                                                <div style="font-family: sans-serif">
                                                                    <div class="txtTinyMce-wrapper" style="font-size: 14px; mso-line-height-alt: 25.2px; color: #fbfbfb; line-height: 1.8; font-family: Arial, Helvetica Neue, Helvetica, sans-serif;">
                                                                        <p style="margin: 0; font-size: 14px; text-align: left;"><a href="https://www.mdi.net.ph/services-data-and-analytics/" rel="noopener" style="text-decoration: none; color: #ffffff;" target="_blank">Products</a></p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table border="0" cellpadding="0" cellspacing="0" class="text_block block-4" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
                                                        <tr>
                                                            <td class="pad" style="padding-bottom:20px;padding-left:10px;padding-right:10px;padding-top:10px;">
                                                                <div style="font-family: sans-serif">
                                                                    <div class="txtTinyMce-wrapper" style="font-size: 14px; mso-line-height-alt: 25.2px; color: #fbfbfb; line-height: 1.8; font-family: Arial, Helvetica Neue, Helvetica, sans-serif;">
                                                                        <p style="margin: 0; font-size: 14px; text-align: left;"><a href="https://www.mdi.net.ph/news/" rel="noopener" style="text-decoration: none; color: #ffffff;" target="_blank">Plans</a></p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table border="0" cellpadding="0" cellspacing="0" class="text_block block-5" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
                                                        <tr>
                                                            <td class="pad" style="padding-bottom:20px;padding-left:10px;padding-right:10px;padding-top:10px;">
                                                                <div style="font-family: sans-serif">
                                                                    <div class="txtTinyMce-wrapper" style="font-size: 14px; mso-line-height-alt: 25.2px; color: #fbfbfb; line-height: 1.8; font-family: Arial, Helvetica Neue, Helvetica, sans-serif;">
                                                                        <p style="margin: 0; font-size: 14px; text-align: left;"><a href="https://www.mdi.net.ph/contact/" rel="noopener" style="text-decoration: none; color: #ffffff;" target="_blank">Contact us</a></p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table border="0" cellpadding="0" cellspacing="0" class="text_block block-6" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; word-break: break-word;" width="100%">
                                                        <tr>
                                                            <td class="pad" style="padding-bottom:25px;padding-left:10px;padding-right:10px;padding-top:10px;">
                                                                <div style="font-family: sans-serif">
                                                                    <div class="txtTinyMce-wrapper" style="font-size: 14px; mso-line-height-alt: 25.2px; color: #fbfbfb; line-height: 1.8; font-family: Arial, Helvetica Neue, Helvetica, sans-serif;">
                                                                        <p style="margin: 0; font-size: 14px; text-align: left;"><a href="http://www.example.com" rel="noopener" style="text-decoration: none; color: #ffffff;" target="_blank">Unsubscribe</a></p>
                                                                    </div>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                                <td class="column column-3" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; font-weight: 400; text-align: left; vertical-align: top; border-top: 0px; border-right: 0px; border-bottom: 0px; border-left: 0px;" width="33.333333333333336%">
                                                    <table border="0" cellpadding="0" cellspacing="0" class="heading_block block-2" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                                                        <tr>
                                                            <td class="pad" style="padding-bottom:20px;padding-left:10px;padding-right:10px;text-align:center;width:100%;padding-top:5px;">
                                                                <h1 style="margin: 0; color: #ffffff; direction: ltr; font-family: Arial, Helvetica Neue, Helvetica, sans-serif; font-size: 18px; font-weight: normal; letter-spacing: normal; line-height: 120%; text-align: left; margin-top: 0; margin-bottom: 0;"><strong>Social Media</strong></h1>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                    <table border="0" cellpadding="0" cellspacing="0" class="social_block block-3" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt;" width="100%">
                                                        <tr>
                                                            <td class="pad" style="padding-bottom:15px;padding-left:10px;padding-right:10px;padding-top:10px;text-align:left;">
                                                                <div class="alignment" style="text-align:left;">
                                                                    <table border="0" cellpadding="0" cellspacing="0" class="social-table" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; display: inline-block;" width="144px">
                                                                        <tr>
                                                                            <td style="padding:0 4px 0 0;"><a href="https://www.facebook.com/mdinovare/" target="_blank"><img alt="Facebook" height="32" src="https://i.ibb.co/jfQP6k2/facebook2x.png" style="display: block; height: auto; border: 0;" title="facebook" width="32" /></a></td>
                                                                            <td style="padding:0 4px 0 0;"><a href="https://twitter.com/mdinovare/" target="_blank"><img alt="Twitter" height="32" src="https://i.ibb.co/HDrfTmC/twitter2x.png" style="display: block; height: auto; border: 0;" title="twitter" width="32" /></a></td>
                                                                            <td style="padding:0 4px 0 0;"><a href="https://ph.linkedin.com/company/mdinovare/" target="_blank"><img alt="Linkedin" height="32" src="https://i.ibb.co/LgtfvN4/linkedin2x.png" style="display: block; height: auto; border: 0;" title="linkedin" width="32" /></a></td>
                                                                            <td style="padding:0 4px 0 0;"><a href="https://www.instagram.com/mdinovare/" target="_blank"><img alt="Instagram" height="32" src="https://i.ibb.co/DCNBZT9/instagram2x.png" style="display: block; height: auto; border: 0;" title="instagram" width="32" /></a></td>
                                                                        </tr>
                                                                    </table>
                                                                </div>
                                                            </td>
                                                        </tr>
                                                    </table>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <table align="center" border="0" cellpadding="0" cellspacing="0" class="row row-6" role="presentation" style="mso-table-lspace: 0pt; mso-table-rspace: 0pt; background-color: #010101;" width="100%">
                    </table>
                </td>
            </tr>
        </tbody>
    </table>
</body>

</html>
"""


def generate_token(username):
    payload = {"username": username}
    payload["exp"] = datetime.datetime.now(
        tz=datetime.timezone.utc
    ) + datetime.timedelta(days=1)
    jwt_token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return jwt_token


def decode_token(encoded_jwt):
    res = {}
    expired = False
    try:
        res = jwt.decode(
            encoded_jwt, SECRET_KEY, algorithms=["HS256"], options={"verify_exp": False}
        )
        try:
            res = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=["HS256"])
            expired = "exp" not in res
        except jwt.ExpiredSignatureError:
            expired = True
    except Exception:
        print_exc()
    return res, expired


def send_verification_token():
    # Define the transport variables
    ctx = ssl.create_default_context()
    sender = SMTP_USERNAME  # Your e-mail address
    receiver = st.session_state.email  # Recipient's address

    # Create the message
    message = MIMEMultipart("alternative")
    message["Subject"] = "[MDI Novare DSA Showroom] Activate your account"
    message["From"] = sender
    message["To"] = receiver

    # HTML version
    activation_link = f"{BASE_URL}?activation={st.session_state.activation_token}"
    message.attach(
        MIMEText(EMAIL_TEMPLATE.format(activation_link=activation_link), "html")
    )

    # Connect with server and send the message
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=ctx) as server:
        server.login(sender, SMTP_PASSWORD)
        server.sendmail(sender, receiver, message.as_string())


def issue_new_token():
    res = False

    try:
        session = Session()
        data = (
            session.query(User).filter(User.username == st.session_state.username)
        ).one()
        data.activation_token = generate_token(st.session_state.username)
        session.commit()
        session.close()

        send_verification_token()
        res = True

    except (MultipleResultsFound, NoResultFound):
        print_exc()
    except Exception:
        print_exc()

    return res


def account_activation():
    st.session_state.sidebar.clear()
    showHeader()
    st.title("Email Activation for Members")
    st.write("Please check your email for the activation link")
    showFooter()


def invalid_activation(has_expired=False):
    st.session_state.sidebar.clear()
    showHeader()
    st.title("Email Activation for Members")
    if has_expired is True:
        st.write("This activation link has already expired.")
        st.button(
            "Email me a new activation link",
            help="Any previous activation link will be invalidated",
            on_click=issue_new_token,
        )
    else:
        st.write("There's been an issue activating your account.")
    st.write("You may reach out to us so we can further assist you.")
    showFooter()


def valid_activation(user, has_expired):

    res = False
    try:
        session = Session()
        data = (session.query(User).filter(User.username == user["username"])).one()
        data.is_activated = True
        session.commit()

        st.session_state.activation_token = data.activation_token
        st.session_state.email = data.email
        st.session_state.username = data.username

        st.session_state.authenticated = not has_expired
        st.session_state.activated = not has_expired
        res = True
        session.close()

    except (MultipleResultsFound, NoResultFound):
        print_exc()
    except Exception:
        print_exc()

    return res
