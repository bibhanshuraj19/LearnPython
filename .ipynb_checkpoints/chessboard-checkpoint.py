import matplotlib.pyplot as plt
import numpy as np

def draw_board(ax, defective, placed_tiles, size=8):
   
    for x in range(size + 1):
        ax.plot([x, x], [0, size], color='black', linewidth=0.5)
        ax.plot([0, size], [x, x], color='black', linewidth=0.5)
    
    # Shade the defective square
    x, y = defective
    ax.add_patch(plt.Rectangle((x, y), 1, 1, color='black'))
    
    for tile in placed_tiles:
        for tx, ty in tile:
            ax.add_patch(plt.Rectangle((tx, ty), 1, 1, color='gray', alpha=0.7))
    
    ax.set_xlim(0, size)
    ax.set_ylim(0, size)
    ax.set_aspect('equal')
    ax.axis('off')

def divide_and_conquer(ax, x, y, size, defective, tiles):
    
    if size == 2:
        l_tile = []
        for dx in range(2):
            for dy in range(2):
                if (x + dx, y + dy) != defective:
                    l_tile.append((x + dx, y + dy))
        tiles.append(l_tile)
        return
    
    half = size // 2
    cx, cy = x + half, y + half
    
    quad = (defective[0] >= cx, defective[1] >= cy)
    
    center_tile = []
    for dx, dy in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        if (dx, dy) != quad:
            center_tile.append((cx - 1 + dx, cy - 1 + dy))
    tiles.append(center_tile)
    
    quads = [
        (x, y), (x, cy), (cx, y), (cx, cy)
    ]
    for i, (qx, qy) in enumerate(quads):
        new_defective = defective if i == quad[0] * 2 + quad[1] else (cx - 1 + (i // 2), cy - 1 + (i % 2))
        divide_and_conquer(ax, qx, qy, half, new_defective, tiles)

fig, ax = plt.subplots(figsize=(6, 6))

defective_square = (3, 3)
board_size = 8

tiles = []

divide_and_conquer(ax, 0, 0, board_size, defective_square, tiles)

draw_board(ax, defective_square, tiles, size=board_size)
plt.show()
