import streamlit as st
import psycopg2

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

# Streamlit app
def main():
    st.set_page_config(page_title="ORBT-LEARN", layout="wide")

    # Custom CSS for styling
    st.markdown("""
        <style>
            /* Styling for the ORBT-LEARN heading */
            h1 {
                text-align: center;
                color: #2E86C1;
                font-family: 'Arial', sans-serif;
                font-size: 2.5em;
                margin-bottom: 20px;
            }

            /* Styling for buttons */
            .stButton>button {
                width: 100%;
                padding: 10px;
                margin: 5px 0;
                border-radius: 5px;
                border: 2px solid #2E86C1;
                background-color: transparent;
                color: #2E86C1;
                font-size: 16px;
                transition: all 0.3s ease;
            }

            .stButton>button:hover {
                background-color: #2E86C1;
                color: white;
                border-color: #2E86C1;
            }

            /* Styling for the logout button */
            .logout-button {
                display: flex;
                justify-content: center;
                margin-top: 20px;
            }

            .logout-button>button {
                width: 200px;
                padding: 10px;
                border-radius: 5px;
                border: 2px solid #E74C3C;
                background-color: transparent;
                color: #E74C3C;
                font-size: 16px;
                transition: all 0.3s ease;
            }

            .logout-button>button:hover {
                background-color: #E74C3C;
                color: white;
                border-color: #E74C3C;
            }

            /* Styling for the "Know About Me" button */
            .know-about-me-button {
                position: fixed;
                bottom: 20px;
                right: 20px;
                z-index: 1000;
            }
            .know-about-me-button>button {
                padding: 8px 16px;
                border-radius: 5px;
                border: 2px solid #4CAF50;
                background-color: transparent;
                color: #4CAF50;
                font-size: 14px;
                transition: all 0.3s ease;
            }
            .know-about-me-button>button:hover {
                background-color: #4CAF50;
                color: white;
                border-color: #4CAF50;
            }
        </style>
    """, unsafe_allow_html=True)

    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'show_about_me' not in st.session_state:
        st.session_state['show_about_me'] = False

    # "Know About Me" button
    st.markdown('<div class="know-about-me-button">', unsafe_allow_html=True)
    if st.button("Know About Me"):
        st.session_state['show_about_me'] = not st.session_state['show_about_me']
    st.markdown('</div>', unsafe_allow_html=True)

    # Display "About Me" information if the button is clicked
    if st.session_state['show_about_me']:
        st.sidebar.markdown("### About Me")
        st.sidebar.write("""
            Hi there! 👋  
            I'm the creator of this app. Here's a little about me:
            - **Name**: John Doe
            - **Role**: Developer
            - **Hobbies**: Coding, Reading, Traveling
            - **Contact**: johndoe@example.com
        """)

    # Login page
    if not st.session_state['logged_in']:
        st.title("ORBT-LeARN")
        name = st.text_input("Name", key="name")
        email = st.text_input("Email", key="email")
        mobile = st.text_input("Mobile Number", key="mobile")

        if st.button("Login"):
            if name and email and mobile:
                try:
                    create_tables()
                    insert_user(name, email, mobile)
                    st.session_state['logged_in'] = True
                    st.success("Logged in successfully!")
                    st.rerun()
                except psycopg2.errors.UniqueViolation:
                    st.error("This email is already registered. Please use a different email.")
            else:
                st.error("Please fill in all fields.")

    # Main page after login
    else:
        st.title("Welcome to ORBT-LEARN")

        # Buttons arranged in 2 columns
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Education Learn"):
                st.write("Education Learn page will be added later.")
            if st.button("Job"):
                st.write("Job page will be added later.")

        with col2:
            if st.button("Podcast"):
                st.write("Podcast page will be added later.")
            if st.button("Travel Place"):
                st.write("Travel Place page will be added later.")

        # Logout button centered below
        st.markdown('<div class="logout-button">', unsafe_allow_html=True)
        if st.button("Logout", key="logout"):
            st.session_state['logged_in'] = False
            st.success("Logged out successfully!")
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
