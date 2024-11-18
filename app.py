import streamlit as st
import pickle
import requests
import numpy as np

st.header('Books Recommender System')

books = pickle.load(open('model/filtered_books.pkl', 'rb'))
books_list = books.drop_duplicates('Book-Title')['Book-Title']

similarity_scores_cs = pickle.load(open('model/similarity_scores_cs.pkl', 'rb'))

pivot_table = pickle.load(open('model/books_users_pivot.pkl', 'rb'))

# st.text(len(books_list))

selected_book = st.selectbox(
    "Select a book to get recommendations",
    books_list
)

def recommend(selected_book):
    index = np.where(pivot_table.index == selected_book)[0][0]
    similar_books = sorted(list(enumerate(similarity_scores_cs[index])), key = lambda x:x[1], reverse=True)[1:6]

    data = []

    for book in similar_books:
        temp_df = books[books['Book-Title'] == pivot_table.index[book[0]]]

        for _, row in temp_df.iterrows():
            item = {
                'title': row['Book-Title'],
                'author': row['Book-Author'],
                'image_url': row['Image-URL-L']
            }
        
        data.append(item)

    return data    



if st.button('Show Recommendations', type='secondary'):
    recs = recommend(selected_book)

    if recs:
        st.text(f'Here are the recommendations related to {selected_book}:')

        cols = st.columns(5)

        for i, b in enumerate(recs):
            with cols[i]:
                st.image(b['image_url'], use_container_width=True)
                st.html(f"<h5>{ b['title'] }</h5>")
                st.html(f"<p>{ b['author'] }</p>")
    else:
        st.text('No recommendations found.')

