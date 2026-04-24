import streamlit as st
import requests
import plotly.graph_objects as go

st.set_page_config(page_title="Resume Intel AI", layout="wide")

st.title("🤖 Resume Intelligence System")
st.markdown("---")

tab1, tab2 = st.tabs(["📊 Candidate Analysis", "🎯 ATS Matcher"])

with tab1:
    st.header("Upload & Profile Generation")
    uploaded_file = st.file_uploader("Choose a Resume PDF", type="pdf")
    
    if st.button("Analyze Resume"):
        if uploaded_file:
            with st.spinner("AI is analyzing your resume..."):
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
                response = requests.post("http://localhost:8000/upload_resume", files=files)
                
                if response.status_code == 200:
                    result = response.json()
                    if "profile" in result:
                        st.session_state['profile'] = result['profile']
                        st.session_state['raw_text'] = result.get('raw_text', '')
                        st.success("Analysis Complete!")
                        st.markdown("### 📋 Recruiter-Ready Profile")
                        st.info(st.session_state['profile'])
                    else:
                        st.error(f"Error: {result.get('error')}")
                else:
                    st.error("Failed to connect to the backend server.")

with tab2:
    st.header("Job Description Matching")
    if 'profile' not in st.session_state:
        st.warning("⚠️ Please analyze a resume in the first tab before scoring.")
    else:
        # Always show the profile summary in Tab 2
        st.markdown("### 📋 Candidate Profile")
        st.info(st.session_state['profile'])
        st.markdown("---")

        jd_text = st.text_area("Paste the Job Description (JD) here:", height=250)
        
        if st.button("Calculate ATS Score"):
            if jd_text:
                with st.spinner("Calculating ATS score..."):
                    payload = {
                        "profile": st.session_state['profile'],
                        "raw_text": st.session_state.get('raw_text', ''),
                        "jd": jd_text
                    }
                    res = requests.post("http://localhost:8000/score_resume", json=payload)
                    score = res.json().get("score")
                    
                    fig = go.Figure(go.Indicator(
                        mode = "gauge+number",
                        value = score,
                        domain = {'x': [0, 1], 'y': [0, 1]},
                        title = {'text': "ATS Match %", 'font': {'size': 24}},
                        gauge = {
                            'axis': {'range': [0, 100], 'tickwidth': 1},
                            'bar': {'color': "#1f77b4"},
                            'steps': [
                                {'range': [0, 40], 'color': "#ff4b4b"},
                                {'range': [40, 75], 'color': "#ffa500"},
                                {'range': [75, 100], 'color': "#00cc96"}
                            ],
                        }
                    ))
                    st.plotly_chart(fig)
            else:
                st.error("Please paste a Job Description to compare.")