import streamlit as st
import pickle
import numpy as np

popular_books = pickle.load(open('model/popular_books_df.pkl', 'rb'))


st.header('Top 20 Popular Books')

st.write("")

for i in range(20):
    book = popular_books.iloc[i]
    with st.container():
        cols = st.columns([1, 3])  

        with cols[0]:
            st.image(book['Image-URL-M'])  

        with cols[1]:
            st.subheader(book['Book-Title'])  
            st.write(f"**Author:** {book['Book-Author']}")  