import streamlit as st
import pickle
import numpy as np


pg = st.navigation([st.Page("pages/home.py", title="Home"), st.Page('pages/recommendations.py', title="Recommend Me a Book")])

pg.run()



