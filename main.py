import streamlit as st
import langchain_helper

st.title("Ingredients for the Dish")

diet = st.sidebar.selectbox("Pick a Diet", ("Vegetarian", "Non-Vegetarian", "Vegan", "Eggitarian", "Carnivore"))

if diet:
    response = langchain_helper.generate_dish_name_and_ingredients(diet)
    st.header(response['dish'].strip())
    items = response['ingredients'].strip().split(",")
    st.write("**Ingredients needed**")
    for item in items:
        st.write("-", item)

