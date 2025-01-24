from math import cos, radians


async def calculate_rectangle_bounds(
        center_lat: float, # Широта
        center_lon: float, # Долгота
        width_km: float,
        height_km: float) -> tuple:
    width_degree_km = 1 / 111
    longitude_degree_km = 1 / (111 * cos(radians(center_lat)))

    width_offset = (height_km * width_degree_km) / 2
    longitude_offset = (width_km * longitude_degree_km) / 2

    min_lat = center_lat - width_offset
    max_lat = center_lat + width_offset
    min_lon = center_lon - longitude_offset
    max_lon = center_lon + longitude_offset

    return min_lon, min_lat, max_lon, max_lat
