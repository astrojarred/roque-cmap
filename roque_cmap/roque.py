import importlib.resources as pkg_resources
import pickle
from math import ceil


def roque_generator(n_colors=256):
    """Return an evenly spaced array of colors from the custom roque colors"""

    path = pkg_resources.files("roque_cmap").joinpath("roque_colors_256.pkl")
    with open(path, "rb") as f:
        roque_colors = pickle.load(f)

    return tuple(roque_colors[0 :: ceil(256 / n_colors)])


def roque(n_colors=256):
    """Return a matplotlib colormap from the custom roque colors"""

    # ensure that matplotlib is installed
    try:
        from matplotlib.colors import LinearSegmentedColormap
    except ImportError:
        raise ImportError("matplotlib is required for this function")

    colors = roque_generator(n_colors)

    color_map = LinearSegmentedColormap.from_list("roque", colors)

    return color_map

def roque_chill_generator(n_colors=200):
    """Return an evenly spaced array of colors from the custom roque colors"""

    path = pkg_resources.files("roque_cmap").joinpath("roque_chill_200.pkl")
    with open(path, "rb") as f:
        roque_colors = pickle.load(f)

    return tuple(roque_colors[0 :: ceil(200 / n_colors)])

def roque_chill(n_colors=200):
    """Return a matplotlib colormap from the custom roque colors"""

    # ensure that matplotlib is installed
    try:
        from matplotlib.colors import LinearSegmentedColormap
    except ImportError:
        raise ImportError("matplotlib is required for this function")

    colors = roque_chill_generator(n_colors)

    color_map = LinearSegmentedColormap.from_list("roque_chill", colors)

    return color_map
