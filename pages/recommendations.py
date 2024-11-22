import streamlit as st
import pickle
import numpy as np
from surprise import SVD, Dataset, Reader
from sklearn.metrics.pairwise import cosine_similarity



books = pickle.load(open('model/filtered_books.pkl', 'rb'))
books_list = books.drop_duplicates('Book-Title')['Book-Title']
# similarity_scores_cs = pickle.load(open('model/similarity_scores_cs.pkl', 'rb'))
# pivot_table = pickle.load(open('model/books_users_pivot.pkl', 'rb'))

filtered_users_df = pickle.load(open('model/filtered_users_df.pkl', 'rb'))

st.header('Books Recommender System')

selected_book = st.selectbox(
    "Select a book to get recommendations",
    books_list
)

@st.cache_data
def train_model(filtered_users_df):
    reader = Reader(rating_scale=(0, 10))
    data = Dataset.load_from_df(filtered_users_df[['User-ID', 'Book-Title', 'Book-Rating']], reader)
    model = SVD()
    full_trainset = data.build_full_trainset()
    model.fit(full_trainset)
    return model, full_trainset

# Main app logic
model, full_trainset = train_model(filtered_users_df)

 


def recommend(selected_book):
    book_index = full_trainset.to_inner_iid(selected_book)

    all_books = [full_trainset.to_raw_iid(i) for i in range(full_trainset.n_items)]
  

    item_latent_factors = model.qi
    similarity_scores = cosine_similarity(item_latent_factors[book_index].reshape(1, -1), item_latent_factors)
    similarity_scores = similarity_scores.flatten()
    similar_book_indices = similarity_scores.argsort()[::-1]

    data = []

    for i in range(1, 6):
        item = []
        similar_book_index = similar_book_indices[i]
        similar_book_name = full_trainset.to_raw_iid(similar_book_index)
        temp_df = filtered_users_df[filtered_users_df['Book-Title'] == similar_book_name]
        item.extend(temp_df.drop_duplicates(subset='Book-Title')['Book-Title'].values)
        item.extend(temp_df.drop_duplicates(subset='Book-Title')['Book-Author'].values)
        item.extend(temp_df.drop_duplicates(subset='Book-Title')['Image-URL-M'].values)

        data.append(item)

    return data


if st.button('Show Recommendations', type='secondary'):
    recs = recommend(selected_book)

    # st.image(recs[1][2])

    if recs:
        st.text(f'Here are the recommendations related to {selected_book}:')

        cols = st.columns(5)

        for i, b in enumerate(recs):
            with cols[i]:
                st.image(recs[i][2])
                st.html(f"<h5>{ recs[i][0] }</h5>")
                st.html(f"<p>{ recs[i][1] }</p>")
    else:
        st.text('No recommendations found.')