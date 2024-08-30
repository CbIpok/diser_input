import numpy as np
import matplotlib.pyplot as plt

class OceanSimulation:
    def __init__(self, width, height, subduction_zone_coords, subduction_zone_size):
        """
        Инициализация симуляции.
        :param width: ширина области
        :param height: высота области
        :param subduction_zone_coords: координаты верхнего левого угла зоны субдукции (x, y)
        :param subduction_zone_size: размер зоны субдукции (ширина, высота)
        """
        self.width = width
        self.height = height
        self.subduction_zone_coords = subduction_zone_coords
        self.subduction_zone_size = subduction_zone_size
        self.ocean_depth = np.zeros((height, width))
        self.water_surface = np.zeros((height, width))

    def set_ocean_depth(self, depth_map):
        """
        Устанавливает карту глубины океана.
        :param depth_map: 2D массив с глубинами
        """
        if depth_map.shape != (self.height, self.width):
            raise ValueError("Размер depth_map должен совпадать с размером области.")
        self.ocean_depth = depth_map

    def generate_basis_function(self, basis_function, x_offset=0, y_offset=0):
        """
        Генерирует и возвращает базисную функцию в зоне субдукции.
        :param basis_function: базисная функция как 2D массив меньшего размера
        :param x_offset: смещение по x в зоне субдукции
        :param y_offset: смещение по y в зоне субдукции
        :return: 2D массив с наложенной базисной функцией
        """
        basis_height, basis_width = basis_function.shape
        subduction_x, subduction_y = self.subduction_zone_coords
        subduction_width, subduction_height = self.subduction_zone_size

        if (basis_width + x_offset > subduction_width) or (basis_height + y_offset > subduction_height):
            raise ValueError("Базисная функция выходит за пределы зоны субдукции при заданных смещениях.")

        water_surface_with_basis = np.zeros((self.height, self.width))

        water_surface_with_basis[
            subduction_y + y_offset : subduction_y + y_offset + basis_height,
            subduction_x + x_offset : subduction_x + x_offset + basis_width
        ] = basis_function

        return water_surface_with_basis

    def apply_basis_functions(self, basis_functions):
        """
        Накладывает коллекцию базисных функций на поверхность воды в зоне субдукции.
        :param basis_functions: коллекция базисных функций (список кортежей вида (базисная функция, x_offset, y_offset))
        :return: 2D массив с наложенными базисными функциями
        """
        for basis_function, x_offset, y_offset in basis_functions:
            self.water_surface += self.generate_basis_function(basis_function, x_offset, y_offset)

    def set_custom_water_surface(self, custom_surface):
        """
        Устанавливает заданный массив в зоне субдукции.
        :param custom_surface: 2D массив с высотой поверхности воды в зоне субдукции
        """
        subduction_x, subduction_y = self.subduction_zone_coords
        subduction_width, subduction_height = self.subduction_zone_size

        if custom_surface.shape != (subduction_height, subduction_width):
            raise ValueError("Размер custom_surface должен совпадать с размером зоны субдукции.")

        self.water_surface[subduction_y:subduction_y + subduction_height, subduction_x:subduction_x + subduction_width] = custom_surface

    def plot_ocean_depth(self):
        """
        Отображает карту глубины океана.
        """
        plt.imshow(self.ocean_depth, cmap='viridis')
        plt.colorbar(label='Глубина')
        plt.title('Карта глубины океана')
        plt.show()

    def plot_water_surface(self):
        """
        Отображает карту поверхности воды.
        """
        plt.imshow(self.water_surface, cmap='Blues')
        plt.colorbar(label='Высота поверхности воды')
        plt.title('Поверхность воды')
        plt.show()

    def plot_basis_function(self, basis_function):
        """
        Отображает базисную функцию.
        :param basis_function: базисная функция как 2D массив
        """
        plt.imshow(basis_function, cmap='coolwarm')
        plt.colorbar(label='Базисная функция')
        plt.title('Базисная функция')
        plt.show()



if __name__ == "__main__":
    # Размеры области и зоны субдукции
    width, height = 100, 100
    subduction_zone_coords = (30, 30)
    subduction_zone_size = (20, 20)

    # Инициализация симуляции
    simulation = OceanSimulation(width, height, subduction_zone_coords, subduction_zone_size)

    # Установка карты глубины океана
    depth_map = np.random.uniform(-5000, 0, (height, width))
    simulation.set_ocean_depth(depth_map)
    simulation.plot_ocean_depth()

    # Генерация базисной функции
    basis_function = np.array([
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ])
    simulation.plot_basis_function(basis_function)

    # Наложение базисных функций на поверхность воды
    basis_functions = [(basis_function, x, y) for x in range(0, 18, 6) for y in range(0, 18, 6)]
    simulation.apply_basis_functions(basis_functions)
    simulation.plot_water_surface()

    # Задание произвольной поверхности воды в зоне субдукции
    custom_surface = np.random.uniform(1, 5, subduction_zone_size)
    simulation.set_custom_water_surface(custom_surface)
    simulation.plot_water_surface()
