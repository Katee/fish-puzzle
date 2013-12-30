from data import *

def can_be_placed_to_right(partial_row, new_tile):
  if not tiles[partial_row[-1]][RIGHT] == tiles[new_tile][LEFT]:
    return False
  for tile_index in partial_row:
    if tiles[tile_index][CENTER] == tiles[new_tile][CENTER]:
      return False
  return True

def make_initial_rows(tiles):
  # first tile in the row can be any tile
  rows = [[i] for i in range(36)]

  for i in range(5):
    new_rows = []
    for row in rows:
      # tiles that match on the right and the centers are not the same
      matches = [row + [i] for i in range(len(tiles)) if can_be_placed_to_right(row, i)]
      map(lambda x: new_rows.append(x), matches)
    rows = new_rows
  return rows

def column_center_match(rows, new_tile, position):
  for row in rows:
    if tiles[new_tile][CENTER] == tiles[row[position]][CENTER]:
      return True
  return False

def find_continuing_rows(partial):
  # the tiles that haven't yet been used in this previous partial solution
  unused_tiles = [i for i in range(len(tiles)) if i not in set(reduce(lambda a, b: a + b, partial, []))]

  # make buckets for each position in the new row that contain unused tiles that
  # do not have the same center fish as any other tile above it and that can legally go below it
  buckets = {i: [] for i in range(6)}
  for tile_index in unused_tiles:
    for i in range(6):
      if tiles[partial[-1][i]][BOTTOM] == tiles[tile_index][TOP]:
        centers = column_center_match(partial, tile_index, i)
        if not centers:
          buckets[i].append(tile_index)

  # take the first bucket as the beginning of the new rows
  rows = [[f] for f in buckets[0]]

  for i in range(1, 6):
    new_rows = []
    for row in rows:
      # tile that match on the right
      matches = [row + [f] for f in buckets[i] if tiles[row[-1]][RIGHT] == tiles[f][LEFT] and f not in row]
      map(lambda x: new_rows.append(x), matches)
    rows = new_rows
  return rows

# check there are no repeats on the diagonals
def check_sudoku(solution):
  tl_br = set()
  tr_bl = set()
  for i in range(6):
    tl_br.add(tiles[solution[i][i]][CENTER])
    tr_bl.add(tiles[solution[i][5 - i]][CENTER])
  return len(tl_br) == 6 and len(tr_bl) == 6

def find_solution(partial):
  if len(partial) == 6 and check_sudoku(partial):
    print partial
    quit()

  for row in find_continuing_rows(partial):
    find_solution(partial + [row])

for row in make_initial_rows(tiles):
  find_solution([row])
