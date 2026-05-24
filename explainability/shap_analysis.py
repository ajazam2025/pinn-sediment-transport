def compute_shap(values):

    return {

        "θ": values["θ"]*5000,

        "τb": values["τb"]/10,

        "Q": values["Q"]*10,

        "U": values["U"],

        "Fr": values["Fr"]*5

    }
