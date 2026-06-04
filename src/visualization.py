import plotly.express as px
import pandas as pd

def histogram(df, column):

    fig = px.histogram(
        df,
        x=column,
        title=f"Distribution of {column}"
    )

    return fig


def boxplot(df, column):

    fig = px.box(
        df,
        y=column,
        title=f"Boxplot of {column}"
    )

    return fig


def scatter_plot(df, x, y):

    fig = px.scatter(
        df,
        x=x,
        y=y,
        title=f"{x} vs {y}"
    )

    return fig


def correlation_heatmap(df):

    numeric_df = df.select_dtypes(
        include=["number"]
    )

    corr = numeric_df.corr()

    fig = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="RdBu_r",
        title="Correlation Heatmap"
    )

    return fig
