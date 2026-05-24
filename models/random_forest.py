from sklearn.ensemble import RandomForestRegressor

def build_rf():

    return RandomForestRegressor(
        n_estimators=300,
        random_state=25
    )
