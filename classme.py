import streamlit as st
from streamlit_tree_select import tree_select

datapath1 = "./treelist"

with open(datapath1) as f:
    nodes = f.readlines()

with st.sidebar:
    st.title("Streamlit-tree-select")
    st.subheader("A simple and elegant checkbox tree for Streamlit.")
 
    return_select = tree_select(nodes)
    st.write(return_select)
