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

# Function to display the story and "About Me" on a new page
def show_story_page():
    st.title("My Story and About Me")
    
    # About Me Section
    st.markdown(""" 
        ### About Me
        Hi there! 👋  
        I'm the creator of this app. Here's a little about me:
        - **<span style='font-size: 20px;'>Bimal Patra</span>** <!-- Increased size -->
        - **Data Scientist at SG Group, Mumbai**
        - **bimalpatrap@gmail.com**
        - **9348245158**
    """, unsafe_allow_html=True)

    # Story Section
    st.markdown(""" 
        ### My Story
        Hi, my name is **Bimal Patra**, and I work as a **Data Scientist at SG Group in Mumbai**.  
        I’m not sharing this story because I was a 95% scorer, a topper, or someone earning 1 or 2 lakhs.  
        I’m sharing this because I’ve spent a lot of time studying the wrong things and choosing the wrong career paths in my life.  
        I just want to share this experience so that you don’t make the same mistakes as I have.  

        **Go correct, work hard, live your life perfectly, and believe in God. That’s all.**  

        Read the full story to gain knowledge.
    """, unsafe_allow_html=True)

    # Button to come back to the dashboard
    if st.button("Come Back to Dashboard"):
        st.session_state['show_story_page'] = False
        st.rerun()

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
                border: 2px solid #E74C3C; /* Red border for logout */
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

            /* Green color for the "Know About Me" button */
            .green-button>button {
                background-color: #28a745;
                color: white;
                border: 2px solid #3498DB; /* Blue border for Know About Me */
            }

            .green-button>button:hover {
                background-color: #218838;
                border-color: #3498DB; /* Blue border on hover */
            }
        </style>
    """, unsafe_allow_html=True)

    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'show_story_page' not in st.session_state:
        st.session_state['show_story_page'] = False

    # If "Read Once" is clicked, show the story page
    if st.session_state.get('show_story_page'):
        show_story_page()
        return  # Stop rendering the rest of the app

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
        st.title("Learn & Earn ")

        # Buttons arranged in 2 columns
        col1, col2 = st.columns(2)

        with col1:
            if st.button("Education Learn"):
                st.write("Education Learn page will be added later.")
            if st.button("Job"):
                st.write("Job page will be added later.")
            if st.button("Podcast"):
                st.write("Podcast page will be added later.")
            if st.button("Travel Place"):
                st.write("Travel Place page will be added later.")

        with col2:
            # "Know About Me" button with green color and blue border
            st.markdown('<div class="green-button">', unsafe_allow_html=True)
            if st.button("Know About Me"):
                st.session_state['show_story_page'] = True
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        # Logout button centered below with red border
        st.markdown('<div class="logout-button">', unsafe_allow_html=True)
        if st.button("Logout", key="logout"):
            st.session_state['logged_in'] = False
            st.session_state['show_story_page'] = False
            st.success("Logged out successfully!")
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
