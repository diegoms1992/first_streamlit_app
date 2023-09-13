import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.title('My parents New Healthy Dinner')

streamlit.header('Breakfast Menu:')
streamlit.text('\n 🥣 Omega3 & Blueberry Oatmeal')
streamlit.text('\n 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('\n 🐔 Hard-boiled Free-Ranged egg')
streamlit.text('\n 🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

streamlit.dataframe(my_fruit_list)
