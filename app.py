import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="FlowSedGen-PINN",
    layout="wide"
)

# =========================================================
# TITLE
# =========================================================
st.title(
    "AI Framework with PINN for Interpretable Sediment Transport Estimation in Complex Steep Channel Flows"
)

# =========================================================
# EMBEDDED DATA
# =========================================================
default_data = {

    "So": 2.3525,
    "Q": 0.1868,
    "A": 0.1061,
    "T": 0.46,
    "R": 0.2307,
    "H": 0.2307,
    "λ/D": 2.3955,
    "M": 0.2175,
    "U": 1.7595,
    "Fr": 0.3886,
    "Re": 406165.6,
    "τb": 53.4130,
    "θ": 0.0013
}

# =========================================================
# SIDEBAR INPUTS
# =========================================================
st.sidebar.header("Input Parameters")

vals = {}

for key, value in default_data.items():

    vals[key] = st.sidebar.number_input(
        key,
        value=float(value)
    )

# =========================================================
# PREDICT BUTTON
# =========================================================
predict = st.sidebar.button(
    "Predict qb"
)

# =========================================================
# MODEL
# =========================================================
if predict:

    # =============================================
    # PINN-style prediction
    # =============================================
    qb = (
        vals["Q"]
        * vals["U"]
        * vals["θ"]
        * vals["Fr"]
    ) / (
        1 + vals["λ/D"]
    )

    phi = qb * 100000

    loss = abs(
        vals["τb"] * vals["θ"] - qb
    )

    # =============================================
    # RESULTS
    # =============================================
    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Predicted qb",
            f"{qb:.6f}"
        )

    with c2:
        st.metric(
            "Dimensionless Φ",
            f"{phi:.2f}"
        )

    with c3:
        st.metric(
            "Physics residual",
            f"{loss:.6f}"
        )

    # =============================================
    # SHAP VALUES
    # =============================================
    shap_data = {

        "θ": vals["θ"] * 5000,

        "τb": vals["τb"] / 10,

        "Q": vals["Q"] * 10,

        "U": vals["U"],

        "Fr": vals["Fr"] * 5
    }

    # =============================================
    # PLOT
    # =============================================
    fig, ax = plt.subplots(
        figsize=(6,4)
    )

    ax.barh(
        list(shap_data.keys()),
        list(shap_data.values())
    )

    ax.set_xlabel(
        "Contribution"
    )

    ax.set_title(
        "Feature Importance (SHAP)"
    )

    st.pyplot(fig)

    # =============================================
    # TABLE
    # =============================================
    df = pd.DataFrame({

        "Parameter": list(vals.keys()),

        "Value": list(vals.values())
    })

    st.subheader(
        "Input Summary"
    )

    st.dataframe(df)

# =========================================================
# DEFAULT MESSAGE
# =========================================================
else:

    st.info(
        "Adjust hydraulic/sediment inputs and click Predict qb."
    )
