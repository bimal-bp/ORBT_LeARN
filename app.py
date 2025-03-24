import streamlit as st

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

            /* Custom styling for the "Know About Me" button */
            .green-button>button {
                background-color: #28a745; /* Green background */
                color: white;
                border: 2px solid #28a745; /* Green border */
            }

            .green-button>button:hover {
                background-color: #218838; /* Darker green on hover */
                border-color: #218838; /* Darker green border on hover */
            }

            /* Custom styling for the "Logout" button */
            .logout-button>button {
                background-color: #E74C3C; /* Red background */
                color: white;
                border: 2px solid #E74C3C; /* Red border */
            }

            .logout-button>button:hover {
                background-color: #C0392B; /* Darker red on hover */
                border-color: #C0392B; /* Darker red border on hover */
            }

            /* Centering the logout button */
            .logout-button {
                display: flex;
                justify-content: center;
                margin-top: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Initialize session state
    if 'show_story_page' not in st.session_state:
        st.session_state['show_story_page'] = False
    if 'show_job_page' not in st.session_state:
        st.session_state['show_job_page'] = False
    if 'show_education_page' not in st.session_state:
        st.session_state['show_education_page'] = False

    # If "Read Once" is clicked, show the story page
    if st.session_state.get('show_story_page'):
        show_story_page()
        return  # Stop rendering the rest of the app

    # If "Job" is clicked, show the job page
    if st.session_state.get('show_job_page'):
        st.title("Job Opportunities")
        st.markdown("### Explore Job Opportunities in Various Departments:")
        job_list = [
            "Sales and Marketing",
            "Finance and Accounting",
            "Human Resources (HR)",
            "Operations",
            "Customer Service",
            "IT and Technical Support",
            "Legal and Compliance",
            "Research and Development (R&D)",
            "Administration",
            "Supply Chain and Logistics"
        ]
        for job in job_list:
            st.write(f"- {job}")
        
        if st.button("Back to Dashboard"):
            st.session_state['show_job_page'] = False
            st.rerun()
        return

    # If "Education Learn" is clicked, show the education page
    if st.session_state.get('show_education_page'):
        st.title("Education and Learning")
        st.markdown("### Explore Educational Opportunities:")
        education_list = [
            "Data Science and Machine Learning",
            "Web Development",
            "Mobile App Development",
            "Digital Marketing",
            "Business Administration",
            "Graphic Design",
            "Cybersecurity",
            "Cloud Computing",
            "Artificial Intelligence",
            "Blockchain Technology"
        ]
        for education in education_list:
            st.write(f"- {education}")
        
        if st.button("Back to Dashboard"):
            st.session_state['show_education_page'] = False
            st.rerun()
        return

    # Main dashboard
    st.title("Learn & Earn")

    # Buttons arranged in 2 columns
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Education Learn"):
            st.session_state['show_education_page'] = True
            st.rerun()
        if st.button("Job"):
            st.session_state['show_job_page'] = True
            st.rerun()
        if st.button("Podcast"):
            st.write("Podcast page will be added later.")
        if st.button("Travel Place"):
            st.write("Travel Place page will be added later.")

    with col2:
        # "Know About Me" button with green color and green border
        st.markdown('<div class="green-button">', unsafe_allow_html=True)
        if st.button("Know About Me"):
            st.session_state['show_story_page'] = True
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
