import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

from roque_cmap import cmap, roque


def test_roque():
    colors = roque()
    assert len(colors) == 256


def test_roque_128():
    colors = roque(128)
    assert len(colors) == 128


def test_matplotlib_cmap():
    assert isinstance(cmap(), LinearSegmentedColormap)

    fig, ax = plt.subplots()
    ax.imshow([[0, 1], [0, 1]], cmap=cmap())
    plt.close(fig)


def test_seaborn_pallete():
    glue = sns.load_dataset("glue").pivot(index="Model", columns="Task", values="Score")
    # Your test code here
    sns.heatmap(glue, cmap=cmap())
