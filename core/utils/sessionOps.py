import streamlit as st

def save_to_session_state(key, value):
    """Save a value to session state"""
    st.session_state[key] = value
    
def get_from_session_state(key, default=None):
    """Get a value from session state with a default"""
    return st.session_state.get(key, default)