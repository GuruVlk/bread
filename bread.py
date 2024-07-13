import streamlit as st

# Step 1: Define translations
translations = {
    'English': {
        'title': 'The Bread 🍞',
        'bread_flour': 'Bread Flour',
        'hydratation': 'Hydration (%)',
        'ingredients': 'Ingredients',
        'instructions': 'Instructions',
        'bread_weight': 'Bread Weight: {} g',
        "salt": "Salt",
        "starter": "Sauerdough Starter",
        "water": "Water"
    },
    'Czech': {
        'title': 'Chléb 🍞',
        'bread_flour': 'Chlebová mouka',
        'hydratation': 'Hydratace (%)',
        'ingredients': 'Ingredience',
        'instructions': 'Instrukce',
        'bread_weight': 'Váha chleba: {} g',
        "salt": "Sůl",
        "starter": "Kvásek",
        "water": "Voda"
        
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
- **{bread_flour:.0f}g** {labels['bread_flour']}
- **{water:.0f}g** {labels['water']}
- **{starter:.0f}g** {labels['starter']}
- **{salt:.0f}g** {labels['salt']}
""")

st.write(labels['bread_weight'].format(overall_weight))

st.header(labels['instructions'])

st.write("""
         Plase noote that every oven baked differently. You may need to adjust the temperature and time based on your oven.
         Every flour is different, you may need to adjust the hydration based on the flour you are using.
         Every starter is different, you may need to adjust the amount of starter based on the starter you are using.

         - Mix all the ingredients together and wait for 30 minutes
         - First **Coil Fold** Method
            - Fold and wait for 30 minutes
            - Fold and wait for 30 minutes
            - Fold and wait for 30 minutes
         - Then **Strech and fold** Method
            - Fold and wait for 45 minutes
            - Fold and wait for 45 minutes
            - Fold and wait for 45 minutes
            - Based on the srength of the dough, you can repeat the **Strech and fold** Method
         - Pre-shape the dough and put it to basket
            - Wait for 1 hour
         - Put the dough to the fridge for 12-18 hours (overnight)
         - Prehat the oven to 245°C
         - Bake the bread for 20 minutes with the lid on
         - Bake the bread for 20 minutes with the lid off

         """)
 