python
import pandas as pd
import plotly.express as px

def load_data(file_path):
    # Load dataset into pandas DataFrame
    return pd.read_excel(file_path)

def calculate_metrics(df):
    # Calculate required metrics
    df['Net Value'] = df['Buy Value'] - df['Sell Value']
    df['Net Volume'] = df['Buy Volume'] - df['Sell Volume']
    df['Net Trades'] = df['Buy Trades'] - df['Sell Trades']
    return df

def visualize_data(df):
    # Example visualization: Bar chart for Total Trading Volume by Category
    fig = px.bar(df, x='Category', y='Total Volume', color='Category', title='Total Trading Volume by Category')
    fig.show()

def main():
    # File path to the dataset
    file_path = 'Ownership_Trading_Summary_FEB.xlsx'

    # Load and preprocess data
    data = load_data(file_path)
    processed_data = calculate_metrics(data)

    # Generate visualizations
    visualize_data(processed_data)

if __name__ == '__main__':
    main()
