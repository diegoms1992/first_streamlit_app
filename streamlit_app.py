import streamlit
import pandas
import requests


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.title('My parents New Healthy Dinner')

streamlit.header('Breakfast Menu:')
streamlit.text('\n 🥣 Omega3 & Blueberry Oatmeal')
streamlit.text('\n 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('\n 🐔 Hard-boiled Free-Ranged egg')
streamlit.text('\n 🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Vamos colocar uma lista de seleção aqui para que eles possam escolher as frutas que desejam incluir 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries']) 
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Exiba a tabela na página.
streamlit.dataframe(fruits_to_show)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())
