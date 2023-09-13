import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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

streamlit.title('Fruityvice Fruit Advice!')

try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get a information")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)

except URLError as e:
  streamlit.Error()

streamlit.write('The user entered ', fruit_choice)



# write your own comment -what does the next line do? 

# write your own comment - what does this do?


streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contain:")
streamlit.dataframe(my_data_rows)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
