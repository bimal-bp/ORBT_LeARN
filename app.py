import streamlit as st

def show_story_page():
    st.title("My Mistakes ")
    
    # About Me Section
    st.markdown(""" 
        ### About Me
        Hi there! 👋  
        I'm the creator of this app. Here's a little about me:
        - **<span style='font-size: 20px;'>Bimal Patra</span>**
        - **Data Scientist( AI/ML) - SG Group, Mumbai**
        - **bimalpatrap@gmail.com**
        - **9348245158**
    """, unsafe_allow_html=True)

    # Story Introduction
    st.markdown(""" 
        ### Short Summary
        Hi, my name is **Bimal Patra**, and I work as a **Data Scientist at SG Group in Mumbai**.  
        -  I'm sharing my story not because I was a topper or someone from IIT/IIM college 
        - and earning in lakhs or have any business and owend a company ,

        but because I made many mistakes in my educational choices & dont do correct things in right time .  
        I hope my experience helps you make better decisions.
    """, unsafe_allow_html=True)

    # Initialize session state for the full story
    if 'show_full_story' not in st.session_state:
        st.session_state.show_full_story = False

    # Button to toggle full story
    if st.button("Read Full Story"):
        st.session_state.show_full_story = not st.session_state.show_full_story
        st.rerun()

    if st.session_state.show_full_story:
        st.markdown("""
            ## My Educational Journey

            ### Family Background
            Hi, my name is Bimal Patra. My father's name is Tarini Charan Patra, and my mother's name is Sanjukta Patra. 
            I have two elder brothers and one sister. My father was a retired Sanskrit teacher at Budhambo School.

            ### 10th Grade Experience
            I joined Budhambo High School and chose Sanskrit as an optional subject because it was easy, and I could write answers 
            in my mother language, Odia. I completed my 10th grade at Budhambo High School, scoring 67%. During our exams, we got 
            help from the teachers, and for those two years, the exam center was held in our own school. There were 50 MCQ questions, 
            and by doing all these, I scored 67% and completed my 10th grade.

            ### After 10th Grade Decisions
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

            ### My First Big Mistake
            This was my first mistake because I am very poor at memorizing things. I have very good analytical knowledge, but I chose 
            Biology and got low scores in it. However, I scored well in other subjects and completed my +2 with 68%. During this time, 
            I played cricket, enjoyed myself, and didn't study properly. In the end, I just barely completed my 12th grade.

            ### The Turning Point
            Now, the failure story starts because, till now, I didn't study properly. This pattern continued in my higher education 
            as well, where I struggled due to poor foundational knowledge and wrong subject choices. However, I eventually discovered 
            my passion for data science, where my analytical skills could shine.

            ### Graduation Story
            After scoring 68% in +2 (Science) and securing 1st division, I was unsure about my career path. Unlike after 10th grade—where there are clear options like diploma, ITI, or continuing +2—after +2, I only knew about B.Tech and +3 (Bachelor's degree).

            My two elder brothers had done diploma in engineering (electrical/mechanical) and understood the work pressure in those fields. They advised me to pursue +3 (graduation) and prepare for government jobs. At the time, I had some interest in civil engineering because I heard it had good earning potential. But the funny thing was—I had no idea about entrance exams like JEE, defence tests (NDA, CDS), or other competitive exams. My only plan was: complete +3 → do B.Ed → become a high school teacher.

            Later, a college offered me admission in BCA (Bachelor of Computer Applications), but I rejected it because I had zero knowledge about computer science or programming. In my village, I only knew 3-4 developers, but I learned about their careers much later.

            I ended up joining +3 at Binayak Acharya College (a government college). But like many students there, I rarely attended classes seriously—just played games, wasted time, and didn't prepare for any exams. My brothers kept telling me to study from 1st/2nd year so I could crack government exams, but I always said "yes" and never acted on it.

            Finally, I completed graduation with 62%, realizing too late that I had made another big mistake by not taking my future seriously.

            ### B.Ed Story
            After completing +3 (graduation), my brothers advised me to either pursue B.Ed or a PG (Post-Graduation). I tried for B.Ed and gave the government entrance exam, but I failed. By then, the admission process for PG courses had also closed.

            Around that time, a relative of mine was doing B.Ed in Special Education. When I asked if I could join the same, he said yes. I discussed it with my brothers, and they agreed—though the downside was that they always let me do whatever I wanted without much guidance.

            I joined the course, but the college didn't provide proper certification. It was a special B.Ed program meant for teaching students with disabilities or mental rehabilitation, but none of us actually planned to work in that field. We just wanted to complete the degree, get the certificate, and use it for government job exams. The college assured us that the government would accept our certificates, so I went ahead with it.

            Eventually, I completed B.Ed and gave the government entrance exam twice but couldn't clear it. Frustrated, I shifted my focus to other government job exams. I started applying, giving tests, and scoring decent marks.

            ### My First Success: Clearing the Constable Exam
            After multiple attempts, I finally cleared a constable recruitment exam in the 3rd round. The selection process was tough:

            1. 1st round: Selected candidates had to pass physical tests. Many failed.
            2. 2nd round: Another elimination round.
            3. 3rd round: I made it through and got selected!

            I was overjoyed—finally, I had achieved something. My brothers were proud and encouraged me to prepare harder for bigger exams.

            ### The Disappointment That Changed My Path
            Later, I came across another recruitment notification for 1,133 posts, but the selection process was strange:

            - First, they shortlisted 9,352 candidates (8x the vacancies)
            - Then, they cut it down to half for the next round
            - Finally, they called 2x the total posts (2,266 candidates) for document verification before selecting the final 1,133

            This felt like a lottery—selection was based on certificate verification rather than merit. Losing hope in the system, I stopped focusing on government exams.

            ### A New Beginning: Discovering Data Science
            Then, out of nowhere, I stumbled upon Data Science. It felt like my first real, self-driven decision—almost like a gift from God. This was the turning point where I took control of my career.

            ### My Data Science Journey Begins
            Before starting my data science journey, I asked a relative who was already in the field if it was a good career choice. He said yes, so I told my brothers that I wouldn't pursue a postgraduate degree (PG) and instead wanted to do data science. They had zero knowledge about the field—only that it was an IT-related job with a good salary package.

            I asked my brother for a laptop, and he inquired about the course fees. I explained that it was a "pay-after-placement" program, meaning I wouldn't have to pay upfront—the institute would provide a job first and then take payment later. However, they initially asked for ₹15,000 from everyone. Since I had already told my family I wouldn't need to pay anything at the start, I stopped my tuition classes and even dropped the idea of becoming a teacher.

            To arrange the payment, I borrowed money from two friends who helped me out. I joined the data science course, but before classes began, I only watched a 17-minute introductory video on Python. It took me 1 hour and 23 minutes to finish because I didn't even know how to type symbols like "@" or use function keys—I had to Google everything. My computer knowledge was practically zero, despite having a PGDCA certificate. In that course, I had only attended 10-12 classes for the basics—the rest of the time, I was busy traveling or playing cricket. In the end, I just got the certificate without learning much.

            Our live classes were held at night (8–10 PM or sometimes until 10:15 PM). Since I was staying alone at home, I didn't attend the initial Python classes properly, thinking I could just read the notes later. As a result, I gained zero knowledge in Python. Programming was completely new to me, and the concepts went over my head.

            A month passed, and we started SQL. This time, I paid a little more attention since writing queries felt easier. After SQL, we moved on to Excel. But around that time, I fell in love with a girl and traveled to another village to see her during a festival. Her parents caught us, but they didn't say anything to me directly. However, 2-3 months later, my brothers found out and called me to Kolkata, insisting I stay there and complete the course properly. I agreed.

            I had been living alone since my father passed away when I was in 7th grade, and my mother passed away when I was in 10th. After that, I stayed in a hostel for 12th grade, then moved to Berhampur for my +3 studies. Later, I completed my B.Ed from a college 10 km away from my village. Now, I'm in Kolkata, focusing on finishing my data science course.

            ### My Data Science Journey: Struggles and Realizations
            After moving to Kolkata, I stayed there for three months. Since I had already fallen behind in the initial stages of the course, I struggled to catch up. I had promised my brothers that I would complete data science in six months and land a job, but the course officially ended by late 2023. By then, I thought I could just revise interview questions and start applying—assuming I'd get a job immediately.

            From YouTube, I learned that deep learning was important for data scientists, so I watched Krish Naik's videos without fully understanding them. Later, I discovered MLOps and Gen AI, which were said to offer high-paying roles, so I tried learning those too—again, just by watching videos. Even now, my knowledge of ML, DL, and Gen AI is shaky, and I have no real projects to show. But I still held onto hope, thinking, "If I just study interview questions, I can land a 9 LPA job."

            I had chosen data science because of the high salary packages I saw on YouTube. I memorized around 100 questions from each subject (with a few topics still pending). Meanwhile, my brother suggested I return to the village to help with boring (installing a borewell). But since my girlfriend was there and I had visited 7-8 months earlier, I refused. I wanted a job first. I argued that I just needed 12-15 more days to finish interview prep before going.

            But when I finally went, I was too angry and distracted to study. For 20 days, I focused on house repairs and the borewell work instead of applying for jobs. By the time I returned, I didn't want to go back to Kolkata—my brothers restricted my freedom, and I resented being sent away.

            So, I decided to go to Hyderabad, where a friend, Ramahari, had offered support. I told my brothers I had an interview there, and they agreed. After arriving, I lied that I had been rejected in the second round and said I'd stay for 5-10 more days to try other companies.

            Then, my brother's roommate referred me for a walk-in interview at Wipro—my first ever. Somehow, I cleared the first round and excitedly told my brother and his roommate. They assured me, "The manager round is easy—you'll get the job!" But I was rejected in the second round.

            Later, I completed a couple of projects in Kolkata with a friend's help. Now, in Hyderabad, I've spent 16 months in data science with little progress. I watched more YouTube videos and realized I needed to practice programming questions, DSA, dynamic programming, and aptitude for technical rounds. I spent 2-3 months studying these, but my brother kept pushing me to attend walk-in interviews. I rarely went, sometimes making excuses like "I was rejected in the 3rd round" or "I didn't clear the first round."

            ### Current Situation
            After 18 months in data science, all I've done is watch YouTube videos and skim through interview questions—without a job or solid skills to show for it.

            ### Lesson Learned
            The key lesson from my journey is to understand your strengths and weaknesses before making educational choices. 
            Just because a field seems prestigious or others are doing it doesn't mean it's right for you. 
            Find what you're good at and passionate about, then pursue that with dedication.
        """, unsafe_allow_html=True)

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
    st.title("🎙 Career Insights Podcast")
    st.markdown("""
    *"Learn directly from top professionals across diverse fields - their journeys, challenges, and advice for students like you!"*""")

    # Introduction
    st.header("About the Podcast")
    st.markdown("""
    This podcast series brings you face-to-face with accomplished professionals from:
    - Technology (Data Scientists, AI Engineers, Software Developers)
    - Medicine (Doctors, Surgeons, Researchers)
    - Government Services (IAS, IPS, IFS officers)
    - Academia (IIT Professors, Top Researchers)
    - Corporate Leaders (CEOs, Entrepreneurs)
    - And many more exciting fields!
    
    Each episode features deep-dive conversations about their career paths, daily work, and actionable advice.
    """)

    # Podcast Format
    st.header("Episode Format")
    st.subheader("12 Essential Questions We Ask Every Expert:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **1. Career Introduction**  
        "Can you introduce yourself and describe your current role?"  
        
        **2. Career Journey**  
        "What experiences led you to this position?"  
        
        **3. Educational Background**  
        "How did your education prepare you for this career?"  
        
        **4. Breaking Into the Field**  
        "What would you recommend to students wanting to enter this profession?"  
        
        **5. Daily Work Life**  
        "What does a typical day look like in your job?"  
        
        **6. Skills & Tools**  
        "What specific skills and tools are essential for your work?"  
        """)
    
    with col2:
        st.markdown("""
        **7. Challenges & Rewards**  
        "What's most challenging and rewarding about your work?"  
        
        **8. Career Motivation**  
        "How do you stay motivated in your career?"  
        
        **9. Key Advice**  
        "What one suggestion would you give aspiring professionals?"  
        
        **10. Early Mistakes**  
        "What mistakes did you make early on that others should avoid?"  
        
        **11. Work-Life Balance**  
        "How do you manage professional and personal life?"  
        
        **12. Future Trends**  
        "Where do you see this field heading in the next 5 years?"  
        """)

    # Featured Professionals Section
    st.header("🎧 Upcoming Episodes")
    
    tech = st.expander("💻 Technology Sector")
    with tech:
        st.markdown("""
        - **AI Research Lead** - The future of machine learning
        - **Senior Data Scientist** - How data drives entertainment
        - **Open Source Maintainer** - Building community software
        """)
    
    medicine = st.expander("🏥 Medical Field")
    with medicine:
        st.markdown("""
        - **Neurosurgeon** - Advances in surgical technology
        - **Public Health Researcher** - Pandemic response lessons
        """)
    
    govt = st.expander("🏛 Government Services")
    with govt:
        st.markdown("""
        - **IAS Officer** - Digital transformation in governance
        - **IPS Officer** - Cybercrime challenges
        - **Scientist @ ISRO** - India's space program
        """)
    
    academia = st.expander("🎓 Academia & Research")
    with academia:
        st.markdown("""
        - **IIT Professor** - Cutting-edge engineering research
        - **PhD Student @ MIT** - Life in top-tier academia
        - **Education Reformer** - Improving STEM education
        """)

    # Call to Action
    st.markdown("""
    ---
    ### Want to suggest a guest or topic?
    [Submit your suggestions here](#) (link to form)
    """)
    if st.button("← Back to Dashboard"):
        st.session_state.show_podcast_page = False
        st.rerun()

def show_education_page():
    st.title("Education and Learning")
    
    education_options = {
        "After 10th": {
            "Academic Streams": [
                "Science (PCM/PCB)", 
                "Commerce", 
                "Arts/Humanities"
            ],
            "Diploma Courses": [
                "Engineering (Mechanical/Civil/CS)", 
                "Hotel Management", 
                "Fashion Design",
                "Medical Lab Technology"
            ],
            "ITI/Vocational": [
                "Electrician", 
                "Fitter", 
                "Computer Operator",
                "Beautician"
            ],
            "Certifications": [
                "Digital Marketing", 
                "Graphic Design", 
                "Basic Programming"
            ]
        },
        "After 12th": {
            "Science Stream": [
                "BTech/BE (Engineering)", 
                "MBBS/BDS (Medical)", 
                "BSc (Physics/Chemistry/CS)",
                "BSc Agriculture"
            ],
            "Commerce Stream": [
                "BCom/BCom(Hons)", 
                "BBA", 
                "CA Foundation",
                "CS/CMA"
            ],
            "Arts/Humanities": [
                "BA (History/Psychology)", 
                "BJMC (Journalism)", 
                "BFA (Fine Arts)",
                "BA LLB (Law)"
            ],
            "Professional Courses": [
                "Diploma in Animation", 
                "Aviation Courses", 
                "Hotel Management",
                "NDA (Defense)"
            ]
        },
        "After Graduation": {
            "Higher Education": [
                "MTech/MS (Engineering)", 
                "MBA/PGDM", 
                "MSc (Sciences)",
                "PhD (Research)"
            ],
            "Government Exams": [
                "UPSC Civil Services", 
                "Banking (IBPS/RBI)", 
                "SSC CGL",
                "State PSCs"
            ],
            "Tech Certifications": [
                "Data Science (Python/R)", 
                "Cloud Computing (AWS/Azure)", 
                "Cybersecurity (CEH)",
                "AI/ML Certifications"
            ],
            "Creative Fields": [
                "UI/UX Design", 
                "Advanced Animation", 
                "Film Making",
                "Photography"
            ],
            "Study Abroad": [
                "MS in USA/Germany", 
                "MBA Abroad", 
                "PhD Scholarships",
                "Work-Study Programs"
            ]
        }
    }

    # Display education options
    selected_level = st.selectbox("Select Education Level", list(education_options.keys()))
    
    if selected_level:
        selected_category = st.selectbox("Choose Category", list(education_options[selected_level].keys()))
        
        if selected_category:
            st.markdown("### Available Options:")
            for option in education_options[selected_level][selected_category]:
                st.write(f"- {option}")

    if st.button("Back to Dashboard"):
        st.session_state.show_education_page = False
        st.rerun()

def show_job_page():
    st.title("Job Opportunities")
    st.markdown("### Explore Job Opportunities Across All Fields:")

    departments = {
        "Software Development & Engineering": [
            "Frontend Developer (React, Angular, Vue.js)",
            "Backend Developer (Node.js, Python, Java, .NET)",
            "Full-Stack Developer",
            "Mobile App Developer (iOS, Android, Flutter, React Native)",
            "Embedded Systems Engineer",
            "Game Developer (Unity, Unreal Engine)",
            "Blockchain Developer (Solidity, Web3)",
            "AR/VR Developer",
            "Cloud Engineer (AWS, Azure, GCP)",
            "DevOps Engineer (Docker, Kubernetes, CI/CD)",
            "Site Reliability Engineer (SRE)",
            "Low-Code/No-Code Developer (Power Platform, OutSystems)"
        ],
        
        "Data & AI/ML Roles": [
            "Data Scientist (Python, R, TensorFlow)",
            "Machine Learning Engineer",
            "AI Research Scientist (NLP, Computer Vision)",
            "Data Engineer (Spark, Hadoop, ETL)",
            "Data Analyst (SQL, Tableau, Power BI)",
            "Business Intelligence (BI) Analyst",
            "Big Data Architect",
            "Quantitative Analyst (Quant) (Finance + Data)"
        ],
        
        "Cybersecurity & Ethical Hacking": [
            "Cybersecurity Analyst",
            "Penetration Tester (Ethical Hacker)",
            "Security Architect",
            "SOC (Security Operations Center) Analyst",
            "Incident Response Analyst",
            "Cryptographer",
            "GRC (Governance, Risk, Compliance) Specialist"
        ],
        
        "Cloud & Infrastructure": [
            "Cloud Architect (AWS, Azure, GCP)",
            "Cloud Security Specialist",
            "Systems Administrator (Linux/Windows)",
            "Network Engineer (CCNA, CCNP)",
            "Database Administrator (DBA) (SQL, NoSQL)",
            "IT Infrastructure Manager"
        ],
        
        "Testing & QA": [
            "Manual Tester",
            "Automation Tester (Selenium, Cypress)",
            "Performance Tester (JMeter, LoadRunner)",
            "QA Lead/Manager",
            "DevTestOps Engineer"
        ],
        
        "IT Consulting & Management": [
            "IT Consultant",
            "Technical Project Manager",
            "Scrum Master (Agile, SAFe)",
            "Product Manager/Owner",
            "Solutions Architect",
            "Enterprise Architect",
            "IT Auditor"
        ],
        
        "Emerging & Niche Tech Roles": [
            "Quantum Computing Engineer",
            "Robotics Process Automation (RPA) Developer (UiPath, Blue Prism)",
            "5G Network Specialist",
            "IoT Solutions Architect",
            "Digital Twin Engineer",
            "Metaverse Developer"
        ],
        
        "Hardware & Electronics": [
            "Hardware Design Engineer",
            "VLSI Engineer (Chip Design)",
            "FPGA Engineer",
            "PCB Design Engineer"
        ],
        
        "Sales and Marketing": [
            "Sales Executive", "Business Development Manager", "Account Manager",
            "Digital Marketing Specialist", "SEO/SEM Expert", "Content Marketer",
            "Social Media Manager", "Brand Manager", "Market Research Analyst",
            "PR (Public Relations) Manager", "Affiliate Marketing Specialist"
        ],
        
        "Finance and Accounting": [
            "Accountant", "Financial Analyst", "Auditor",
            "Tax Consultant", "CFO (Chief Financial Officer)", "Investment Banker",
            "Risk Analyst", "Payroll Specialist", "Treasury Manager",
            "Cost Accountant"
        ],
        
        "Human Resources (HR)": [
            "HR Manager", "Recruiter", "Talent Acquisition Specialist",
            "Learning & Development (L&D) Manager", "Compensation & Benefits Analyst",
            "HR Business Partner", "Diversity & Inclusion Officer",
            "Employee Relations Manager"
        ],
        
        "Operations": [
            "Operations Manager", "Logistics Coordinator", "Supply Chain Analyst",
            "Production Supervisor", "Quality Assurance (QA) Manager",
            "Inventory Manager", "Process Engineer", "Facilities Manager"
        ],
        
        "Customer Service": [
            "Customer Support Representative", "Call Center Agent",
            "Technical Support Engineer", "Client Success Manager",
            "Helpdesk Analyst", "Customer Experience (CX) Specialist"
        ],
        
        "Legal and Compliance": [
            "Corporate Lawyer", "Compliance Officer", "Legal Consultant",
            "Intellectual Property (IP) Specialist", "Data Privacy Officer",
            "Contract Manager"
        ],
        
        "Research and Development (R&D)": [
            "Research Scientist", "Product Development Engineer",
            "Biotech Researcher", "AI/ML Researcher", "Pharmaceutical Researcher",
            "UX Researcher"
        ],
        
        "Administration": [
            "Executive Assistant", "Office Manager", "Administrative Coordinator",
            "Receptionist", "Data Entry Operator", "Virtual Assistant"
        ],
        
        "Supply Chain and Logistics": [
            "Procurement Manager", "Warehouse Supervisor", "Transportation Manager",
            "Demand Planner", "Logistics Engineer", "Import/Export Specialist"
        ],
        
        "Non-Technical & Support Roles (IT Domain)": [
            "Technical Writer",
            "IT Recruiter",
            "IT Sales Executive",
            "Pre-Sales Consultant",
            "Customer Support Engineer",
            "IT Trainer",
            "UX Researcher",
            "UI/UX Designer",
            "Digital Marketing Specialist (IT Domain)"
        ]
    }

    # Display departments and roles in expandable sections
    for dept, roles in departments.items():
        with st.expander(f"📌 {dept} ({len(roles)} roles)"):
            for role in roles:
                st.markdown(f"• {role}")
    
    if st.button("Back to Dashboard"):
        st.session_state.show_job_page = False
        st.rerun()

def main():
    st.set_page_config(page_title="ORBT-LEARN", layout="wide")

    # Green title
    st.markdown("<h1 style='color: green; text-align: center;'>ORBT LeARN</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>LeARN & eARN</h1>", unsafe_allow_html=True)

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
        show_job_page()
        return
    if st.session_state.show_education_page:
        show_education_page()
        return
    if st.session_state.show_travel_page:
        show_travel_page()
        return
    if st.session_state.show_podcast_page:
        show_podcast_page()
        return

    # Main dashboard

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
