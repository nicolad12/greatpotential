import streamlit as st
import json
from streamlit_tree_select import tree_select

datapath1 = "./treelist"

lines = []
with open(datapath1) as file:
    for line in file: 
        line = line.strip() #or some other preprocessing
        lines.append(line) #storing everything in memory!
     
with st.sidebar:
    st.title("Streamlit-tree-select")
    st.subheader("A simple and elegant checkbox tree for Streamlit.")
 
    return_select = tree_select(nodes)
    st.write(return_select)
