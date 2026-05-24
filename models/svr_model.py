from sklearn.svm import SVR

def build_svr():

    return SVR(
        kernel='rbf',
        C=50,
        gamma=0.05
    )
