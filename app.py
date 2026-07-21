import streamlit as st

from src.optimizer import solve_optimization

st.set_page_config(
    page_title="Operational Optimization Solver",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Operational Optimization Solver")

st.subheader("Business Inputs")

workers = st.slider(
    "Available Workers",
    1,
    20,
    10
)

budget = st.slider(
    "Available Budget",
    1000,
    10000,
    5000
)

profit = st.slider(
    "Profit per Unit",
    10,
    200,
    80
)

labor_cost = st.slider(
    "Labor Cost per Unit",
    10,
    100,
    30
)

capacity = st.slider(
    "Maximum Units per Worker",
    1,
    20,
    8
)

if st.button("Optimize"):

    result = solve_optimization(
        workers,
        budget,
        profit,
        labor_cost,
        capacity
    )

    st.success("Optimization Complete")

    st.write(result)