import numpy as np

def predict_mpm(theta):

    theta_eff = np.maximum(
        theta - 0.047,
        0
    )

    qb = 8 * (
        theta_eff ** 1.5
    )

    return qb
