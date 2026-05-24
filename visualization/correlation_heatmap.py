import seaborn as sns
import matplotlib.pyplot as plt

def heatmap(df):

    sns.heatmap(
        df.corr(),
        cmap="coolwarm",
        annot=True
    )

    plt.show()
