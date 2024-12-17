from typing import Dict
from colors import COLOR_MAPPING_, COLOR_MAPPING_CATEGORY_


def hex_to_rgba(hex_value):
    hex_value = hex_value.lstrip('#')
    red = int(hex_value[0:2], 16)
    green = int(hex_value[2:4], 16)
    blue = int(hex_value[4:6], 16)
    return f"rgba({red}, {green}, {blue}, 1.0)"


def update_colors_to_rgba(color_map):
    rgba_map = { }
    for hex_code, value in color_map.items():
        rgba_map[hex_to_rgba(hex_code)] = value
    return rgba_map


def update_nested_colors_to_rgba(nested_map):
    updated_nested_map = { }
    for category, color_map in nested_map.items():
        updated_nested_map[category] = update_colors_to_rgba(color_map)
    return updated_nested_map


COLOR_MAPPING = update_colors_to_rgba(COLOR_MAPPING_)
COLOR_MAPPING_CATEGORY = update_nested_colors_to_rgba(COLOR_MAPPING_CATEGORY_)
