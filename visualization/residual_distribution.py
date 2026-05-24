mport matplotlib.pyplot as plt
import seaborn as sns

def residual_plot(obs,pred):

    residual = obs - pred

    sns.histplot(
        residual,
        kde=True
    )

    plt.xlabel("Residual")

    plt.ylabel("Frequency")

    plt.show()
