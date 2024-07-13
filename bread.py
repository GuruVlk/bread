import streamlit as st

# Step 1: Define translations
translations = {
    'English': {
        'title': 'Sauerdough Bread 🍞',
        'bread_flour': 'Bread Flour',
        'hydratation': 'Hydration (%)',
        'ingredients': 'Ingredients',
        'instructions': 'Instructions',
        'bread_weight': 'Bread Weight: {} g',
        "salt": "Salt",
        "starter": "Sauerdough Starter",
        "water": "Water",
        "Hydratation60": "60% - 70% Medium hydration dough is easy to handle - not so fluffy bread",
        "Hydratation70": "70% - 80% is the best range for hydration and fluffy bread",
        "Hydratation80": "80% - 100% High hydration dough is sticky and hard to handle - cibatta bread is made with this dough",
        'instructions_description': """
Plase note that every oven bakes differently. You may need to adjust the temperature and time based on your oven.
Every flour is different, you may need to adjust the hydration based on the flour you are using.
Every starter is different, you may need to adjust the amount of starter based on the starter you are using.

- Mix all the ingredients together and wait for 30 minutes
- First **Coil Fold** Method
   - Fold and wait for 30 minutes
   - Fold and wait for 30 minutes
   - Fold and wait for 30 minutes
- Then **Stretch and Fold** Method
   - Fold and wait for 45 minutes
   - Fold and wait for 45 minutes
   - Fold and wait for 45 minutes
   - Based on the strength of the dough, you can repeat the **Stretch and Fold** Method
- Pre-shape the dough and put it into a basket
   - Wait for 1 hour
- Put the dough into the fridge for 12-18 hours (overnight)
- Remove the dough from the fridge and place it to the french oven and make a cut on the top
- Preheat the oven to 245°C
- Bake the bread for 20 minutes with the lid on
- Bake the bread for 20 minutes with the lid off
"""
    },
    'Czech': {
        'title': 'Kváskový Chléb 🍞',
        'bread_flour': 'Chlebová mouka',
        'hydratation': 'Hydratace (%)',
        'ingredients': 'Ingredience',
        'instructions': 'Instrukce',
        'bread_weight': 'Váha chleba: {} g',
        "salt": "Sůl",
        "starter": "Kvásek",
        "Hydratation60": "60% - 70% Středně hydratované těsto je snadno ovladatelné - ne tak nadýchaný chléb",
        "Hydratation70": "70% - 80% je nejlepší rozsah pro hydrataci a nadýchaný chléb",
        "Hydratation80": "80% - 100% Vysoká hydratace těsta je lepkavá a těžko se s ní manipuluje - cibatta chléb je vyroben z tohoto těsta",
        "water": "Voda",
            'instructions_description': """
**Vezměte prosím na vědomí, že každá trouba peče jinak.** Možná bude potřeba upravit teplotu a čas podle vaší trouby.
Každá mouka je jiná, možná bude potřeba upravit hydrataci podle použité mouky.
Každý kvásek je jiný, možná bude potřeba upravit množství kvásku podle použitého kvásku.

- Smíchejte všechny ingredience dohromady a počkejte 30 minut
- První metoda **Coil Fold**
   - Složte a počkejte 30 minut
   - Složte a počkejte 30 minut
   - Složte a počkejte 30 minut
- Poté metoda **Stretch and Fold**
   - Složte a počkejte 45 minut
   - Složte a počkejte 45 minut
   - Složte a počkejte 45 minut
   - Podle síly těsta můžete opakovat metodu **Stretch and Fold**
- Předtvarujte těsto a vložte ho do košíku
   - Počkejte 1 hodinu
- Vložte těsto do lednice na 12-18 hodin (přes noc)
- Předehřejte troubu na 245°C
- Pečte chléb 20 minut s pokličkou
- Pečte chléb 20 minut bez pokličky
"""
        
    }
}

# Step 2: Language selection
# language = st.selectbox('Choose your language', options=['English', 'Czech'])

language_opt = st.toggle('Czech', False)
if language_opt:
    language = 'Czech'
else:
    language = 'English'


# Use the selected language for labels
labels = translations[language]

# App content using translations
st.title(labels['title'])

bread_flour = st.number_input(labels['bread_flour'], value=500, step=100)
hydratation = st.slider(labels["hydratation"] , 60, 100, 70, 5, )

if hydratation >= 80:
    st.warning(labels['Hydratation80'])
elif hydratation >=70:
    st.success(labels['Hydratation70'])
elif hydratation >=60:
    st.info(labels['Hydratation60'])

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

st.subheader(labels['bread_weight'].format(overall_weight))

st.divider()

st.header(labels['instructions'])

st.write(labels['instructions_description'])
 

