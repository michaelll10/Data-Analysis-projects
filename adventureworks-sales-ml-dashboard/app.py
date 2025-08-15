
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df=pd.read_csv('adventureworks-sales-ml-dashboard/data.csv')
df_cleaned= pd.read_csv('adventureworks-sales-ml-dashboard/df_cleaned.csv')
df_orders=pd.read_csv('adventureworks-sales-ml-dashboard/df_orders.csv')
X_train_encoded=pd.read_csv('adventureworks-sales-ml-dashboard/train_cleaned_encoded.csv')
X_test_encoded=pd.read_csv('adventureworks-sales-ml-dashboard/test_cleaned_encoded.csv')



page = st.sidebar.selectbox("Choose a page", ["Data Overview", "Interactive Plots","Encoded Data"])

if page == "Data Overview":
    col1, col2 = st.columns(2)
    with col1:
        
        st.header('Data from AdventureWorks Internet Sales')
        st.dataframe(df)
        st.markdown("""
        ### Dataset Description
        This dataset contains internet sales order details from the AdventureWorksDW2019 database.
        
        **Key Points:**
        - Each row is a sales order line, including product, customer, and order information.
        - Customer demographics include Age, Gender, Marital Status, Yearly Income, and more.
        - Product information covers Product Name, Color, Class, and Product Line.
        - Financial details include Sales Amount, Tax Amount, Freight, and Total Paid.
        - Missing values in 'Class' are filled as 'Unknown'.
        - Outliers in numeric columns such as Age, Yearly Income, and Order Quantity have been clipped for better model stability.
        
        """)

    with col2:
        st.header("Data Summary Stats")
        st.write(f"Number of rows: {df.shape[0]}")
        st.write(f"Number of columns: {df.shape[1]}")
        st.write("Date range:")
        st.write(f"- Earliest Order Date: {df['OrderDate'].min()}")
        st.write(f"- Latest Order Date: {df['OrderDate'].max()}")
        st.write("Unique products:", df['EnglishProductName'].nunique())
        max_paid=df_orders['TotalPaid'].max()
        st.write(f"most paid customers: {df_orders['FullName'][df_orders['TotalPaid']==max_paid].head(10).tolist()} with Total Paid = {max_paid}")
        st.write("### Summary Statistics for Numeric Columns")
        st.write(df.describe())
        

    
    

elif page == "Interactive Plots":
    st.write("Interactive plots on Aggregated Orders Data")

    plot_type = st.selectbox("Select plot type", ["Bar Plot", "Scatter Plot", "Line Plot"])

    numeric_cols = df_cleaned.select_dtypes(include=np.number).columns.tolist()
    categorical_cols = df_cleaned.select_dtypes(include='object').columns.tolist()

    if plot_type == "Bar Plot":
        x_col = st.selectbox("Select X-axis (categorical)", categorical_cols)
        y_col = st.selectbox("Select Y-axis (numerical)", numeric_cols)
        agg_func = st.selectbox("Aggregation function", ["sum", "mean", "median", "count"])

        if st.button("Generate Plot"):
            if agg_func == "count":
                plot_data = df_cleaned.groupby(x_col).size().reset_index(name='count')
                y_col_to_plot = 'count'
            else:
                plot_data = df_cleaned.groupby(x_col)[y_col].agg(agg_func).reset_index()
                y_col_to_plot = y_col

            fig = px.bar(plot_data, x=x_col, y=y_col_to_plot, title=f"{agg_func.title()} of {y_col} by {x_col}")
            st.plotly_chart(fig)

    elif plot_type == "Scatter Plot":
        x_col = st.selectbox("Select X-axis (numerical)", numeric_cols, key="scatter_x")
        y_col = st.selectbox("Select Y-axis (numerical)", numeric_cols, key="scatter_y")
        color_col = st.selectbox("Color by (categorical)", [None] + categorical_cols)

        if st.button("Generate Plot"):
            fig = px.scatter(df_cleaned, x=x_col, y=y_col, color=color_col, title=f"{y_col} vs {x_col}")
            st.plotly_chart(fig)

    elif plot_type == "Line Plot":
        x_col = st.selectbox("Select X-axis (numerical or categorical)", numeric_cols + categorical_cols, key="line_x")
        y_col = st.selectbox("Select Y-axis (numerical)", numeric_cols, key="line_y")
        agg_func = st.selectbox("Aggregation function", ["sum", "mean", "median"], key="line_agg")

        if st.button("Generate Plot"):
            plot_data = df_cleaned.groupby(x_col)[y_col].agg(agg_func).reset_index()
            fig = px.line(plot_data, x=x_col, y=y_col, title=f"{agg_func.title()} of {y_col} by {x_col}")
            st.plotly_chart(fig)
            
            
elif page == "Encoded Data":
    st.header("Data After Encoding")

    st.write("### Encoded Training Data")
    st.dataframe(X_train_encoded)

    st.write("### Encoded Test Data")
    st.dataframe(X_test_encoded)

    st.write("### Summary Statistics")
    st.dataframe(X_train_encoded.describe())


