import streamlit as st

# Step 1: Define translations
translations = {
    'English': {
        'title': 'The Bread 🍞',
        'bread_flour': 'Bread Flour',
        'hydratation': 'Hydration (%)',
        'ingredients': 'Ingredients',
        'instructions': 'Instructions',
        'bread_weight': 'Bread Weight: {} g'
    },
    'Czech': {
        'title': 'Chléb 🍞',
        'bread_flour': 'Chlebová mouka',
        'hydratation': 'Hydratace (%)',
        'ingredients': 'Ingredience',
        'instructions': 'Instrukce',
        'bread_weight': 'Váha chleba: {} g'
    }
}

# Step 2: Language selection
language = st.selectbox('Choose your language', options=['English', 'Czech'])

# Use the selected language for labels
labels = translations[language]

# App content using translations
st.title(labels['title'])

bread_flour = st.number_input(labels['bread_flour'], value=500, step=50)
hydratation = st.number_input(labels['hydratation'], value=75, step=5)

water = bread_flour * hydratation / 100
salt = bread_flour * 0.02
starter = bread_flour * 0.15

overall_weight = bread_flour + water + salt + starter

st.header(labels['ingredients'])
st.write(f"""
 - **{bread_flour:.0f}g** bread flour
 - **{water:.0f}g** water
 - **{starter:.0f}g** sourdough starter
 - **{salt:.0f}g** salt""")




st.write(labels['bread_weight'].format(overall_weight))

st.header(labels['instructions'])

st.write("Mix all the ingredients together and let the dough rest for 12 hours. ")
 