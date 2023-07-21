import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Read kazpop.csv
data = pd.read_csv('archive/kazpop.csv')

# Group the data by 'Область' (area names)
grouped_data = data.groupby('Область')

# Create dictionaries to store the models and predictions for each area
models = {}
predictions = {}

# Loop through each area, create and train the model, and make predictions
for area, area_data in grouped_data:
    X = area_data['Год'].values.reshape(-1, 1)
    y = area_data['Население'].values

    # Create the Linear Regression model
    model = LinearRegression()

    # Train the model on the data
    model.fit(X, y)

    # Store the model in the 'models' dictionary
    models[area] = model

    # Create a range of future years from 2024 to 2050
    future_years = np.arange(2024, 2051).reshape(-1, 1)

    # Predict populations for the future years
    predicted_populations = model.predict(future_years)

    # Store the predictions in the 'predictions' dictionary
    predictions[area] = predicted_populations

# Create a new DataFrame to store the predictions
predictions_df = pd.DataFrame()

# Add 'Год' (year) column with future years from 2024 to 2050
predictions_df['Год'] = np.arange(2024, 2051)

# Loop through each area, append the corresponding predictions to the DataFrame
for area, area_data in grouped_data:
    area_predictions = predictions[area]
    predictions_df[area] = area_predictions

# Append the new predictions to the original data
predictions_df = predictions_df.melt(id_vars='Год', var_name='Область', value_name='Население')
combined_df = pd.concat([data, predictions_df], ignore_index=True)

df_sorted = combined_df.sort_values(by=['Год'])

# Export to csv_final.csv
df_sorted.to_csv('data/csv_final.csv')
