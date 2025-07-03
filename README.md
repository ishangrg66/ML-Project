# 🚦 Traffic Congestion Level Predictor

A beginner-friendly machine learning project that predicts traffic congestion levels (Low, Medium, High) based on factors like time of day, day type, weather conditions, road type, vehicle count, number of lanes, and vehicle mix.

This project includes:
- A trained **Random Forest Classifier**
- A clean **manual hyperparameter tuning approach**
- An interactive **Streamlit web interface**
- A synthetic but realistic dataset designed for learning and demonstration

---

## 📊 Features

- Predicts traffic congestion level based on 7 user-input features
- Fully interactive web app built with Streamlit
- Easy to extend or connect to real-time traffic APIs
- Clean codebase suitable for beginners and students

---

## 🛠️ Tech Stack

- **Python 3**
- **scikit-learn** – model training
- **pandas** – data handling
- **joblib** – model saving/loading
- **Streamlit** – web UI
- **matplotlib/seaborn** – optional visualizations

---

## 📁 Project Structure

📦 ML_PROJECT/
├── app.py # Streamlit web app
├── traffic_model.pkl # Trained model
├── traffic_data.csv # Synthetic dataset
├── requirement.txt # Python dependencies
└── README.md # You're reading this file


## Install dependencies -  pip install -r requirements.txt

## Run the streamlit app - streamlit run app.py


---


## 🧠 How It Works
Data Preparation: The dataset includes road and traffic-related features.

Manual Label Encoding: All categorical values are encoded manually to keep things beginner-friendly.

Model Training: A RandomForestClassifier is trained using scikit-learn.

Manual Hyperparameter Tuning: Different values of n_estimators and max_depth are tried manually.

Model Saving: The best model is saved using joblib.

Web App: Users enter values via Streamlit and instantly receive a congestion prediction.


---


## ✨ Sample Inputs in UI

- Time of Day: **Morning, Afternoon, Evening, Night**

- Day Type: **Weekday or Weekend**

- Weather: **Sunny, Rainy, Foggy, Snowy**

- Road Type: **Highway, Local, One-way, Mountain**

- Vehicle Count:**e.g. 150**

- Road Lanes: **e.g. 2**

- Vehicle Mix Ratio: **Slider from 0.0 to 1.0**


---


## 🙌 Acknowledgements
This project was created as part of a learning journey in machine learning and Python development. It is meant to be simple, educational, and extendable.
