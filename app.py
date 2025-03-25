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
        I'm sharing my story not because I was a topper or someone from iit iim college and earning in lakhs or have any business and owend a company , but because I made many mistakes in my educational choices.  
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

            **Gradutaion Story**
            After scoring 68% in +2 (Science) and securing 1st division, I was unsure about my career path. Unlike after 10th grade—where there are clear options like diploma, ITI, or continuing +2—after +2, I only knew about B.Tech and +3 (Bachelor's degree).

My two elder brothers had done diploma in engineering (electrical/mechanical) and understood the work pressure in those fields. They advised me to pursue +3 (graduation) and prepare for government jobs. At the time, I had some interest in civil engineering because I heard it had good earning potential. But the funny thing was—I had no idea about entrance exams like JEE, defence tests (NDA, CDS), or other competitive exams. My only plan was: complete +3 → do B.Ed → become a high school teacher.

Later, a college offered me admission in BCA (Bachelor of Computer Applications), but I rejected it because I had zero knowledge about computer science or programming. In my village, I only knew 3-4 developers, but I learned about their careers much later.

I ended up joining +3 at Binayak Acharya College (a government college). But like many students there, I rarely attended classes seriously—just played games, wasted time, and didn't prepare for any exams. My brothers kept telling me to study from 1st/2nd year so I could crack government exams, but I always said "yes" and never acted on it.

Finally, I completed graduation with 62%, realizing too late that I had made another big mistake by not taking my future seriously.


    **B.Ed story**

    After completing +3 (graduation), my brothers advised me to either pursue B.Ed or a PG (Post-Graduation). I tried for B.Ed and gave the government entrance exam, but I failed. By then, the admission process for PG courses had also closed.

Around that time, a relative of mine was doing B.Ed in Special Education. When I asked if I could join the same, he said yes. I discussed it with my brothers, and they agreed—though the downside was that they always let me do whatever I wanted without much guidance.

I joined the course, but the college didn't provide proper certification. It was a special B.Ed program meant for teaching students with disabilities or mental rehabilitation, but none of us actually planned to work in that field. We just wanted to complete the degree, get the certificate, and use it for government job exams. The college assured us that the government would accept our certificates, so I went ahead with it.

Eventually, I completed B.Ed and gave the government entrance exam twice but couldn't clear it. Frustrated, I shifted my focus to other government job exams. I started applying, giving tests, and scoring decent marks.

My First Success: Clearing the Constable Exam
After multiple attempts, I finally cleared a constable recruitment exam in the 3rd round. The selection process was tough:

1st round: Selected candidates had to pass physical tests. Many failed.

2nd round: Another elimination round.

3rd round: I made it through and got selected!

I was overjoyed—finally, I had achieved something. My brothers were proud and encouraged me to prepare harder for bigger exams.

The Disappointment That Changed My Path
Later, I came across another recruitment notification for 1,133 posts, but the selection process was strange:

First, they shortlisted 9,352 candidates (8x the vacancies).

Then, they cut it down to half for the next round.

Finally, they called 2x the total posts (2,266 candidates) for document verification before selecting the final 1,133.

This felt like a lottery—selection was based on certificate verification rather than merit. Losing hope in the system, I stopped focusing on government exams.

A New Beginning: Discovering Data Science
Then, out of nowhere, I stumbled upon Data Science. It felt like my first real, self-driven decision—almost like a gift from God. This was the turning point where I took control of my career.

And now... my Data Science journey begins.


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
        {"name": "Somanath Temple", "location": "Veraval , Gujurat"},
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
        ##  !0 Questions With Experience Levels:
        
        ### 1. For Senior Data Scientists:
        -  How Got the job , When  and   overall Job Experince

        ### 2. For Mid-Level Professionals:
        
        ### 3. For Junior Professionals:

        - "Learning Machines " - Foundational concepts explained
    """)
    
    if st.button("Back to Dashboard"):
        st.session_state.show_podcast_page = False
        st.rerun()

def main():
    st.set_page_config(page_title="ORBT-LEARN", layout="wide")

    # Custom CSS for styling with medium round button
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
            .button-container {
                display: flex;
                justify-content: center;
                align-items: center;
                margin: 20px 0;
            }
            .round-button {
                border-radius: 50%;
                width: 150px;
                height: 150px;
                padding: 0;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 20px auto;
                background-color: #FF5733;
                color: white;
                border: 3px solid #FF5733;
                font-weight: bold;
                font-size: 20px;
                transition: all 0.3s ease;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                cursor: pointer;
            }
            .round-button:hover {
                background-color: #E64A19;
                border-color: #E64A19;
                transform: scale(1.05);
                box-shadow: 0 6px 12px rgba(0,0,0,0.3);
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
        # Create a container for the round button
        container = st.container()
        with container:
            # Use columns to center the button
            _, center_col, _ = st.columns([1, 2, 1])
            with center_col:
                # Use markdown to create a styled div that looks like a button
                st.markdown("""
                <div class="round-button" onclick="window.streamlitScriptRunner.runScript('My Mistakes')">
                    My Mistakes
                </div>
                """, unsafe_allow_html=True)
                
                # Add the actual button that will be triggered
                if st.button("My Mistakes", key="my_mistakes_button"):
                    st.session_state.show_story_page = True
                    st.rerun()

if __name__ == "__main__":
    main()
