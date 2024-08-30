import numpy as np
import matplotlib.pyplot as plt

class OceanExperiment:
    def __init__(self, grid_size, subduction_zone_bounds):
        """
        grid_size: tuple of (rows, cols)
        subduction_zone_bounds: tuple of (x_start, x_end, y_start, y_end)
        """
        self.grid_size = grid_size
        self.subduction_zone_bounds = subduction_zone_bounds
        self.depth_map = np.zeros(grid_size)
        self.water_surface_map = np.zeros(grid_size)
        self.basis_function_maps = []

    def set_depth_map(self, depth_array):
        """ Установить карту глубины по заданному 2D массиву """
        assert depth_array.shape == self.grid_size, "Размер depth_array должен совпадать с размером сетки"
        self.depth_map = depth_array

    def generate_basis_function_maps(self, basis_function, x_translation, y_translation):
        """
        Создает набор карт поверхности воды с базисными функциями в зоне субдукции с заданными шагами.

        basis_function: 2D массив базисной функции меньшего размера, чем зона субдукции.
        x_translation: шаг перемещения базисной функции по оси X.
        y_translation: шаг перемещения базисной функции по оси Y.
        """
        x_start, x_end, y_start, y_end = self.subduction_zone_bounds
        sub_zone_shape = (x_end - x_start, y_end - y_start)

        assert basis_function.shape[0] <= sub_zone_shape[0], "Базисная функция слишком велика по X"
        assert basis_function.shape[1] <= sub_zone_shape[1], "Базисная функция слишком велика по Y"

        self.basis_function_maps.clear()

        for i in range(0, sub_zone_shape[0] - basis_function.shape[0] + 1, x_translation):
            for j in range(0, sub_zone_shape[1] - basis_function.shape[1] + 1, y_translation):
                water_surface = np.zeros(self.grid_size)
                x_pos = x_start + i
                y_pos = y_start + j
                water_surface[x_pos:x_pos + basis_function.shape[0],
                y_pos:y_pos + basis_function.shape[1]] = basis_function
                self.basis_function_maps.append(water_surface)

    def set_water_surface_map(self, water_surface_array):
        """ Установить карту поверхности воды в зоне субдукции по заданному массиву """
        x_start, x_end, y_start, y_end = self.subduction_zone_bounds
        self.water_surface_map[x_start:x_end, y_start:y_end] = water_surface_array

    def display_basis_function(self, basis_function):
        """ Отобразить базисную функцию отдельно """
        plt.imshow(basis_function, cmap='viridis')
        plt.colorbar()
        plt.title('Basis Function')
        plt.show()

    def display_water_surface_with_basis_functions(self):
        """ Отобразить поверхность воды со всеми базисными функциями """
        combined_surface = np.zeros(self.grid_size)
        for basis_map in self.basis_function_maps:
            combined_surface += basis_map

        plt.imshow(combined_surface, cmap='viridis')
        plt.colorbar()
        plt.title('Water Surface with Basis Functions')
        plt.show()

    def display_water_surface(self):
        """ Отобразить текущую поверхность воды """
        plt.imshow(self.water_surface_map, cmap='viridis')
        plt.colorbar()
        plt.title('Water Surface')
        plt.show()

# Пример использования
grid_size = (100, 100)
subduction_zone_bounds = (30, 70, 30, 70)  # Определяем зону субдукции

experiment = OceanExperiment(grid_size, subduction_zone_bounds)

# Задать карту глубины
depth_map = np.random.rand(*grid_size)  # случайная карта глубины для примера
experiment.set_depth_map(depth_map)

# Задать базисную функцию
basis_function = np.array([[1, 1, 1], [1, 2, 1], [1, 1, 1]])  # Пример базисной функции
experiment.generate_basis_function_maps(basis_function,1,1)

# Отобразить единичную базисную функцию
experiment.display_basis_function(basis_function)

# Отобразить поверхность воды с наложенными базисными функциями
experiment.display_water_surface_with_basis_functions()

# Задать поверхность воды в зоне субдукции
water_surface = np.random.rand(40, 40)  # случайная поверхность воды в зоне субдукции
experiment.set_water_surface_map(water_surface)

# Отобразить текущую поверхность воды
experiment.display_water_surface()
