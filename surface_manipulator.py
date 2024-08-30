import matplotlib.pyplot as plt
import ground_depth
import global_cords

class ArrayManipulator:
    def __init__(self, array):
        """
        Инициализация класса с начальным 2D массивом.

        array: 2D numpy массив
        """
        self.array = array

    def place_rectangle(self, top_left, width, height, value=1):
        """
        Размещает прямоугольную область на 2D массиве.

        top_left: tuple (row, col) - координаты верхнего левого угла прямоугольника
        width: ширина прямоугольника
        height: высота прямоугольника
        value: значение, которым будет заполнена прямоугольная область
        """
        row_start, col_start = top_left
        row_end = min(row_start + height, self.array.shape[0])
        col_end = min(col_start + width, self.array.shape[1])

        self.array[row_start:row_end, col_start:col_end] = value

    def display_array(self):
        """
        Отображает 2D массив с использованием matplotlib.
        """
        plt.imshow(self.array, cmap='viridis', interpolation='none')
        plt.colorbar()
        plt.show()


def visualize_subduction_zone():
    # Создаем 2D массив размером 10x10
    array = ground_depth.generate_sloped_bottom((global_cords.size_x, global_cords.size_y), 100, 2000)

    # Инициализируем объект класса
    manipulator = ArrayManipulator(array)

    # Размещаем прямоугольник размером 4x3 начиная с координаты (2, 3)
    manipulator.place_rectangle(global_cords.subduction_zone_top_left, width=global_cords.subduction_zone_widht,
                                height=global_cords.subduction_zone_height, value=5)

    # Отображаем массив
    manipulator.display_array()



if __name__ == "__main__":
    visualize_subduction_zone()

