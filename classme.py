import streamlit as st
from streamlit_tree_select import tree_select

with st.sidebar:
    st.title("Streamlit-tree-select")
    st.subheader("A simple and elegant checkbox tree for Streamlit.")

    # Create nodes to display
    nodes = [
        {"label": "Folder A", "value": "folder_a"},
        {
            "label": "Folder B",
            "value": "folder_b",
            "children": [
                {"label": "Sub-folder A", "value": "sub_a"},
                {"label": "Sub-folder B", "value": "sub_b"},
                {"label": "Sub-folder C", "value": "sub_c"},
            ],
        },
        {
            "label": "Folder Bc",
            "value": "folder_bc",
            "children": [
                {"label": "Sub-folder A", "value": "sub_a1"},
                {"label": "Sub-folder B", "value": "sub_b1"},
                {"label": "Sub-folder C", "value": "sub_c1"},
            ],
        },
        {
            "label": "Folder Bcc",
            "value": "folder_bcc",
            "children": [
                {"label": "Sub-folder A", "value": "sub_a2"},
                {"label": "Sub-folder B", "value": "sub_b2"},
                {"label": "Sub-folder C", "value": "sub_c2"},
            ],
        },
        {
            "label": "Folder Bccc",
            "value": "folder_bccc",
            "children": [
                {"label": "Sub-folder A", "value": "sub_a3"},
                {"label": "Sub-folder B", "value": "sub_b3"},
                {"label": "Sub-folder C", "value": "sub_c3"},
            ],
        },
        {
            "label": "Folder D",
            "value": "folder_d",
            "children": [
                {"label": "Sub-folder A", "value": "sub_a4"},
                {"label": "Sub-folder B", "value": "sub_b4"},
                {"label": "Sub-folder C", "value": "sub_c4"},
            ],
        },
        {
            "label": "Folder E",
            "value": "folder_e",
            "children": [
                {"label": "Sub-folder A", "value": "sub_a5"},
                {"label": "Sub-folder B", "value": "sub_b5"},
                {"label": "Sub-folder C", "value": "sub_c5"},
            ],
        },
        {
            "label": "Folder F",
            "value": "folder_f",
            "children": [
                {"label": "Sub-folder A", "value": "sub_a6"},
                {"label": "Sub-folder B", "value": "sub_b6"},
                {"label": "Sub-folder C", "value": "sub_c6"},
            ],
        },
        {
            "label": "Folder G",
            "value": "folder_g",
            "children": [
                {"label": "Sub-folder A", "value": "sub_a7"},
                {"label": "Sub-folder B", "value": "sub_b7"},
                {"label": "Sub-folder C", "value": "sub_c7"},
            ],
        },
        {
            "label": "Folder H",
            "value": "folder_h",
            "children": [
                {"label": "Sub-folder A", "value": "sub_a8"},
                {"label": "Sub-folder B", "value": "sub_b8"},
                {"label": "Sub-folder C", "value": "sub_c8"},
            ],
        },
        {
            "label": "Folder I",
            "value": "folder_i",
            "children": [
                {"label": "Sub-folder A", "value": "sub_a9"},
                {"label": "Sub-folder B", "value": "sub_b9"},
                {"label": "Sub-folder C", "value": "sub_c9"},
            ],
        },
        {
            "label": "Folder L",
            "value": "folder_l",
            "children": [
                {"label": "Sub-folder A", "value": "sub_a10"},
                {"label": "Sub-folder B", "value": "sub_b10"},
                {"label": "Sub-folder C", "value": "sub_c10"},
            ],
        },
        {
            "label": "Folder M",
            "value": "folder_m",
            "children": [
                {"label": "Sub-folder A", "value": "sub_a11"},
                {"label": "Sub-folder B", "value": "sub_b11"},
                {"label": "Sub-folder C", "value": "sub_c11"},
            ],
        },
        {
            "label": "Folder N",
            "value": "folder_n",
            "children": [
                {"label": "Sub-folder D", "value": "sub_d1"},
                {
                    "label": "Sub-folder E",
                    "value": "sub_e",
                    "children": [
                        {"label": "Sub-sub-folder A", "value": "sub_sub_a"},
                        {"label": "Sub-sub-folder B", "value": "sub_sub_b"},
                    ],
                },
                {"label": "Sub-folder F", "value": "sub_f"},
            ],
        },
    ]

    return_select = tree_select(nodes)
    st.write(return_select)
