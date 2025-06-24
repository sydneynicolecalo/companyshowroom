import webbrowser
from pages.footnote import *

def contact_us():
    showHeader()
    st.title("Reach out to us!")
    st.write("Click [here](https://www.novare.com.hk/contact/) if you were not redirected to Contact us Page.")
    webbrowser.open("https://www.novare.com.hk/contact/")

    showFooter()
