import time

import numpy as np
import matplotlib.pyplot as plt
from fontTools.merge import timer


class OceanExperimentGeometry:
    def __init__(self, grid_size, subduction_zone_bounds):
        """
        grid_size: tuple of (rows, cols)
        subduction_zone_bounds: tuple of (x_start, x_end, y_start, y_end)
        """
        self.grid_size = grid_size
        self.subduction_zone_bounds = subduction_zone_bounds


class OceanExperimentBasis(OceanExperimentGeometry):
    def __init__(self, geometry):
        super().__init__(geometry.grid_size, geometry.subduction_zone_bounds)
        self.basis_function_maps = []

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
        count = 0
        for i in range(0, sub_zone_shape[0] - basis_function.shape[0] + 1, x_translation):
            for j in range(0, sub_zone_shape[1] - basis_function.shape[1] + 1, y_translation):
                count += 1
        self.basis_function_maps = np.memmap('basis_function_maps', dtype=np.float32, mode='w+', shape=(count,*self.grid_size))
        count = 0
        for i in range(0, sub_zone_shape[0] - basis_function.shape[0] + 1, x_translation):
            for j in range(0, sub_zone_shape[1] - basis_function.shape[1] + 1, y_translation):
                # water_surface = np.zeros(self.grid_size, dtype=np.float32)
                x_pos = x_start + i
                y_pos = y_start + j
                self.basis_function_maps[count][x_pos:x_pos + basis_function.shape[0],
                y_pos:y_pos + basis_function.shape[1]] = basis_function
                # self.basis_function_maps.append(water_surface)

        self.basis_function = basis_function

    def display_basis_function(self):
        """ Отобразить базисную функцию отдельно """
        plt.imshow(self.basis_function, cmap='viridis')
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


class OceanExperimentSurface(OceanExperimentGeometry):
    def __init__(self, geometry):
        super().__init__(geometry.grid_size, geometry.subduction_zone_bounds)
        self.water_surface_map = np.zeros(self.grid_size)

    def set_water_surface_map(self, water_surface_array):
        """ Установить карту поверхности воды в зоне субдукции по заданному массиву """
        x_start, x_end, y_start, y_end = self.subduction_zone_bounds
        self.water_surface_map[x_start:x_end, y_start:y_end] = water_surface_array

    def display_water_surface(self):
        """ Отобразить текущую поверхность воды """
        plt.imshow(self.water_surface_map, cmap='viridis')
        plt.colorbar()
        plt.title('Water Surface')
        plt.show()

class OceanExperimentDepthMap(OceanExperimentGeometry):
    def __init__(self, geometry):
        super().__init__(geometry.grid_size, geometry.subduction_zone_bounds)
        self.depth_map = np.zeros(self.grid_size)

    def set_depth_map(self, depth_array):
        """ Установить карту глубины по заданному 2D массиву """
        assert depth_array.shape == self.grid_size, "Размер depth_array должен совпадать с размером сетки"
        self.depth_map = depth_array

if __name__ == "__main__":
    # Пример использования
    grid_size = (100, 100)
    subduction_zone_bounds = (30, 70, 30, 70)  # Определяем зону субдукции

    experiment_geometry = OceanExperimentGeometry(grid_size, subduction_zone_bounds)

    # Задать карту глубины
    depth_map = np.random.rand(*grid_size)  # случайная карта глубины для примера
    experiment_depth_map = OceanExperimentDepthMap(experiment_geometry)
    experiment_depth_map.set_depth_map(depth_map)

    # Задать базисную функцию
    basis_function = np.array([[1, 1, 1], [1, 2, 1], [1, 1, 1]])  # Пример базисной функции
    experiment_basis = OceanExperimentBasis(experiment_geometry)
    experiment_basis.generate_basis_function_maps(basis_function, 1, 1)

    # Отобразить поверхность воды с наложенными базисными функциями
    experiment_basis.display_water_surface_with_basis_functions()

    # Отобразить единичную базисную функцию
    experiment_basis.display_basis_function()

    experiment_surface = OceanExperimentSurface(experiment_geometry)

    # Задать поверхность воды в зоне субдукции
    water_surface = np.random.rand(40, 40)  # случайная поверхность воды в зоне субдукции
    experiment_surface.set_water_surface_map(water_surface)

    # Отобразить текущую поверхность воды
    experiment_surface.display_water_surface()
