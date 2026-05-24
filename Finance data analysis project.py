# ============================================
# FINANCE DATA ANALYSIS PROJECT
# Stock Market Analysis Using Python
# ============================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------
# STEP 1: LOAD DATASET
# --------------------------------------------

# Replace with your dataset file name
df = pd.read_csv(r"C:/Users/VINOTHINI/Downloads/random_stock_market_dataset.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# --------------------------------------------
# STEP 2: DATA CLEANING
# --------------------------------------------

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove missing values
df.dropna(inplace=True)

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# --------------------------------------------
# STEP 3: BASIC INFORMATION
# --------------------------------------------

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# --------------------------------------------
# STEP 4: VISUALIZATION
# --------------------------------------------

# Line Chart - Closing Price Trend
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Close'])
plt.title("Stock Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.grid(True)
plt.show()

# --------------------------------------------
# STEP 5: MOVING AVERAGE
# --------------------------------------------

# Create 30-day moving average
df['Moving_Avg_30'] = df['Close'].rolling(window=30).mean()

# Plot Closing Price and Moving Average
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Close'], label='Closing Price')
plt.plot(df['Date'], df['Moving_Avg_30'], label='30-Day Moving Average')

plt.title("Stock Price with Moving Average")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.show()

# --------------------------------------------
# STEP 6: DAILY RETURNS
# --------------------------------------------

# Calculate daily returns
df['Daily_Return'] = df['Close'].pct_change()

# Plot Daily Returns
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Daily_Return'])

plt.title("Daily Returns")
plt.xlabel("Date")
plt.ylabel("Return")
plt.grid(True)
plt.show()

# --------------------------------------------
# STEP 7: CONCLUSION
# --------------------------------------------

print("\nProject Completed Successfully!")
print("This project analyzed stock market trends,")
print("moving averages, and daily returns.")
