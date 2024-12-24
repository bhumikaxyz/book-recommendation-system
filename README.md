# Book Recommendation System

## Overview

This project is a Book Recommendation System that provides users with book suggestions based on two approaches: **a popularity-based (content-based) system** and a **collaborative filtering-based system**. The goal is to recommend books that are relevant and engaging to users based on ratings data.

## Application URL

[https://book-recommendation-system-fd2b.onrender.com](https://book-recommendation-system-fd2b.onrender.com)

## Dataset

The dataset used for the purpose of this project can be accessed [here](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset).

The project utilizes three CSV files:

* **books.csv**: Contains information about the books.
* **users.csv**: Contains information about the users.
* **ratings.csv**: Contains user ratings for books.

## Features

### 1. Popularity-Based Recommendation System

* Recommends the top 50 books with the highest average rating.
* Considers only books that have received at least 250 ratings to ensure reliability.

### 2. Collaborative Filtering-Based Recommendation System

* Recommends books based on user preferences and similarities.
* Filters:
  * Only considers users who have rated at least 200 books.
  * Only includes books with at least 50 ratings.
* Utilizes **cosine similarity** for building the collaborative filtering system.

### 3. Advanced Collaborative Filtering Using scikit-surprise

* Explored multiple algorithms for collaborative filtering:
  * SVD
  * KNNBasic
  * KNNWithZScore
  * NMF
* Finalized the use of **SVD i.e Singular Value Decomposition** to generate recommendations.
* **Implementation Details for SVD**:
  * Built a full training dataset using the `scikit-surprise` library.
  * Trained the SVD model on user-item interactions.
  * For a given book, calculated similarity scores between its latent factors and those of all other books using cosine similarity.
  * Ranked the books based on their similarity scores and retrieved the top 5 recommendations.
  * Each recommendation includes the book title, author, and cover image for enhanced user experience.


## Installation

1. Clone this repository:
   ```
   git clone https://github.com/bhumikaxyz/book-recommendation-system.git
   ```
2. Navigate to the project directory:
   ```
   cd book-recommendation-system
   ```
3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit application:
   ```
   streamlit run app.py
   ```
2. Open the provided local URL in your browser to use the system.

## License

This project is licensed under the MIT License.
