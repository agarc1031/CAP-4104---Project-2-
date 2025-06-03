import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

# Title and Intro
st.title("Healthy Bites: Nutrition Info App")
st.subheader("Instant Nutrition Data & Health Ratings for Your Favorite Foods")
st.caption("Powered by the Nutritionix API")

# Sidebar
st.sidebar.header("Food Search")
food_item = st.sidebar.text_input("Enter a food:")
search = st.sidebar.button("Get Nutrition Info")

# Info box
st.info("This app provides calorie, sugar, fiber and other nutrient info. It also gives a gut health rating.")

# API credentials (replace with your own)
app_id = "YOUR_APP_ID"
app_key = "YOUR_APP_KEY"

# Function to get food data
def fetch_nutrition(food):
    url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    headers = {
        "x-app-id": app_id,
        "x-app-key": app_key,
        "Content-Type": "application/json"
    }
    data = {"query": food}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Function to calculate a health rating
def calculate_health_score(nutrient):
    fiber = nutrient.get("dietary_fiber", 0)
    sugar = nutrient.get("sugars", 0)
    score = min(fiber * 5, 25) + max(0, 20 - sugar)
    return max(0, min(100, score))

# Main App Logic
if search and food_item:
    try:
        result = fetch_nutrition(food_item)
        if "foods" in result:
            food = result["foods"][0]
            st.success(f"Results for '{food_item}'")

            # Show table
            df = pd.DataFrame({
                "Calories": [food["nf_calories"]],
                "Protein (g)": [food["nf_protein"]],
                "Sugar (g)": [food["nf_sugars"]],
                "Fiber (g)": [food["nf_dietary_fiber"]],
                "Fat (g)": [food["nf_total_fat"]]
            })
            st.dataframe(df)

            # Health score
            score = calculate_health_score(food)
            if score > 70:
                st.success(f"Health Score: {score} - Excellent")
            elif score > 40:
                st.warning(f"Health Score: {score} - Moderate")
            else:
                st.error(f"Health Score: {score} - Poor")

            # Chart
            chart_data = df.T.reset_index()
            chart_data.columns = ["Nutrient", "Amount"]
            st.bar_chart(chart_data.set_index("Nutrient"))

            # Optional checkbox
            if st.checkbox("Show raw JSON response"):
                st.json(food)

            # Feedback form
            st.markdown("### Rate this food")
            rating = st.slider("How healthy do you think it is?", 0, 100, score)
            comment = st.text_area("Leave a comment about this food:")
            if st.button("Submit Feedback"):
                st.success("Thanks for your feedback!")

        else:
            st.warning("No data found. Try a more specific food name.")

    except Exception as e:
        st.exception(e)
else:
    st.write("Enter a food in the sidebar and click 'Get Nutrition Info' to begin.")
