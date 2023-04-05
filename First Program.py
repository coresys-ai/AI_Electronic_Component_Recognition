import streamlit as st 

# To add title to streamlit
st.title("Streamlit - First Program")

# To print string to streamlit
st.write("Hello")

# To add text input box
movie_name = st.text_input('Enter Movie title')
st.write('Entered movie title is', movie_name)

# To add dropdown selectbox
option = st.selectbox(
    'Which number do you like best?',
     ("1",
     "2",
     "3"))
st.write('You selected: ', option)

# To add buttons
if st.button('Say hello'):
    st.write('Why hello there')
else:
	st.write('Goodbye')

# To add radio buttons
genre = st.radio("What's your favorite movie genre",
	('Comedy', 'Drama', 'Documentary'))

if genre == 'Comedy':
	st.write('You selected comedy.')
else:
	st.write("You didn't select comedy.")

