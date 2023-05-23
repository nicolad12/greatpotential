import streamlit as st
import json
from streamlit_tree_select import tree_select

datapath1 = "./treelist"

# reading the data from the file
with open(datapath1) as f:
    data = f.read()
     
# reconstructing the data as a dictionary
nodes = json.loads(data)
    
with st.sidebar:
    st.title("Streamlit-tree-select")
    st.subheader("A simple and elegant checkbox tree for Streamlit.")
 
    return_select = tree_select(nodes)
    st.write(return_select)
