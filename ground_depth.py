import numpy as np


def generate_sloped_bottom(grid_size, min_depth, max_depth):
    """
    Генерирует 2D массив, симулирующий наклонное дно по оси X от min_depth до max_depth.

    grid_size: tuple (rows, cols) - размер массива
    min_depth: минимальная глубина (значение в начале по оси X)
    max_depth: максимальная глубина (значение в конце по оси X)

    Возвращает: 2D numpy массив размера grid_size
    """
    rows, cols = grid_size
    # Генерация линейного градиента по оси X
    x_gradient = np.linspace(min_depth, max_depth, cols)

    # Повторение градиента по оси Y
    sloped_bottom = np.tile(x_gradient, (rows, 1))

    return sloped_bottom
