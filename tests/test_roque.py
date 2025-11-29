import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

from roque_cmap import roque, roque_generator, roque_chill, roque_chill_generator


def test_roque():
    colors = roque_generator()
    assert len(colors) == 256


def test_roque_128():
    colors = roque_generator(128)
    assert len(colors) == 128


def test_matplotlib_cmap():
    assert isinstance(roque(), LinearSegmentedColormap)

    fig, ax = plt.subplots()
    ax.imshow([[0, 1], [0, 1]], cmap=roque())
    plt.close(fig)


def test_seaborn_pallete():
    glue = sns.load_dataset("glue").pivot(index="Model", columns="Task", values="Score")
    # Your test code here
    sns.heatmap(glue, cmap=roque())


def test_roque_chill_generator():
    colors = roque_chill_generator()
    # The pickle file has 201 colors, with step=ceil(200/200)=1, we get all 201 colors
    assert len(colors) == 201


def test_roque_chill_generator_custom():
    colors = roque_chill_generator(100)
    # With step=ceil(200/100)=2, we get 101 colors (indices 0, 2, 4, ..., 200)
    assert len(colors) == 101


def test_roque_chill():
    assert isinstance(roque_chill(), LinearSegmentedColormap)

    fig, ax = plt.subplots()
    ax.imshow([[0, 1], [0, 1]], cmap=roque_chill())
    plt.close(fig)


def test_roque_chill_custom():
    assert isinstance(roque_chill(100), LinearSegmentedColormap)


def test_roque_import_error():
    """Test that roque() raises ImportError when matplotlib is not available"""
    import sys
    import importlib
    
    # Save original module
    original_roque = sys.modules.get('roque_cmap.roque')
    
    # Reload the roque module
    if 'roque_cmap.roque' in sys.modules:
        del sys.modules['roque_cmap.roque']
    
    # Patch the import to raise ImportError for matplotlib.colors
    original_import = __builtins__['__import__']
    
    def mock_import(name, globals=None, locals=None, fromlist=(), level=0):
        if name == 'matplotlib.colors' or (fromlist and 'LinearSegmentedColormap' in fromlist and name == 'matplotlib.colors'):
            raise ImportError("No module named 'matplotlib'")
        return original_import(name, globals, locals, fromlist, level)
    
    __builtins__['__import__'] = mock_import
    
    try:
        from roque_cmap.roque import roque as roque_func
        try:
            roque_func()
            assert False, "Expected ImportError"
        except ImportError as e:
            assert "matplotlib is required" in str(e)
    finally:
        # Restore original import and module
        __builtins__['__import__'] = original_import
        if 'roque_cmap.roque' in sys.modules:
            del sys.modules['roque_cmap.roque']
        if original_roque:
            sys.modules['roque_cmap.roque'] = original_roque


def test_roque_chill_import_error():
    """Test that roque_chill() raises ImportError when matplotlib is not available"""
    import sys
    
    # Save original module
    original_roque = sys.modules.get('roque_cmap.roque')
    
    # Reload the roque module
    if 'roque_cmap.roque' in sys.modules:
        del sys.modules['roque_cmap.roque']
    
    # Patch the import to raise ImportError for matplotlib.colors
    original_import = __builtins__['__import__']
    
    def mock_import(name, globals=None, locals=None, fromlist=(), level=0):
        if name == 'matplotlib.colors' or (fromlist and 'LinearSegmentedColormap' in fromlist and name == 'matplotlib.colors'):
            raise ImportError("No module named 'matplotlib'")
        return original_import(name, globals, locals, fromlist, level)
    
    __builtins__['__import__'] = mock_import
    
    try:
        from roque_cmap.roque import roque_chill as roque_chill_func
        try:
            roque_chill_func()
            assert False, "Expected ImportError"
        except ImportError as e:
            assert "matplotlib is required" in str(e)
    finally:
        # Restore original import and module
        __builtins__['__import__'] = original_import
        if 'roque_cmap.roque' in sys.modules:
            del sys.modules['roque_cmap.roque']
        if original_roque:
            sys.modules['roque_cmap.roque'] = original_roque
