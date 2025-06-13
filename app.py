import streamlit as st
from resume_parser import extract_text_from_pdf
from matcher import get_similarity_score
from nlp_utils import clean_text, extract_skills

SKILLS_DB = ['python', 'sql', 'java', 'c++', 'communication', 'ml', 'data analysis']

st.set_page_config(page_title="AI Resume Screener", layout="wide")
st.title("🤖 AI-Powered Resume Screening Tool")

resume = st.file_uploader("📄 Upload Resume", type=['pdf'])
job_description = st.text_area("📝 Paste Job Description")

if resume and job_description:
    with st.spinner("Processing..."):
        resume_text = extract_text_from_pdf(resume)
        clean_resume = clean_text(resume_text)
        clean_jd = clean_text(job_description)

        # Match Score
        score = get_similarity_score(clean_resume, clean_jd)

        # Skill Extraction
        matched_skills = extract_skills(clean_resume, SKILLS_DB)

    st.success(f"✅ Resume Match Score: {score}%")
    st.markdown("**🎯 Skills Found in Resume:**")
    st.write(", ".join(matched_skills))
