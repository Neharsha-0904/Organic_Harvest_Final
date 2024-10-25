import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data (replace with your actual data)
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [10000, 12000, 15000, 13000, 14000],
    'Profit': [2000, 2500, 3000, 2700, 2800],
    'Area': ['Punjab', 'Gujarat', 'Uttar Pradesh', 'Punjab', 'Gujarat'],
    'Crop': ['Wheat', 'Rice', 'Corn', 'Wheat', 'Rice'],
    'Farmer': ['Rahul', 'Sachin', 'Priya', 'Amit', 'Anjali'],
    'Season': ['Winter', 'Monsoon', 'Winter', 'Monsoon', 'Winter'],
    'Warehouse_Tonnage': [500, 600, 700, 650, 680]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Plot sales over time
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Month', y='Sales', marker='o')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# Plot profit over time
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Month', y='Profit', ci=None)
plt.title('Next Month Profit')
plt.xlabel('Month')
plt.ylabel('Profit')
plt.grid(True)
plt.show()

# Plot sales by area
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Area', y='Sales', ci=None)
plt.title('Sales by Area')
plt.xlabel('Area')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# Plot sales by crop
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Crop', y='Sales', ci=None)
plt.title('Sales by Crop')
plt.xlabel('Crop')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# Plot sales by farmer
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Farmer', y='Sales', ci=None)
plt.title('Sales by Farmer')
plt.xlabel('Farmer')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# Plot sales by season
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Season', y='Sales', ci=None)
plt.title('Sales by Season')
plt.xlabel('Season')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

# Plot warehouse tonnage over time
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Month', y='Warehouse_Tonnage', marker='o')
plt.title('Warehouse Tonnage Over Time')
plt.xlabel('Month')
plt.ylabel('Warehouse Tonnage')
plt.grid(True)
plt.show()
