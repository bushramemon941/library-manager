import streamlit as st
import pandas as pd

# Load or initialize the library data
if 'library' not in st.session_state:
    st.session_state.library = pd.DataFrame(columns=["Title", "Author", "Genre", "Year"])

# Function to add a book
def add_book(title, author, genre, year):
    new_book = pd.DataFrame({"Title": [title], "Author": [author], "Genre": [genre], "Year": [year]})
    st.session_state.library = pd.concat([st.session_state.library, new_book], ignore_index=True)

# Function to delete a book
def delete_book(title):
    st.session_state.library = st.session_state.library[st.session_state.library["Title"] != title]

# Function to update a book
def update_book(old_title, new_title, new_author, new_genre, new_year):
    index = st.session_state.library[st.session_state.library["Title"] == old_title].index
    if not index.empty:
        st.session_state.library.at[index[0], "Title"] = new_title
        st.session_state.library.at[index[0], "Author"] = new_author
        st.session_state.library.at[index[0], "Genre"] = new_genre
        st.session_state.library.at[index[0], "Year"] = new_year

# Custom CSS for colorful UI and background image
def set_custom_css():
    st.markdown(
        """
        <style>
       

        /* Set headings and subheadings  */
        h1, h2, h3, h4, h5, h6 {
            color:black !important; /* black color */
        }

        /* Set all text, including labels, inputs, and table content, to white */
        label, .stTextInput label, .stNumberInput label, .stTable th, .stTable td, .stInfo, .stWarning, .stSuccess, .stError {
            color:blue !important; 
        }

        /* Sidebar styling */
        .css-1d391kg {
            background-color: rgba(77, 221, 58, 0.9) !important;
        }

        /* Sidebar menu text color */
        .stSelectbox>div>div>div {
            color:#FF0000. !important;
        }

        /* Sidebar dropdown options text color */
        .stSelectbox>div>div>div[role="listbox"]>div {
            color: #FF0000.  !important;
        }

        /* Sidebar label text color */
        .stSidebar label {
            color: #FF0000.  !important;
        }

        /* Button styling */
        .stButton>button {
            background-color: #3498DB !important;
            color: white !important;
            border-radius: 10px;
            padding: 10px 20px;
            border: none;
        }

        /* Input field styling */
        .stTextInput>div>div>input, .stNumberInput>div>div>input {
            background-color: rgba(255, 255, 255, 0.9) !important;
            border-radius: 5px;
            border: 1px solid #BDC3C7;
            color: black !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Streamlit App
def main():
    set_custom_css()  # Apply custom CSS
    st.title("📚 Personal Library Manager")

    # Sidebar for navigation
    menu = st.sidebar.selectbox("Menu", ["Add Book", "View Books", "Search Book", "Delete Book", "Update Book"])

    if menu == "Add Book":
        st.header(" Add a New Book")
        title = st.text_input("Title")
        author = st.text_input("Author")
        genre = st.text_input("Genre")
        year = st.number_input("Year", min_value=1800, max_value=2100)
        if st.button("Add Book"):
            if title and author and genre and year:
                add_book(title, author, genre, year)
                st.success("✅ Book added successfully!")
            else:
                st.error(" Please fill in all fields.")

    elif menu == "View Books":
        st.header("📖 Your Library")
        if not st.session_state.library.empty:
            st.table(st.session_state.library)
        else:
            st.info("📂 Your library is empty. Add some books!")

    elif menu == "Search Book":
        st.header("🔍 Search for a Book")
        search_term = st.text_input("Enter title or author")
        if search_term:
            result = st.session_state.library[
                (st.session_state.library["Title"].str.contains(search_term, case=False)) |
                (st.session_state.library["Author"].str.contains(search_term, case=False))
            ]
            if not result.empty:
                st.table(result)
            else:
                st.warning("🔍 No books found matching your search.")

    elif menu == "Delete Book":
        st.header("🗑️ Delete a Book")
        title_to_delete = st.text_input("Enter the title of the book to delete")
        if st.button("Delete Book"):
            if title_to_delete:
                delete_book(title_to_delete)
                st.success("✅ Book deleted successfully!")
            else:
                st.error(" Please enter a title.")

    elif menu == "Update Book":
        st.header("✏️ Update Book Details")
        old_title = st.text_input("Enter the current title of the book")
        new_title = st.text_input("Enter the new title (leave blank to keep current)")
        new_author = st.text_input("Enter the new author (leave blank to keep current)")
        new_genre = st.text_input("Enter the new genre (leave blank to keep current)")
        new_year = st.number_input("Enter the new year (leave blank to keep current)", min_value=1800, max_value=2100)
        if st.button("Update Book"):
            if old_title:
                update_book(old_title, new_title, new_author, new_genre, new_year)
                st.success("✅ Book updated successfully!")
            else:
                st.error(" Please enter the current title of the book.")

# Run the app
if __name__ == "__main__":
    main()