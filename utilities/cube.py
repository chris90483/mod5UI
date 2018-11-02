import math
import pygame


# returns a 3d array of tuples with a pygame Rect and a "Draw as active" boolean
def get_cube(offset):
    surfaces = []
    left_offset = 0
    top_offset = 30
    box_radius = math.floor(2.5 * offset)

    for _z in range(0, 4):
        top = top_offset
        row_surfaces = []
        for _y in range(0, 4):
            val_surfaces = []
            left = left_offset
            for _x in range(0, 4):
                #                    PYGAME RECT                                     DRAW AS ACTIVE
                val_surfaces.append([pygame.Rect(left, top, box_radius, box_radius), False])
                left += box_radius + offset
            row_surfaces.append(val_surfaces)
            top += box_radius + offset
        surfaces.append(row_surfaces)
        top_offset += math.floor(0.5 * offset)
        left_offset += math.floor(0.5 * offset)
    return surfaces
