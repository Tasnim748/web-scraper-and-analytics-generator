# visualize.py

import matplotlib.pyplot as plt
import streamlit as st

def plot_bar(df, x_field, y_field, title=None):
    if x_field not in df.columns or y_field not in df.columns:
        st.error(f"Fields {x_field} or {y_field} not found in DataFrame.")
        return
    
    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(df[x_field], df[y_field])
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    ax.set_xlabel(x_field.capitalize())
    ax.set_ylabel(y_field.capitalize())
    ax.set_title(title or f"{y_field.capitalize()} by {x_field.capitalize()}")
    plt.tight_layout()
    
    # Return the figure to be displayed by Streamlit
    return fig

def plot_line(df, x_field, y_field, title=None):
    if x_field not in df.columns or y_field not in df.columns:
        st.error(f"Fields {x_field} or {y_field} not found in DataFrame.")
        return
    
    fig, ax = plt.subplots(figsize=(10,6))
    ax.plot(df[x_field], df[y_field], marker='o')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    ax.set_xlabel(x_field.capitalize())
    ax.set_ylabel(y_field.capitalize())
    ax.set_title(title or f"{y_field.capitalize()} over {x_field.capitalize()}")
    plt.tight_layout()
    
    # Return the figure to be displayed by Streamlit
    return fig