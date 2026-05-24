import matplotlib.pyplot as plt

def parity_plot(obs,pred,title):

    plt.scatter(
        obs,
        pred
    )

    plt.xlabel("Experimental qb")

    plt.ylabel("Predicted qb")

    plt.title(title)

    plt.show()
