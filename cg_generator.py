import random

from builder import create_building
from cleanup import clear_generated
from config import (
    BUILDINGS_PER_SIDE,
    CELL_SIZE,
    ROAD_WIDTH,
    MIN_BUILDING_HEIGHT,
    MAX_BUILDING_HEIGHT,
    ALLOWED_ROTATIONS
)

from asset_loader import load_templates


def build_random_building(template_pool):
    template = random.choice(template_pool)
    height = random.uniform(MIN_BUILDING_HEIGHT, MAX_BUILDING_HEIGHT)
    rotation = random.choice(ALLOWED_ROTATIONS)
    return template, height, rotation


def generate_city(templates):
    clear_generated()

    if not templates:
        print("Error: No available base templates found. Cannot generate city.")
        return

    offset_y = ROAD_WIDTH / 2
    sides = [-offset_y, offset_y]

    start_x = -((BUILDINGS_PER_SIDE - 1) * CELL_SIZE) / 2

    for i in range(BUILDINGS_PER_SIDE):
        x = start_x + i * CELL_SIZE

        for side in sides:
            template, height, rotation = build_random_building(templates)

            create_building(
                template,
                (x, side, 0),
                height,
                rotation
            )

            print(f"Selected base template: {template.name}")