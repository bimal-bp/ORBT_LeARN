import streamlit as st
def show_story_page():
    st.title(" About Me")
    
    # About Me Section
    st.markdown(""" 
        ### About Me
        Hi there! 👋  
        I'm the creator of this app. Here's a little about me:
        - **<span style='font-size: 20px;'>Bimal Patra</span>**
        - **Data Scientist at SG Group, Mumbai**
        - **bimalpatrap@gmail.com**
        - **9348245158**
    """, unsafe_allow_html=True)

    # Story Section
    st.markdown(""" 
        ### My Story
        Hi, my name is **Bimal Patra**, and I work as a **Data Scientist at SG Group in Mumbai**.  
        I'm not sharing this story because I was a 95% scorer, a topper, or someone earning 1 or 2 lakhs.  
        I'm sharing this because I've spent a lot of time studying the wrong things and choosing the wrong career paths in my life.  
        I just want to share this experience so that you don't make the same mistakes as I have.  

        **Go correct, work hard, live your life perfectly, and believe in God. That's all.**  
    """, unsafe_allow_html=True)

    # Initialize session state for full story if not exists
    if 'show_full_story' not in st.session_state:
        st.session_state.show_full_story = False

    # Button to toggle full story - with fixed variable name
    if st.button("Read Full Story"):
        st.session_state.show_full_story = not st.session_state.show_full_story
        st.rerun()  # Add this to immediately show the change

    # Display full story if toggled
    if st.session_state.show_full_story:
        st.markdown("""
            ### My Educational Journey
            
            **Early Education:**
            Hi, my name is Bimal Patra. My father's name is Tarini Charan Patra, and my mother's name is Sanjukta Patra. I have two elder brothers and one sister. My father was a retired Sanskrit teacher at Budhambo School.  

            I joined Budhambo High School and chose Sanskrit as an optional subject because it was easy, and I could write answers in my mother language, Odia. I completed my 10th grade at Budhambo High School, scoring 67%. During our exams, we got help from the teachers, and for those two years, the exam center was held in our own school. There were 50 MCQ questions, and by doing all these, I scored 67% and completed my 10th grade.  

            **After 10th Grade:**
            After 10th grade, I and my whole family knew that we had 3-5 course options based on my marks:  
            - Very low marks: ITI  
            - Very good marks: Doctor (so +2 Science)  
            - Low marks: Arts (no scope)  
            - Commerce and Diploma  

            I was an intelligent student, so my brother told me to go for Science. I was also okay with it. Some of my friends joined a summer course for +2 Science, but I didn't. I asked one friend what +2 Science was, and he said, "It's all in English. If you just remember 30 molecules from the periodic table, that's all for Chemistry. Physics is like 8th and 9th-grade books in English, and Math is just Math." I was okay with his explanation, so I finally joined +2 College with 3-4 friends, aiming to take Biology as an optional subject, which would help me prepare for medical studies.  

            But this was my first mistake because I am very poor at memorizing things. I have very good analytical knowledge, but I chose Biology and got low scores in it. However, I scored well in other subjects and completed my +2 with 68%. During this time, I played cricket, enjoyed myself, and didn't study properly. In the end, I just barely completed my 12th grade.  

            Now, the failure story starts because, till now, I didn't study properly. We will continue this story later.
        """)

    # Button to come back to the dashboard
    if st.button("Come Back to Dashboard"):
        st.session_state.show_story_page = False
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
            .know-about-me-button>button {
                background-color: #FF5733; /* Orange background */
                color: white;
                border: 2px solid #FF5733; /* Orange border */
                transition: all 0.3s ease;
            }

            .know-about-me-button>button:hover {
                background-color: #E64A19; /* Darker orange on hover */
                border-color: #E64A19; /* Darker orange border on hover */
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
    st.title(" **ORBT LeARN** ")
    st.title("LeARN & eARN ")

    # Buttons arranged in 2 columns
    col1, col2 = st.columns(2)

    with col1:
        if st.button("**Education Learn**"):
            st.session_state['show_education_page'] = True
            st.rerun()
        if st.button("**Job**"):
            st.session_state['show_job_page'] = True
            st.rerun()
        if st.button("Podcast"):
            st.write("Podcast page will be added later.")
        if st.button("Travel Place"):
            st.write("Travel Place page will be added later.")

    with col2:
        # "Know About Me" button with custom orange color
        st.markdown('<div class="know-about-me-button">', unsafe_allow_html=True)
        if st.button("My Mistakes"):
            st.session_state['show_story_page'] = True
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
