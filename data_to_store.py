import numpy as np
import surface_gen
import global_cords
import ground_depth
import basis_function
import struct
def calculate_rectangle_bounds(top_left, width, height):
    """
    Вычисляет границы прямоугольной области.

    top_left: tuple (x_start, y_start) - координаты верхнего левого угла прямоугольника.
    width: ширина прямоугольника.
    height: высота прямоугольника.

    Возвращает:
    x_start, x_end, y_start, y_end - границы прямоугольной области.
    """
    x_start = top_left[0]
    y_start = top_left[1]
    x_end = x_start + width
    y_end = y_start + height

    return x_start, x_end, y_start, y_end
print(struct.calcsize("P") * 8)
experiment_geometry = surface_gen.OceanExperimentGeometry(global_cords.size, global_cords.subduction_zone_bounds)
depth_map = ground_depth.generate_sloped_bottom(global_cords.size,100,2000)  # случайная карта глубины для примера
experiment_depth_map = surface_gen.OceanExperimentDepthMap(experiment_geometry)
experiment_depth_map.set_depth_map(depth_map)

# Задать базисную функцию
basis_func, *(x_translation,y_translation) = basis_function.generate_array_with_central_square(48)  # Пример базисной функции
experiment_basis =  surface_gen.OceanExperimentBasis(experiment_geometry)
experiment_basis.generate_basis_function_maps(basis_func, x_translation,y_translation)

# Отобразить поверхность воды с наложенными базисными функциями
experiment_basis.display_water_surface_with_basis_functions()

# Отобразить единичную базисную функцию
experiment_basis.display_basis_function()

experiment_surface = surface_gen.OceanExperimentSurface(experiment_geometry)

# Задать поверхность воды в зоне субдукции
water_surface = np.random.rand(global_cords.subduction_zone_widht,global_cords.subduction_zone_height)  # случайная поверхность воды в зоне субдукции
experiment_surface.set_water_surface_map(water_surface)

# Отобразить текущую поверхность воды
experiment_surface.display_water_surface()

basises = []