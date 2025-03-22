import streamlit as st
import psycopg2
from streamlit_chat import message

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        "postgresql://neondb_owner:npg_nRWri4OJ5vcs@ep-solitary-waterfall-a575ahao-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require"
    )
    return conn

# Create tables if they don't exist
def create_tables():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            mobile TEXT NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

# Insert user data into the database
def insert_user(name, email, mobile):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email, mobile) VALUES (%s, %s, %s)", (name, email, mobile))
    conn.commit()
    cur.close()
    conn.close()

# Chatbot logic
def chatbot_response(user_input):
    # Simple echo chatbot for demonstration
    return f"You said: {user_input}"

# Streamlit app
def main():
    st.set_page_config(page_title="ORBT-LEARN", layout="wide")

    # Custom CSS for styling
    st.markdown("""
        <style>
            .stButton>button {
                width: 100%;
                padding: 10px;
                margin: 5px 0;
                border-radius: 5px;
                background-color: #4CAF50;
                color: white;
                font-size: 16px;
            }
            .stTextInput>div>div>input {
                padding: 10px;
                border-radius: 5px;
                border: 1px solid #ccc;
            }
            .stChatbox {
                position: fixed;
                bottom: 20px;
                right: 20px;
                width: 300px;
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
        </style>
    """, unsafe_allow_html=True)

    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'chatbot_open' not in st.session_state:
        st.session_state['chatbot_open'] = False
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # Login page
    if not st.session_state['logged_in']:
        st.title("ORBT-LEARN Login")
        name = st.text_input("Name")
        email = st.text_input("Email")
        mobile = st.text_input("Mobile Number")

        if st.button("Login"):
            if name and email and mobile:
                create_tables()
                insert_user(name, email, mobile)
                st.session_state['logged_in'] = True
                st.success("Logged in successfully!")
                st.experimental_rerun()
            else:
                st.error("Please fill in all fields.")

    # Main page after login
    else:
        st.title("Welcome to ORBT-LEARN")
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("Education Learn"):
                st.write("Education Learn page will be added later.")
        with col2:
            if st.button("Job"):
                st.write("Job page will be added later.")
        with col3:
            if st.button("Podcast"):
                st.write("Podcast page will be added later.")

        col4, col5, col6 = st.columns(3)

        with col4:
            if st.button("Motivation"):
                st.write("Motivation page will be added later.")
        with col5:
            if st.button("Travel Place"):
                st.write("Travel Place page will be added later.")
        with col6:
            if st.button("Logout"):
                st.session_state['logged_in'] = False
                st.success("Logged out successfully!")
                st.experimental_rerun()

        # Chatbot pop-up
        if st.button("Chatbot"):
            st.session_state['chatbot_open'] = not st.session_state['chatbot_open']

        if st.session_state['chatbot_open']:
            st.markdown("""
                <div class="stChatbox">
                    <h4>Chatbot</h4>
                    <div id="chat-container">
            """, unsafe_allow_html=True)

            user_input = st.text_input("You:", key="chat_input")
            if user_input:
                response = chatbot_response(user_input)
                st.session_state['chat_history'].append((user_input, response))

            for i, (user_msg, bot_msg) in enumerate(st.session_state['chat_history']):
                message(user_msg, is_user=True, key=f"user_{i}")
                message(bot_msg, key=f"bot_{i}")

            st.markdown("""
                    </div>
                </div>
            """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
