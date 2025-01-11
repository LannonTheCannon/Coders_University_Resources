import streamlit as st
from database import init_db, add_registration, get_all_registrations
import re
from PIL import Image
from datetime import datetime

# Page config
st.set_page_config(
    page_title="AI Workshop & Courses",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stRadio > label {
        font-size: 1.2rem;
        font-weight: bold;
        color: #1F75FE;
    }
    .big-font {
        font-size: 1.2rem !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize the database
init_db()


# Sidebar
with st.sidebar:
    st.title("🌟 Navigation")
    choice = st.radio(
        "Choose a Page",
        ["Student Workshop", "PCEP-30 Python Certification", "WHS Tech Course", "📝 Register Now"],
        index=0
    )

    st.markdown("---")
    st.markdown("### 📧 Contact Us")
    st.markdown("Email: khaulannon@gmail.com")
    st.markdown("📞 Phone: (626) 977-3921")


# Helper function for countdown
def get_countdown():
    event_date = datetime(2025, 1, 15, 18, 0)  # January 15th, 2025 at 6:00 PM
    now = datetime.now()
    delta = event_date - now

    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60

    return days, hours, minutes, seconds

# Main Content
if choice == "Workshop Showcase":

    # Header with gradient
    st.markdown("""
        <h1 style='text-align: center; color: #1F75FE; 
        background: linear-gradient(to right, #FF69B4, #4B0082); 
        padding: 20px; border-radius: 10px; color: white;'>
        🎉 AI x Python Workshop Showcase 🎉
        </h1>
        """, unsafe_allow_html=True)

    if choice == "Workshop Showcase":
        # Header with gradient (previous code remains)

        # Add Countdown Timer
        st.markdown("""
            <h2 style='text-align: center; color: #1F75FE; margin-top: 20px;'>
            ⏳ Countdown to Showcase
            </h2>
        """, unsafe_allow_html=True)

        # Create placeholder for countdown
        countdown_placeholder = st.empty()


        # Display countdown in columns
        def display_countdown():
            days, hours, minutes, seconds = get_countdown()
            col1, col2, col3, col4 = st.columns(4)

            with col1:
                st.markdown(f"""
                    <div style='background-color: #FF69B4; padding: 20px; border-radius: 10px; text-align: center;'>
                        <h1 style='color: white; margin: 0;'>{days}</h1>
                        <p style='color: white; margin: 0;'>Days</p>
                    </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                    <div style='background-color: #4B0082; padding: 20px; border-radius: 10px; text-align: center;'>
                        <h1 style='color: white; margin: 0;'>{hours}</h1>
                        <p style='color: white; margin: 0;'>Hours</p>
                    </div>
                """, unsafe_allow_html=True)

            with col3:
                st.markdown(f"""
                    <div style='background-color: #FF69B4; padding: 20px; border-radius: 10px; text-align: center;'>
                        <h1 style='color: white; margin: 0;'>{minutes}</h1>
                        <p style='color: white; margin: 0;'>Minutes</p>
                    </div>
                """, unsafe_allow_html=True)

            with col4:
                st.markdown(f"""
                    <div style='background-color: #4B0082; padding: 20px; border-radius: 10px; text-align: center;'>
                        <h1 style='color: white; margin: 0;'>{seconds}</h1>
                        <p style='color: white; margin: 0;'>Seconds</p>
                    </div>
                """, unsafe_allow_html=True)


        # Display initial countdown
        with countdown_placeholder.container():
            display_countdown()

        # Add some space after countdown
        st.markdown("<br>", unsafe_allow_html=True)

    # Event Details
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("📅 Date: January 15th, 2025")
    with col2:
        st.info("⏰ Time: 6:00 PM - 7:00 PM")
    with col3:
        st.info("📍 Location: Premier Academy")

    # Description
    st.markdown("## 🌟 Join Us for an Evening of Innovation!")
    st.write("""
    Watch as our talented students showcase their innovative projects combining 
    Python programming with OpenAI's cutting-edge technology. Experience firsthand 
    how the next generation of programmers is shaping the future!
    """)

    # Presenters
    st.markdown("## 🎤 Our Amazing Presenters")
    col1, col2, col3 = st.columns(3)

    presenters = [
        {"name": "Bailey Tang", "project": "Portfolio x OpenAI"},
        {"name": "Stanley Zhu", "project": "Portfolio x OpenAI"},
        {"name": "Shawn Zhu", "project": "Portfolio x OpenAI"}
    ]

    for presenter, col in zip(presenters, [col1, col2, col3]):
        with col:
            st.markdown(f"""
            <div style='background-color: #f0f8ff; padding: 20px; border-radius: 10px; text-align: center;'>
                <h3 style='color: #1F75FE;'>{presenter['name']}</h3>
                <p style='color: #4B0082;'>{presenter['project']}</p>
            </div>
            """, unsafe_allow_html=True)

elif choice == "PCEP-30 Python Certification":
    st.markdown("""
        <h1 style='text-align: center; color: white; 
        background: linear-gradient(to right, #32CD32, #008000); 
        padding: 20px; border-radius: 10px;'>
        🐍 PCEP-30 Python Certification Prep Course
        </h1>
        """, unsafe_allow_html=True)

    st.markdown("### 🎯 Program Highlights")
    col1, col2 = st.columns(2)

    with col1:
        st.success("""
        #### 📚 What You'll Learn
        - Python fundamentals
        - Data structures & algorithms
        - Object-oriented programming
        - Problem-solving techniques
        - Industry best practices
        """)

    with col2:
        st.info("""
        #### ⭐ Why Choose This Course?
        - 9-month structured curriculum
        - Hands-on projects
        - Industry-recognized certification
        - Expert instructors
        - Small class sizes
        """)

    st.markdown("### 🎓 Perfect for Students Grades 6-12!")
    st.write("""
    Start your coding journey today! Our program is specially designed to take you 
    from a complete beginner to a certified Entry Level Python Programmer in just 9 months. 
    No prior experience needed!
    """)


elif choice == "📝 Register Now":
    st.markdown("""
        <h1 style='text-align: center; color: white; 
        background: linear-gradient(to right, #FF1493, #00BFFF); 
        padding: 20px; border-radius: 10px;'>
        ✨ Register for Our Programs ✨
        </h1>
        """, unsafe_allow_html=True)

    # Registration form
    with st.form("registration_form"):
        name = st.text_input("Full Name*")
        email = st.text_input("Email Address*")

        # Program selection
        program = st.selectbox(
            "Select Program",
            ["AI x Python Workshop", "PCEP-30 Python Certification",
             "WHS Tech Course"]
        )

        # Additional comments
        comments = st.text_area("Additional Comments (Optional)")

        submitted = st.form_submit_button("Register Now!")

        if submitted:
            if not name or not email:
                st.error("Please fill in all required fields!")
            elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                st.error("Please enter a valid email address!")
            else:
                if add_registration(name, email):
                    st.balloons()
                    st.success("""
                        🎉 Registration Successful! 
                        We'll contact you shortly with more details.
                    """)
                    # Send confirmation details
                    st.info(f"""
                        Registration Details:
                        - Name: {name}
                        - Email: {email}
                        - Program: {program}
                    """)
                else:
                    st.error("An error occurred. Please try again later.")

    # Add some engaging content below the form
    st.markdown("---")
    st.markdown("### 🌟 Why Register with Us?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        #### ✨ Benefits
        - Expert instructors
        - Hands-on learning
        - Small class sizes
        - Flexible schedules
        - Project-based curriculum
        """)

    with col2:
        st.markdown("""
        #### 🎯 What to Expect
        - Regular progress updates
        - Interactive sessions
        - Real-world projects
        - Supportive community
        - Certificate of completion
        """)

    # Add this if you want an admin view of registrations (optional)
    # if st.sidebar.checkbox("Show Admin View", key="admin"):
    #     st.markdown("### 📊 Recent Registrations")
    #     registrations = get_all_registrations()
    #     if registrations:
    #         st.table(registrations)
    #     else:
    #         st.info("No registrations yet!")

else:  # WHS Tech Course
    st.markdown("""
        <h1 style='text-align: center; color: white; 
        background: linear-gradient(to right, #FF8C00, #FF4500); 
        padding: 20px; border-radius: 10px;'>
        💻 Walnut High School Tech & Innovation Course Support
        </h1>
        """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🏫 Group Classes", "👤 1-on-1 Sessions"])

    with tab1:
        st.markdown("### 👥 Group Classes")
        st.write("""
        Join our collaborative learning environment where students work together 
        to master Python programming concepts while having fun!
        """)

        st.success("""
        #### Benefits:
        - Interactive group projects
        - Peer programming practice
        - Team problem-solving
        - Competitive coding challenges
        - Affordable group rates
        """)

    with tab2:
        st.markdown("### 🎯 1-on-1 Sessions")
        st.write("""
        Get personalized attention and custom-paced learning with our 
        dedicated instructors.
        """)

        st.info("""
        #### Advantages:
        - Flexible scheduling
        - Personalized curriculum
        - Focus on your specific needs
        - Rapid progress tracking
        - Direct feedback and support
        """)

    # Success Stories
    st.markdown("### 🌟 Student Success Stories")
    st.markdown("""
    > "The course helped me ace my Tech and Innovation test!" - *Sarah L.*

    > "I went from struggling with basic concepts to confidently building my own programs." - *David K.*
    """)


    # Add this if you want an admin view of registrations (optional)
    if st.sidebar.checkbox("Show Admin View", key="admin"):
        st.markdown("### 📊 Recent Registrations")
        registrations = get_all_registrations()
        if registrations:
            st.table(registrations)
        else:
            st.info("No registrations yet!")


# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    © 2024 Premier Academy. All rights reserved.
</div>
""", unsafe_allow_html=True)