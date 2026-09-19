# Width of a total wall and a tile
TOTAL_WIDTH = 100
TILE_WIDTH = 5

# Compute the number of tiles and gap size
numberOfPairs = (TOTAL_WIDTH - TILE_WIDTH) // (2 * TILE_WIDTH)    # a pair of tiles: white and black
numberOfTiles = 1 + 2 * numberOfPairs    # 1 is black tile at the end
gap = (TOTAL_WIDTH - numberOfTiles * TILE_WIDTH) / 2.0


# Print the output
print("Number of tiles:", numberOfTiles)
print("Gap at each end:", gap)