import streamlit as st
import pandas as pd
from datetime import timedelta

def simple_period_predictor(cycle_data):
    # Convert to datetime
    cycle_data['cycle_start_date'] = pd.to_datetime(cycle_data['cycle_start_date'])
    
    # Calculate average cycle length
    avg_cycle_length = cycle_data['cycle_length'].mean()
    
    # Last period start date
    last_period = cycle_data['cycle_start_date'].max()
    
    # Predict next period start date
    predicted_next_period = last_period + timedelta(days=int(round(avg_cycle_length)))
    
    # Predict ovulation date (approx 14 days before next period)
    predicted_ovulation = predicted_next_period - timedelta(days=14)
    
    return {
        'average_cycle_length': avg_cycle_length,
        'last_period_start': last_period.date(),
        'predicted_next_period_start': predicted_next_period.date(),
        'predicted_ovulation_date': predicted_ovulation.date()
    }

def main():
    st.title("Simple Period & Ovulation Predictor")

    uploaded_file = st.file_uploader("Upload CSV with columns: 'cycle_start_date' and 'cycle_length'", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader("Your Cycle History Data")
        st.write(df)

        predictions = simple_period_predictor(df)
        
        st.subheader("Predictions")
        st.write(f"Average Cycle Length: {predictions['average_cycle_length']:.2f} days")
        st.write(f"Last Period Start Date: {predictions['last_period_start']}")
        st.write(f"Predicted Next Period Start Date: {predictions['predicted_next_period_start']}")
        st.write(f"Predicted Ovulation Date: {predictions['predicted_ovulation_date']}")
    else:
        st.info("Please upload a CSV file to see predictions.")

if __name__ == "__main__":
    main()
