import streamlit as st
import random
import time
import smtplib
from email.mime.text import MIMEText
from twilio.rest import Client

# Function to generate a random 6-digit OTP
def generate_otp():
    return str(random.randint(100000, 999999))

# Function to send OTP via email
def send_otp_email(email, otp):
    # SMTP configuration (replace with your email provider's details)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "your_email@gmail.com"  # Replace with your email
    sender_password = "your_email_password"  # Replace with your email password

    # Create the email message
    message = MIMEText(f"Your OTP for verification is: {otp}")
    message["Subject"] = "OTP Verification"
    message["From"] = sender_email
    message["To"] = email

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email, message.as_string())
        st.success("OTP sent to your email!")
    except Exception as e:
        st.error(f"Failed to send OTP via email: {e}")

# Function to send OTP via SMS using Twilio
def send_otp_sms(mobile, otp):
    # Twilio configuration (replace with your Twilio credentials)
    account_sid = "your_twilio_account_sid"  # Replace with your Twilio account SID
    auth_token = "your_twilio_auth_token"  # Replace with your Twilio auth token
    twilio_phone_number = "your_twilio_phone_number"  # Replace with your Twilio phone number

    try:
        # Initialize Twilio client
        client = Client(account_sid, auth_token)

        # Send SMS
        message = client.messages.create(
            body=f"Your OTP for verification is: {otp}",
            from_=twilio_phone_number,
            to=mobile
        )
        st.success("OTP sent to your mobile number!")
    except Exception as e:
        st.error(f"Failed to send OTP via SMS: {e}")

# Streamlit app
def main():
    st.set_page_config(page_title="OTP Verification System", layout="centered")

    # Custom CSS for styling
    st.markdown("""
        <style>
            .stTextInput>div>div>input {
                padding: 8px;
                border-radius: 5px;
                border: 1px solid #ccc;
                width: 100%;
            }
            .stButton>button {
                width: 100%;
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #ccc;
                background-color: #f0f2f6;
                color: #333;
                font-size: 16px;
                transition: all 0.3s ease;
            }
            .stButton>button:hover {
                background-color: #4CAF50;
                color: white;
                border-color: #4CAF50;
            }
        </style>
    """, unsafe_allow_html=True)

    # Initialize session state
    if 'otp' not in st.session_state:
        st.session_state['otp'] = None
    if 'email' not in st.session_state:
        st.session_state['email'] = None
    if 'mobile' not in st.session_state:
        st.session_state['mobile'] = None
    if 'verified' not in st.session_state:
        st.session_state['verified'] = False

    # Login and OTP verification page
    if not st.session_state['verified']:
        st.title("OTP Verification System")

        # Collect user details
        name = st.text_input("Enter your name:")
        email = st.text_input("Enter your email:")
        mobile = st.text_input("Enter your mobile number:")

        if st.button("Send OTP"):
            if name and email and mobile:
                # Generate OTP
                otp = generate_otp()
                st.session_state['otp'] = otp
                st.session_state['email'] = email
                st.session_state['mobile'] = mobile

                # Send OTP to email and mobile
                send_otp_email(email, otp)
                send_otp_sms(mobile, otp)
            else:
                st.error("Please fill in all fields.")

        # OTP input
        if st.session_state['otp']:
            otp_input = st.text_input("Enter OTP:")

            if st.button("Verify OTP"):
                if otp_input == st.session_state['otp']:
                    st.session_state['verified'] = True
                    st.success("OTP verified successfully!")
                    st.rerun()
                else:
                    st.error("Invalid OTP. Please try again.")

    # Main page after OTP verification
    else:
        st.title(f"Welcome, {st.session_state['email']}!")
        st.write("You have successfully logged in.")

        if st.button("Logout"):
            st.session_state['otp'] = None
            st.session_state['email'] = None
            st.session_state['mobile'] = None
            st.session_state['verified'] = False
            st.success("Logged out successfully!")
            st.rerun()

if __name__ == "__main__":
    main()
