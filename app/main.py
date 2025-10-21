import streamlit as st

st.set_page_config(
    page_title="Pension AI Advisor",
    page_icon="🏦",
    layout="wide"
)

def main():
    st.sidebar.title("🏦 Navigation")
    page = st.sidebar.radio("Go to", ["Configuration", "Chat", "Analytics"])
    
    if page == "Configuration":
        st.title("⚙️ Configuration")
        st.info("Configure your Databricks workspace and LLM endpoints")
        
    elif page == "Chat":
        st.title("💬 Chat")
        st.info("Chat with the AI pension advisor")
        
    elif page == "Analytics":
        st.title("📊 Analytics")
        st.info("View performance metrics and evaluations")

if __name__ == "__main__":
    main()
