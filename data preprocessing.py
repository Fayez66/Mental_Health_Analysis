import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

# Load the dataset
file_path = r"D:\Desktop\anxiety_depression_data.xlsx" # Update this with the actual file path
df = pd.read_excel(file_path)

# Display initial dataset info
print("Initial Data Info:")
print(df.info())

# Handling missing values
df.fillna(method='ffill', inplace=True)  # Forward fill missing values

# Removing duplicate rows
df.drop_duplicates(inplace=True)

# Convert categorical columns to numeric
categorical_cols = ['Gender', 'Education_Level', 'Employment_Status', 
                    'Medication_Use', 'Therapy', 'Meditation', 'Substance_Use']

label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le  # Store encoders for future use

# Normalize numerical columns
numerical_cols = ['Age', 'Sleep_Hours', 'Physical_Activity_Hrs', 
                  'Social_Support_Score', 'Anxiety_Score', 'Depression_Score',
                  'Stress_Level', 'Financial_Stress', 'Work_Stress', 
                  'Self_Esteem_Score', 'Life_Satisfaction_Score', 'Loneliness_Score']

scaler = MinMaxScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

# Display cleaned data info
print("\nCleaned Data Info:")
print(df.info())

# Save the cleaned dataset
cleaned_file_path = "cleaned_data.xlsx"
df.to_excel(cleaned_file_path, index=False)

print(f"\nData cleaning and normalization completed. File saved as {cleaned_file_path}")
