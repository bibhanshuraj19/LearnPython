import matplotlib.pyplot as plt
import numpy as np

def draw_board(ax, defective, placed_tiles, size=8):
    """
    Draws a chessboard with a defective square and placed tiles.
    
    Parameters:
    - ax: The axes object to draw on.
    - defective: Tuple (x, y) of the defective square's position.
    - placed_tiles: List of L-shaped tiles, each defined as [(x1, y1), (x2, y2), (x3, y3)].
    - size: Size of the chessboard (default is 8x8).
    """
    # Draw the grid
    for x in range(size + 1):
        ax.plot([x, x], [0, size], color='black', linewidth=0.5)
        ax.plot([0, size], [x, x], color='black', linewidth=0.5)
    
    # Shade the defective square
    x, y = defective
    ax.add_patch(plt.Rectangle((x, y), 1, 1, color='black'))
    
    # Shade L-shaped tiles
    for tile in placed_tiles:
        for tx, ty in tile:
            ax.add_patch(plt.Rectangle((tx, ty), 1, 1, color='gray', alpha=0.7))
    
    # Set limits and aspect ratio
    ax.set_xlim(0, size)
    ax.set_ylim(0, size)
    ax.set_aspect('equal')
    ax.axis('off')

def divide_and_conquer(ax, x, y, size, defective, tiles):
    """
    Recursively applies the divide-and-conquer algorithm to tile the board.
    
    Parameters:
    - ax: The axes object to draw on.
    - x, y: Top-left corner of the current board.
    - size: Size of the current board.
    - defective: Position of the defective square within the current board.
    - tiles: List to store the placed tiles.
    """
    if size == 2:
        # Base case: 2x2 board
        l_tile = []
        for dx in range(2):
            for dy in range(2):
                if (x + dx, y + dy) != defective:
                    l_tile.append((x + dx, y + dy))
        tiles.append(l_tile)
        return
    
    # Find the center of the board
    half = size // 2
    cx, cy = x + half, y + half
    
    # Determine which quadrant contains the defective square
    quad = (defective[0] >= cx, defective[1] >= cy)
    
    # Place an L-shaped tile in the center of the board
    center_tile = []
    for dx, dy in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        if (dx, dy) != quad:
            center_tile.append((cx - 1 + dx, cy - 1 + dy))
    tiles.append(center_tile)
    
    # Recurse on each quadrant
    quads = [
        (x, y), (x, cy), (cx, y), (cx, cy)
    ]
    for i, (qx, qy) in enumerate(quads):
        new_defective = defective if i == quad[0] * 2 + quad[1] else (cx - 1 + (i // 2), cy - 1 + (i % 2))
        divide_and_conquer(ax, qx, qy, half, new_defective, tiles)

# Initialize plot
fig, ax = plt.subplots(figsize=(6, 6))

# Defective square and board size
defective_square = (3, 3)
board_size = 8

# List to store tiles
tiles = []

# Apply divide-and-conquer algorithm
divide_and_conquer(ax, 0, 0, board_size, defective_square, tiles)

# Draw the final board with tiles
draw_board(ax, defective_square, tiles, size=board_size)
plt.show()
