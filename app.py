import streamlit as st
from src.pipelines.prediction_pipeline import PredictPipeline
import pandas as pd
st.header("Diamond Price Prediction")
def price_prediction():
    carat=st.text_input(label='',placeholder='Enter carat value(float)')
    depth=st.text_input(label='',placeholder='Enter depth value(float)')
    table=st.text_input(label='',placeholder='Enter table value(float)')
    x=st.text_input(label='',placeholder='Enter x value(float)')
    y=st.text_input(label='',placeholder='Enter y value(float)')
    z=st.text_input(label='',placeholder='Enter z value(float)')
    cut = st.selectbox(
        'Select cut',
        ('Ideal', 'Premium', 'Very Good','Good','Fair')
    )
    clarity=st.selectbox(
        'Select Clarity',
        ('SI1','VS2','VS1','SI2','VVS2','VVS1','IF','I1')
    )

    color=st.selectbox(
        'Select Color',
        ('D','E','F','G','H','I','J')
    )

    if st.button('Predict'):
        if carat and depth and table and x and y and z and cut and clarity and color:
        # Create a dictionary with user inputs
            data = {
                'carat': [float(carat)],
                'depth': [float(depth)],
                'table': [float(table)],
                'x': [float(x)],
                'y': [float(y)],
                'z': [float(z)],
                'cut': [cut],
                'clarity': [clarity],
                'color': [color]
            }

            # Create a DataFrame from the dictionary
            df = pd.DataFrame(data)
            st.write(df)
        else:
            st.warning("Please fill in all the fields.")
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(df)
        results=round(pred[0],2)
        return results
    
st.subheader(f"Predicted Diamond Price: {price_prediction()}")