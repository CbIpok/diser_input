import numpy as np
from scipy.ndimage import zoom


def generate_array_with_central_square(width):
    """
        Генерирует 2D массив заданной ширины, с центральным квадратом и соблюдением пропорций.

        width: ширина массива (должна быть делима на 8 для соблюдения пропорций)

        Возвращает:
        - Массив 2D numpy
        - Размеры центрального квадрата по x и y (высота и ширина)
        """
    # Проверка, чтобы ширина была кратна 8 для соблюдения пропорций
    if width % 8 != 0:
        closest_width = (width // 8) * 8
        print(f"Warning: The width {width} is not suitable for preserving the proportions. "
              f"The closest valid width is {closest_width}. Using it instead.")
        width = closest_width

    # Размеры массива
    height = width  # массив будет квадратным
    central_square_size = width // 4  # размер центрального квадрата

    # Инициализация массива
    array = np.ones((height, width), dtype=int)

    # Определяем границы центрального квадрата
    x_start = (width // 2) - (central_square_size // 2)
    x_end = x_start + central_square_size
    y_start = (height // 2) - (central_square_size // 2)
    y_end = y_start + central_square_size

    # Заполнение центрального квадрата
    array[y_start:y_end, x_start:x_end] = 2

    return array, central_square_size, central_square_size


class ArrayScaler:
    def __init__(self, initial_array):
        self.array = initial_array

    def get_scaled_array(self, new_size):
        """
        Масштабирует 2D массив до нового размера.

        new_size: tuple (new_rows, new_cols)

        Возвращает: новый 2D массив размера new_size
        """
        # Определяем коэффициенты масштабирования
        zoom_factors = (new_size[0] / self.array.shape[0], new_size[1] / self.array.shape[1])

        # Применяем масштабирование
        scaled_array = zoom(self.array, zoom_factors, order=1)  

        return scaled_array


# Пример использования
initial_array = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
)  # Пример 2D массива


if __name__ == "__main__":
    scaler = ArrayScaler(initial_array)

    new_size = (24, 24)  # Новый размер массива
    scaled_array = scaler.get_scaled_array(new_size)

    print("Исходный массив:")
    print(initial_array)

    print("\nМасштабированный массив:")
    array_str = repr(scaled_array.tolist())
    formatted_array_str = array_str.replace('], [', '],\n [')
    print(formatted_array_str)