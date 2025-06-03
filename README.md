# Welcome to Our App, Healthy Bites!

Designed with Streamlit, Healthy Bites lets users search for any food item and view comprehensive nutritional information driven by the Nutritionix API.  The app shows calories, sugar, fiber, fat, protein, and a personalized health score based on nutrient data, therefore guiding users in making better food decisions.

Healthy Bites is designed for individuals who value their nutrition and need quick access to food statistics. This includes consumers attempting to eat healthier, people with dietary issues such as diabetes or IBS, and fitness enthusiasts. The app is designed to deliver an instructive, simple, and visual experience to its users by giving them a health score and nutrient breakdown they can quickly understand. 

The goal of Healthy Bites is to give its users quick and easy access to nutritional facts so that they can make better health choices when it comes to their food. The health score and nutritional images help to simplify complicated data, therefore defining the purpose of the app from the moment it is launched. The app's focus on health education and quick insights directly serves the needs of its audience. 


![giphy ](https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmpvaGp3bXZmNWoyOTJnZzZteGR4dGphcmJ5bDVneGlpZ2I3ZXltbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MXiWqZBY45qiJ818nX/giphy.gif)

## Key Features
- 🔍 Search for any food item, such as "apple" or "cheeseburger"
- 📊 View important nutritional information in a table
- 📈 Visualize your nitrients with bar charts
- ✅ Receive an instant health score (0–100)
- 🧠 Rate the food and leave remarks
- ✅ Messages on success, caution, and mistakes depending on food health score
- 📦 Option to display raw JSON response from the API
- 🎨 Streamlit widgets: text input, buttons, sliders, checkbox, text area, charts

## How to Install and Run the Automated Usability Testing App
### For Windows Users: 
1. Clone the Repository
  - git clone https://github.com/yourusername/healthy-bites.git
    cd healthy-bites
2. Install Python 3.9 or later
  - Download from: https://www.python.org/downloads/
  - Make sure to check the box that says "Add Python to PATH" during installation.
3. Install Dependencies Open Command Prompt:
  - pip install -r requirements.txt
  - Or manually: pip install streamlit pandas requests matplotlib
4. Add Your API Credentials
  - Go to https://developer.nutritionix.com/
  - Create a free account and get your App ID and App Key
  - Open app.py and replace the placeholders:
      - app_id = "YOUR_APP_ID"
      - app_key = "YOUR_APP_KEY"
5. Run the App
  - streamlit run app.py

### For macOS Users:
1. Open Terminal and Clone the Repository
- git clone https://github.com/yourusername/healthy-bites.git
  cd healthy-bites
2. Install Python 3.9 or later (via Homebrew or Python.org)
- brew install python
- Or download directly from https://www.python.org/downloads/mac-osx/
3. Install Dependencies
- pip3 install -r requirements.txt
- Or manually:
  pip3 install streamlit pandas requests matplotlib
4. Add Your API Credentials
- Sign up at https://developer.nutritionix.com/
- Copy your App ID and App Key
- Open app.py and update:
  app_id = "YOUR_APP_ID"
  app_key = "YOUR_APP_KEY"
5. Run the App
- streamlit run app.py
## Healthy Bites Demo: 
👉
