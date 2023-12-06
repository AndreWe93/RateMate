import streamlit as st
import requests


# ####### TO Dos #########
# """
# 1. Show the original score
# 2. Show the subratings from the dataset
# 3. Integrate the Word cloud picture from my notebook somehow into the streamlit app
# 4. Add more features
# """


st.snow()

st.markdown("""# RateMate
## Get your personal rating for the restaurant of your choice
Hello friend, please insert the google maps url of the restaurant you are interested in:""")

url = st.text_input("url of your restaurant")

# the selected value is returned by st.slider
price_review_weightage = st.slider('Select your price rating weight', 0.0, 1.0, 0.25)
food_review_weightage = st.slider('Select your food rating weight', 0.0, 1.0, 0.25)
service_review_weightage = st.slider('Select your service rating weight', 0.0, 1.0, 0.25)
ambience_review_weightage = st.slider('Select your ambience rating weight', 0.0, 1.0, 0.25)

# checkbox for local guides
local_guides_review_weightage = st.checkbox('Review only from local guides')

if st.button("Get Score"):

    params = {
            'url': url,
            'price_review_weightage': price_review_weightage,
            'food_review_weightage': food_review_weightage,
            'service_review_weightage': service_review_weightage,
            'ambience_review_weightage': ambience_review_weightage,
            'local_guides_review_weightage': local_guides_review_weightage
            }


    ratemate_api_url = 'http://127.0.0.1:8000/personal_score'
    response = requests.get(ratemate_api_url, params=params)

    # original_score = response.json()
    your_personal_score = response.json()["personal_score"]
    top_1_review = response.json()["top_1"]
    top_2_review = response.json()["top_2"]
    top_3_review = response.json()["top_3"]

    st.divider()

    #st.header(f'Restuarant Rating: ⭐️ {original_score} ⭐️')
    st.header(f'⭐️ Your personal score is: {your_personal_score} ⭐️')
    st.header("Here are the reviews of the most active reviewers")
    st.markdown(f'Top 1: {top_1_review}')
    st.markdown(f'Top 2: {top_2_review}')
    st.markdown(f'Top 3: {top_3_review}')
