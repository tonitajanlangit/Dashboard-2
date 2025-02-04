import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
@st.cache_data
def load_data():
    file_path = "netflix_titles.csv"  # Ensure this file exists
    df = pd.read_csv(file_path)
    df_movies = df[df['type'] == 'Movie']  # Filter only movies
    return df_movies

df = load_data()

# Sidebar - Release Year Filter
st.sidebar.title("Filters")
st.write("Columns in DataFrame:", df.columns)  # Debugging step

all_years = df['release_year'].dropna().unique().tolist()
selected_year = st.sidebar.selectbox("Select a Year", ["All"] + sorted(all_years))

# Filter data based on selection
if selected_year != "All":
    df_filtered = df[df['release_year'] == selected_year]
else:
    df_filtered = df

# Ensure 'release_year' exists
if 'release_year' in df_filtered.columns:
    movies_per_year = df_filtered['release_year'].value_counts()

    # Main Title
    st.title("📽️ Netflix Movies Dashboard")

    # Show Movie Count Bar Chart
    st.subheader("Number of Movies Per Year")
    fig, ax = plt.subplots(figsize=(10, 5))
    movies_per_year.plot(kind='bar', ax=ax, color="skyblue")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Movies")
    st.pyplot(fig)

    # Show Table
    st.subheader("Movie Data")
    st.dataframe(df_filtered[['title', 'country', 'release_year', 'duration', 'rating']])
else:
    st.error("⚠️ 'release_year' column not found in dataset!")
