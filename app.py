import streamlit as st
from src.model import train_model
from src.agents import health_analysis
from src.rag import load_knowledge, build_index, retrieve

# Train model once
train_model()

st.title("🧬 AI Digital Health Twin")

steps = st.number_input("Daily Steps", value=6000)
sleep = st.number_input("Sleep Hours", value=7.0)
heart_rate = st.number_input("Heart Rate", value=75)

query = st.text_input("Ask Health Question")

if st.button("Analyze Health"):
    
    score, level, advice = health_analysis(steps, sleep, heart_rate)
    
    st.subheader("📊 Health Analysis")
    st.write(f"Risk Score: {score:.2f}")
    st.write(f"Risk Level: {level}")
    st.write(f"Advice: {advice}")
    
    # RAG Insights
    docs = load_knowledge()
    index = build_index(docs)
    
    if query:
        insights = retrieve(query, docs, index)
        
        st.subheader("🔎 Health Insights")
        for i in insights:
            st.write(i)