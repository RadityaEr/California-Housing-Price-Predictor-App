# 🏡 California Housing Price Predictor App

A simple yet powerful web app built with **Streamlit** that predicts the median house value in California districts based on user-provided housing details. This project combines data preprocessing and a trained regression model (e.g., Random Forest or Gradient Boosting) into a deployable machine learning pipeline.

---

## 🔍 Features

- Interactive UI built using Streamlit
- Accepts multiple housing attributes as input
- Preprocessing and prediction using a trained ML pipeline
- Handles both numerical and categorical features
- Responsive layout with clean 2-column design
- Provides quick insight into housing market trends

---

## 📥 Input Features

| Feature               | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| Longitude            | The longitudinal coordinate of the location                                 |
| Latitude             | The latitudinal coordinate of the location                                  |
| Housing Median Age   | Median age of houses in the area                                            |
| Total Rooms          | Total rooms in the house's block                                            |
| Total Bedrooms       | Total bedrooms in the house's block                                         |
| Population           | Total population in the house's block                                       |
| Households           | Total households in the house's block                                       |
| Median Income        | Median income of residents in the area                                      |
| Ocean Proximity      | Categorical variable indicating proximity to the ocean                      |

> ℹ️ Note: The Total Rooms, Bedrooms, Population, and Households refer to values within the house's block, not a single unit.

---

## 🧠 Model Info

The app uses a `Pipeline` with:
- `StandardScaler` for numerical features
- `OneHotEncoder` for categorical features (`ocean_proximity`)
- A regression model such as `RandomForestRegressor` or `GradientBoostingRegressor`

---
