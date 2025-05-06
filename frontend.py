from rag_pipeline import answer_query, retrieve_docs, llm_model
import streamlit as st

# Initialize session state for conversation history
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Step_1: Setup Upload PDF functionality
uploaded_file = st.file_uploader("Upload PDF",
                                type="pdf",
                                accept_multiple_files=False)

# Display conversation history
st.subheader("Conversation History")
for message in st.session_state.conversation:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Step_2: Chatbot Interface
user_query = st.chat_input("Ask Anything!")

if user_query:
    if uploaded_file:
        # Add user message to conversation history
        st.session_state.conversation.append({"role": "user", "content": user_query})
        
        # Display user message
        with st.chat_message("user"):
            st.write(user_query)

        # RAG Pipeline
        retrieved_docs = retrieve_docs(user_query)
        response = answer_query(documents=retrieved_docs, model=llm_model, query=user_query)
        
        # Add AI response to conversation history
        st.session_state.conversation.append({"role": "AI Lawyer", "content": response})
        
        # Display AI response
        with st.chat_message("AI Lawyer"):
            st.write(response)
    else:
        st.error("Kindly upload a valid PDF file first!")

# Add button to clear conversation history
if st.button("Clear Conversation"):
    st.session_state.conversation = []
    st.rerun()