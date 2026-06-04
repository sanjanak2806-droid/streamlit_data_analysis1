import streamlit as st
import pandas as pd

from src.data_loader import load_data
from src.analysis import (
    get_basic_info,
    missing_values,
    statistical_summary
)

from src.visualization import (
    histogram,
    boxplot,
    scatter_plot,
    correlation_heatmap
)

st.set_page_config(
    page_title="Data Analysis Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Advanced Data Analysis Dashboard")

st.sidebar.header("Upload Dataset")

uploaded_file = st.sidebar.file_uploader(
    "Choose CSV or Excel File",
    type=["csv", "xlsx"]
)

if uploaded_file:

    df = load_data(uploaded_file)

    st.success("Dataset Loaded Successfully")

    st.header("Dataset Preview")

    st.dataframe(df.head())

    st.header("Dataset Information")

    info = get_basic_info(df)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Rows", info["Rows"])
    col2.metric("Columns", info["Columns"])
    col3.metric("Missing Values",
                info["Missing Values"])
    col4.metric("Duplicates",
                info["Duplicates"])

    st.divider()

    tab1, tab2, tab3, tab4 = st.tabs([
        "Overview",
        "Missing Values",
        "Statistics",
        "Visualizations"
    ])

    with tab1:

        st.subheader("Data Types")

        dtypes = pd.DataFrame({
            "Column": df.columns,
            "Datatype": df.dtypes.astype(str)
        })

        st.dataframe(dtypes)

    with tab2:

        st.subheader("Missing Value Analysis")

        mv = missing_values(df)

        st.dataframe(mv)

    with tab3:

        st.subheader("Statistical Summary")

        st.dataframe(
            statistical_summary(df)
        )

    with tab4:

        numeric_cols = list(
            df.select_dtypes(
                include="number"
            ).columns
        )

        if len(numeric_cols) > 0:

            st.subheader("Histogram")

            col = st.selectbox(
                "Select Column",
                numeric_cols
            )

            st.plotly_chart(
                histogram(df, col),
                use_container_width=True
            )

            st.subheader("Boxplot")

            st.plotly_chart(
                boxplot(df, col),
                use_container_width=True
            )

            if len(numeric_cols) >= 2:

                st.subheader(
                    "Scatter Plot"
                )

                x = st.selectbox(
                    "X Axis",
                    numeric_cols,
                    key="x"
                )

                y = st.selectbox(
                    "Y Axis",
                    numeric_cols,
                    key="y"
                )

                st.plotly_chart(
                    scatter_plot(df, x, y),
                    use_container_width=True
                )

            st.subheader(
                "Correlation Heatmap"
            )

            st.plotly_chart(
                correlation_heatmap(df),
                use_container_width=True
            )

else:

    st.info(
        "Upload a CSV or Excel file to begin analysis."
    )
