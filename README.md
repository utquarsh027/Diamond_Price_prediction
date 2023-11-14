# Diamond Price Prediction Project

## Introduction

This project aims to predict the price of diamonds using regression analysis. The dataset contains various attributes of diamonds that can influence their price.

## About the Data

The dataset includes the following independent variables:

- **id**: Unique identifier for each diamond.
- **carat**: Weight measurement exclusive to gemstones and diamonds (Carat - ct.).
- **cut**: Quality of the diamond cut.
- **color**: Color grade of the diamond.
- **clarity**: Measure of the purity and rarity of the diamond.
- **depth**: Height of the diamond (in millimeters) from the culet to the table.
- **table**: Facet visible when the stone is viewed face up.
- **x**: Diamond X dimension.
- **y**: Diamond Y dimension.
- **z**: Diamond Z dimension.

### Target Variable

- **price**: Price of the given diamond.

## Data Source

The dataset used in this project is sourced from kaggle.

## Project Workflow

1. **Data Exploration**: Understanding the dataset, checking for missing values, and exploring statistical summaries.
2. **Data Preprocessing**: Handling missing values, encoding categorical variables, and scaling numerical features if required.
3. **Feature Engineering**: Creating new features or transforming existing ones to improve model performance.
4. **Model Building**: Training and evaluating regression models to predict diamond prices.
5. **Model Evaluation**: Assessing model performance using appropriate metrics and validation techniques.
6. **Deployment**: The model is deployed and available [here](https://diamondpriceprediction-yqxo7hcgsmrluosbx2pwsq.streamlit.app/).


## Instructions

1. Clone the repository.
2. Install the required dependencies (`requirements.txt`).
3. Run the `app.py` file.
