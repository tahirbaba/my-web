import streamlit as st
from PIL import Image

st.set_page_config(page_title="Muhammad Tahir Hasni | Portfolio", layout="wide")

# ----- Custom CSS for styling -----
st.markdown("""
    <style>
        html, body {
            font-family: 'Segoe UI', sans-serif;
        }
        .hero-title {
            font-size: 48px;
            font-weight: bold;
            color: #0e76a8;
        }
        .hero-subtitle {
            font-size: 22px;
            color: #333;
        }
        .section-title {
            font-size: 30px;
            font-weight: 600;
            color: #0e2a47;
            border-left: 5px solid #0e76a8;
            padding-left: 15px;
            margin-top: 50px;
        }
        .project-card {
            background-color: #f2f2f2;
            border-radius: 15px;
            padding: 20px;
            margin: 20px 0;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .contact-links a {
            text-decoration: none;
            color: #0e76a8;
        }
    </style>
""", unsafe_allow_html=True)

# ----- Hero Section -----
st.image("assets/profile_pic.jpg", use_container_width=False, width=180)
st.markdown('<div class="hero-title">👋 Hi, I\'m Muhammad Tahir Hasni</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-subtitle">Aspiring Cloud Native AI Engineer | Streamlit Developer | Web Creator | Frontend Dev</div>', unsafe_allow_html=True)
st.markdown("---")

# ----- Projects -----
st.markdown('<div class="section-title">🚀 Featured Projects</div>', unsafe_allow_html=True)

projects = [
    {
        "name": "BMI Calculator App",
        "description": "Streamlit app to calculate your Body Mass Index.",
        "image": "assets/bmi-calculator.png",
        "live_url": "https://bmi-calculator-tahir.streamlit.app/",
        "repo_url": "https://github.com/tahirbaba/bmi-calculator"
    },
    {
        "name": "Unit Converter",
        "description": "Convert values between units easily with this responsive Streamlit tool.",
        "image": "assets/unit_converter.png",
        "live_url": "https://unit-converter-tahirbaba.streamlit.app/",
        "repo_url": "https://github.com/tahirbaba/unit-converter"
    },
    {
        "name": "Password Strength Generator",
        "description": "Password Strength Generator is a tool to create strong, secure passwords with instant strength detection and customizable options.",
        "image": "assets/Password Strength Generator.png",
        "live_url": "https://password-strength-generator-tahirbaba.streamlit.app/",
        "repo_url": "https://github.com/tahirbaba/tahir-baba-library-manager"
    },
            {
        "name": "Personal Library Manager",
        "description": "Personal Library Manager helps you organize, track, and manage your book collection with ease — all in one place.",
        "image": "assets/Personal Library Manager.png",
        "live_url": "https://personal-library-manager-tahirbaba.streamlit.app/",
        "repo_url": "https://github.com/tahirbaba/tahir-library-manager.git"
    },
    {
        "name": "Mandi To Home",
        "description": "Mandi To Home is a fast and reliable Q-commerce platform that brings the freshest fruits and vegetables straight from the mandi to your doorstep. We ensure top-quality, handpicked produce with same-day delivery — making healthy eating easier, faster, and more convenient than ever.",
        "image": "assets/Mandi-to-home.png",
        "live_url": "https://q-com-mth.vercel.app/",
        "repo_url": "https://github.com/tahirbaba/q-com-mth.git"
    },
]

for project in projects:
    with st.container():
        cols = st.columns([1, 2])
        with cols[0]:
            st.image(project["image"], use_container_width=True)
        with cols[1]:
            st.subheader(project["name"])
            st.write(project["description"])
            st.markdown(f"[🔗 Live Demo]({project['live_url']}) | [📂 GitHub Repo]({project['repo_url']})")

# ----- Skills -----
st.markdown('<div class="section-title">🧠 Skills</div>', unsafe_allow_html=True)
skills = ["Python", "Streamlit", "Pandas", "GitHub", "TypeScript", "Next.js", "HTML", "CSS", "Tailwind"]
cols = st.columns(3)
for i, skill in enumerate(skills):
    cols[i % 3].markdown(f"- ✅ {skill}")

# ----- Services -----
st.markdown('<div class="section-title">🛠️ Services</div>', unsafe_allow_html=True)
services = [
    "🔧 Custom Web Apps (Streamlit/React)",
    "📊 Data Dashboards",
    "🖼️ UI/UX Prototypes",
    "🚀 Deployment (Streamlit Cloud/Vercel)",
    "💬 Chatbot Integrations"
]
for service in services:
    st.write(service)

# ----- Testimonials -----
st.markdown('<div class="section-title">💬 What Clients Say</div>', unsafe_allow_html=True)
testimonials = [
    ("⭐️⭐️⭐️⭐️⭐️", "Very professional and fast delivery!", "Ali Khan"),
    ("⭐️⭐️⭐️⭐️", "Loved the UI design, exactly what I needed.", "Sarah Javed"),
    ("⭐️⭐️⭐️⭐️⭐️", "Highly recommended for web apps.", "Umer Raza")
]

for stars, feedback, name in testimonials:
    st.markdown(f"**{stars}** — *{feedback}* — `{name}`")

# ----- Metrics -----
st.markdown('<div class="section-title">📊 Quick Stats</div>', unsafe_allow_html=True)
m1, m2, m3, m4 = st.columns(4)
m1.metric("Projects", "12")
m2.metric("Live Demos", "8")
m3.metric("Skills", "10+")
m4.metric("Clients", "5+")

# ----- Contact -----
st.markdown('<div class="section-title">📬 Contact Me</div>', unsafe_allow_html=True)
st.markdown("""
<ul class='contact-links'>
    <li>📧 Email: <a href="mailto:muhammadtahirhasni@gmail.com" target="_blank">muhammadtahirhasni@gmail.com</a></li>
    <li>💼 LinkedIn: <a href="https://www.linkedin.com/in/muhammad-tahir-hasni-021a562ba" target="_blank">linkedin.com/in/muhammad-tahir-hasni</a></li>
    <li>🌐 GitHub: <a href="https://github.com/tahirbaba" target="_blank">github.com/tahirbaba</a></li>
    <li>📝 Portfolio: <a href="https://tahirbaba-portfolio.vercel.app" target="_blank">tahirbaba-portfolio.vercel.app</a></li>
</ul>
""", unsafe_allow_html=True)

# ----- Footer -----
st.markdown("---")
st.markdown("<center>Crafted with ❤️ by Muhammad Tahir Hasni | © 2025</center>", unsafe_allow_html=True)
