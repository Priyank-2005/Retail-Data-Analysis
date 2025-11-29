import streamlit as st
import pandas as pd

# 1. Page Config (Tab Title)
st.set_page_config(page_title="Retail Insights", layout="wide")

# 2. Title
st.title("Global Retail Performance Dashboard")
st.markdown("---")

# 3. Load Data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("orders.csv", encoding='utf-8')
    except UnicodeDecodeError:
        df = pd.read_csv("orders.csv", encoding='ISO-8859-1')
    
    # Standardize column names
    df.columns = df.columns.str.replace(' ', '_').str.lower()
    
    # Convert date column to datetime objects (Crucial for charts)
    if 'order_date' in df.columns:
        df['order_date'] = pd.to_datetime(df['order_date'])
        
    return df

try:
    df = load_data()
    
    # 4. Find the Right Columns for Math
    # We look for specific keywords usually found in retail data
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    
    sales_col = next((col for col in numeric_cols if 'sale' in col or 'price' in col), None)
    profit_col = next((col for col in numeric_cols if 'profit' in col), None)
    qty_col = next((col for col in numeric_cols if 'quantity' in col), None)

    # 5. KPI Section
    st.subheader("Key Metrics")
    col1, col2, col3 = st.columns(3)
    
    # KPI 1: Total Revenue (if sales column exists)
    if sales_col:
        total_sales = df[sales_col].sum()
        col1.metric("Total Revenue", f"${total_sales:,.0f}")
    else:
        col1.metric("Total Orders", len(df))

    # KPI 2: Average Profit (if profit column exists)
    if profit_col:
        total_profit = df[profit_col].sum()
        col2.metric("Total Profit", f"${total_profit:,.0f}")
    elif sales_col:
        avg_sale = df[sales_col].mean()
        col2.metric("Avg. Order Value", f"${avg_sale:,.2f}")

    # KPI 3: Total Quantity
    if qty_col:
        total_qty = df[qty_col].sum()
        col3.metric("Units Sold", f"{total_qty:,.0f}")
    else:
        col3.metric("Records Analyzed", len(df))

    st.markdown("---")

    # 6. Charts Section
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Sales Trends")
        if 'order_date' in df.columns and sales_col:
            # Group by Month to make the chart readable
            monthly_sales = df.set_index('order_date').resample('M')[sales_col].sum()
            st.line_chart(monthly_sales)
        else:
            st.warning("Could not identify Date or Sales columns for trend analysis.")

    with col_right:
        st.subheader("Top Performing Categories")
        # Find a categorical column (like 'Category' or 'Sub-Category')
        cat_col = next((col for col in df.columns if 'category' in col), None)
        
        if cat_col and sales_col:
            top_cats = df.groupby(cat_col)[sales_col].sum().sort_values(ascending=False).head(5)
            st.bar_chart(top_cats)
        else:
            st.write("Could not identify Category information.")

    # 7. Raw Data Toggle
    with st.expander("View Raw Data"):
        st.dataframe(df.head(100))
    
except Exception as e:
    st.error(f"Error loading data: {e}")