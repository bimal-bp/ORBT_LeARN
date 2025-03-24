import streamlit as st

def show_story_page():
    st.title("My Mistakes - Learning Journey")
    
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

    # Story Introduction
    st.markdown(""" 
        ### My Educational Journey
        Hi, my name is **Bimal Patra**, and I work as a **Data Scientist at SG Group in Mumbai**.  
        I'm sharing my story not because I was a topper, but because I made many mistakes in my educational choices.  
        I hope my experience helps you make better decisions.
    """, unsafe_allow_html=True)

    # Initialize session state for the full story
    if 'show_full_story' not in st.session_state:
        st.session_state.show_full_story = False

    # Button to toggle full story
    if st.button("Read Full Story"):
        st.session_state.show_full_story = not st.session_state.show_full_story
        st.rerun()

    # Full story content
    if st.session_state.show_full_story:
        st.markdown("""
            ### My Educational Journey
            
            **Family Background:**
            Hi, my name is Bimal Patra. My father's name is Tarini Charan Patra, and my mother's name is Sanjukta Patra. 
            I have two elder brothers and one sister. My father was a retired Sanskrit teacher at Budhambo School.  

            **10th Grade Experience:**
            I joined Budhambo High School and chose Sanskrit as an optional subject because it was easy, and I could write answers 
            in my mother language, Odia. I completed my 10th grade at Budhambo High School, scoring 67%. During our exams, we got 
            help from the teachers, and for those two years, the exam center was held in our own school. There were 50 MCQ questions, 
            and by doing all these, I scored 67% and completed my 10th grade.  

            **After 10th Grade Decisions:**
            After 10th grade, I and my whole family knew that we had 3-5 course options based on my marks:  
            - Very low marks: ITI  
            - Very good marks: Doctor (so +2 Science)  
            - Low marks: Arts (no scope)  
            - Commerce and Diploma  

            I was considered an intelligent student, so my brother told me to go for Science. I was also okay with it. Some of my 
            friends joined a summer course for +2 Science, but I didn't. I asked one friend what +2 Science was, and he said, 
            "It's all in English. If you just remember 30 molecules from the periodic table, that's all for Chemistry. Physics is 
            like 8th and 9th-grade books in English, and Math is just Math." I was okay with his explanation, so I finally joined 
            +2 College with 3-4 friends, aiming to take Biology as an optional subject, which would help me prepare for medical studies.  

            **My First Big Mistake:**
            This was my first mistake because I am very poor at memorizing things. I have very good analytical knowledge, but I chose 
            Biology and got low scores in it. However, I scored well in other subjects and completed my +2 with 68%. During this time, 
            I played cricket, enjoyed myself, and didn't study properly. In the end, I just barely completed my 12th grade.  

            **The Turning Point:**
            Now, the failure story starts because, till now, I didn't study properly. This pattern continued in my higher education 
            as well, where I struggled due to poor foundational knowledge and wrong subject choices. However, I eventually discovered 
            my passion for data science, where my analytical skills could shine.
            
            **Lesson Learned:**
            The key lesson from my journey is to understand your strengths and weaknesses before making educational choices. 
            Just because a field seems prestigious or others are doing it doesn't mean it's right for you. 
            Find what you're good at and passionate about, then pursue that with dedication.
        """)

    # Button to return to dashboard
    if st.button("Back to Dashboard"):
        st.session_state.show_story_page = False
        st.rerun()

def show_travel_page():
    st.title("Famous Travel Destinations in India")
    st.markdown("## Explore these beautiful destinations across India:")
    
    destinations = [
        {"name": "Ram Janmabhumi Temple", "location": "Ayodhya, Uttar Pradesh"},
        {"name": "Taj Mahal", "location": "Agra, Uttar Pradesh"},
        {"name": "Qutub Minar", "location": "New Delhi"},
        {"name": "Gateway of India", "location": "Mumbai, Maharashtra"},
        {"name": "Jaipur City Palace", "location": "Jaipur, Rajasthan"},
        {"name": "Kerala Backwaters", "location": "Kerala"},
        {"name": "Meghalaya - Cherrapunji", "location": "Cherrapunji, Meghalaya"},
        {"name": "Red Fort", "location": "New Delhi"},
        {"name": "Leh-Ladakh", "location": "Jammu & Kashmir"},
        {"name": "Ranthambore National Park", "location": "Sawai Madhopur, Rajasthan"}
    ]
    
    for idx, place in enumerate(destinations, 1):
        st.markdown(f"""
        ### {idx}. {place['name']}
        **Location:** {place['location']}
        """)
        st.write("---")
    
    if st.button("Back to Dashboard"):
        st.session_state.show_travel_page = False
        st.rerun()

