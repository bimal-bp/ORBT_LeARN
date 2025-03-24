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
