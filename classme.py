import streamlit as st
import pandas as pd
from streamlit_tree_select import tree_select

datapath1 = "./treelist"

tree1 = pd.load_data(datapath1)

with st.sidebar:
    st.title("Streamlit-tree-select")
    st.subheader("A simple and elegant checkbox tree for Streamlit.")
    
    

    # Create nodes to display
    nodes = tree1

    return_select = tree_select(nodes)
    st.write(return_select)
