"""
This script demonstrates DataFrame operations using pandas:
- Creates a sample DataFrame
- Adds a bonus column
- Filters data based on age
- Groups data by age brackets and calculates averages

Required packages:
- pandas (install with: uv add pandas)
"""

import pandas as pd
import numpy as np # Galus note: Useless import.

def process_employee_data():
    """
    Creates and processes employee data using pandas DataFrame operations.

    Returns:
        tuple: Contains the processed DataFrame and age-grouped statistics
    """
    # Create sample data
    data = {
        'Name': ['John', 'Alice', 'Bob', 'Carol', 'David', 'Eve', 'Frank', 'Grace'],
        'Age': [25, 32, 45, 28, 35, 41, 52, 38],
        'Salary': [50000, 65000, 85000, 48000, 70000, 75000, 95000, 72000]
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Add Bonus column (10% of Salary)
    df['Bonus'] = df['Salary'] * 0.10

    # Filter for age > 30
    filtered_df = df[df['Age'] > 30]

    # Create age brackets
    def age_bracket(age):
        return f"{(age // 10) * 10}s"

    # Add age bracket column
    filtered_df['Age_Bracket'] = filtered_df['Age'].apply(age_bracket)

    # Group by age bracket and calculate means
    grouped_stats = filtered_df.groupby('Age_Bracket').agg({
        'Salary': 'mean',
        'Bonus': 'mean'
    }).round(2)

    return filtered_df, grouped_stats

def main():
    # Process the data
    filtered_df, grouped_stats = process_employee_data()

    # Display results
    print("Filtered Employee Data (Age > 30):")
    print("=" * 60)
    print(filtered_df)
    print("\nAverage Salary and Bonus by Age Bracket:")
    print("=" * 60)
    print(grouped_stats)

if __name__ == "__main__":
    main()
