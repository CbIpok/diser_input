from typing import Callable, List


def generate_2d_array(width: int, height: int, func: Callable[[int, int, int, int], float]) -> List[List[float]]:
    """
    Генерирует 2D массив типа float заданного размера на основе функции от координат.

    :param width: ширина массива (количество столбцов)
    :param height: высота массива (количество строк)
    :param func: функция, которая принимает координаты x, y и размеры области и возвращает значение типа float
    :return: 2D массив значений float
    """
    return [[func(x, y, width, height) for x in range(width)] for y in range(height)]


def save_2d_array_to_file(array: List[List[float]], file_path: str):
    """
    Сохраняет 2D массив в текстовый файл, где значения разделены пробелом, а строки - переносом строки.

    :param array: 2D массив значений float
    :param file_path: путь к файлу для сохранения
    """
    with open(file_path, 'w') as file:
        for row in array:
            file.write(' '.join(map(str, row)) + '\n')


# Пример функции для генерации значений на основе координат
def example_function(x: int, y: int, width: int, height: int) -> float:
    """
    Пример функции, которая генерирует значения на основе координат. Здесь используется простая функция,
    возвращающая нормализованное значение по координатам.

    :param x: координата x
    :param y: координата y
    :param width: ширина массива
    :param height: высота массива
    :return: значение float
    """
    return (x / width) * (y / height) + 1000


# Пример использования
width, height = 2581, 2581  # Задать размеры массива
array = generate_2d_array(width, height, example_function)

# Сохранить сгенерированный массив в файл
save_2d_array_to_file(array, 'ex.bath')