def show_podcast_page():
    st.title("Podcast Recommendations")
    st.markdown("""
        ## Data Science Podcasts for Different Experience Levels:
        
        ### 1. For Senior Data Scientists:
        - "Data Skeptic" - Advanced topics in ML and statistics
        - "TWIML AI" - Interviews with industry leaders
        
        ### 2. For Mid-Level Professionals:
        - "DataFramed" - Practical applications of data science
        - "Super Data Science" - Career growth and technical skills
        
        ### 3. For Junior Professionals:
        - "Data Science Imposters" - For beginners in the field
        - "Learning Machines 101" - Foundational concepts explained
    """)
    
    if st.button("Back to Dashboard"):
        st.session_state.show_podcast_page = False
        st.rerun()

def main():
    st.set_page_config(page_title="ORBT-LEARN", layout="wide")

    # Custom CSS for styling
    st.markdown(""" 
        <style>
            h1 {
                text-align: center;
                color: #2E86C1;
                font-family: 'Arial', sans-serif;
                font-size: 2.5em;
                margin-bottom: 20px;
            }
            .stButton>button {
                width: 100%;
                padding: 10px;
                margin: 5px 0;
                border-radius: 8px;
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
            .mistakes-button>button {
                background-color: #FF5733;
                color: white;
                border: 2px solid #FF5733;
            }
            .mistakes-button>button:hover {
                background-color: #E64A19;
                border-color: #E64A19;
            }
            .logout-button>button {
                background-color: #E74C3C;
                color: white;
                border: 2px solid #E74C3C;
            }
            .logout-button>button:hover {
                background-color: #C0392B;
                border-color: #C0392B;
            }
            .logout-button {
                display: flex;
                justify-content: center;
                margin-top: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Initialize session states
    session_vars = [
        'show_story_page', 'show_job_page', 
        'show_education_page', 'show_travel_page',
        'show_podcast_page'
    ]
    for var in session_vars:
        if var not in st.session_state:
            st.session_state[var] = False

    # Page routing
    if st.session_state.show_story_page:
        show_story_page()
        return
    if st.session_state.show_job_page:
        st.title("Job Opportunities")
        st.markdown("### Explore Job Opportunities in Various Departments:")
        for job in [
            "Sales and Marketing", "Finance and Accounting", "Human Resources (HR)",
            "Operations", "Customer Service", "IT and Technical Support",
            "Legal and Compliance", "Research and Development (R&D)",
            "Administration", "Supply Chain and Logistics"
        ]:
            st.write(f"- {job}")
        if st.button("Back to Dashboard"):
            st.session_state.show_job_page = False
            st.rerun()
        return
    if st.session_state.show_education_page:
        st.title("Education and Learning")
        st.markdown("### Explore Educational Opportunities:")
        for education in [
            "Data Science and Machine Learning", "Web Development",
            "Mobile App Development", "Digital Marketing",
            "Business Administration", "Graphic Design",
            "Cybersecurity", "Cloud Computing",
            "Artificial Intelligence", "Blockchain Technology"
        ]:
            st.write(f"- {education}")
        if st.button("Back to Dashboard"):
            st.session_state.show_education_page = False
            st.rerun()
        return
    if st.session_state.show_travel_page:
        show_travel_page()
        return
    if st.session_state.show_podcast_page:
        show_podcast_page()
        return

    # Main dashboard
    st.title("ORBT LeARN")
    st.title("LeARN & eARN")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("**Education Learn**"):
            st.session_state.show_education_page = True
            st.rerun()
        if st.button("**Job**"):
            st.session_state.show_job_page = True
            st.rerun()
        if st.button("Podcast"):
            st.session_state.show_podcast_page = True
            st.rerun()
        if st.button("Travel Place"):
            st.session_state.show_travel_page = True
            st.rerun()

    with col2:
        # "My Mistakes" button with custom styling
        st.markdown('<div class="mistakes-button">', unsafe_allow_html=True)
        if st.button("My Mistakes"):
            st.session_state.show_story_page = True
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

        # Other buttons can go here
        st.button("Other Option 1")
        st.button("Other Option 2")

    # Logout button at the bottom
    st.markdown('<div class="logout-button">', unsafe_allow_html=True)
    if st.button("Logout"):
        st.write("Logout functionality would go here")
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
