# ====== JJ's Data entry, thanks JJ! ======

# CENTER FISH
class Centerfish:
  def __init__(self):
    # Horizontal stripe rainbow head
    self.stripe = 0
    # Pufferfish
    self.puf = 1
    # Black and white vertical stripes
    self.bw = 2
    # Purple with yellow spots
    self.pys = 3
    # White with orange stripes
    self.nemo = 4
    # Blue with white stripes
    self.quebec = 5

# EDGE FISH
class Edgefish:
  def __init__(self):
    # Yellow and purple, black around eyes
    self.goth = 6
    # Green with yellow stripes
    self.sevenup = 7
    # Black in the middle, white and brown stripes, facing left
    self.inkspot = 8
    # Twin red fish
    self.twin = 9
    # Yellow-black face, red-white body
    self.waspface = 10

c = Centerfish()
e = Edgefish()

# The fish themselves
# Fish are described as 5-tuples: (CENTER, LEFT, UP, RIGHT, BOTTOM)
# Indices:
CENTER = 0
LEFT = 1
TOP = 2
RIGHT = 3
BOTTOM = 4

# Fish:
tiles = [
(c.stripe, e.sevenup, e.inkspot, e.waspface, e.goth),     #0
(c.stripe, e.goth, e. inkspot, e.waspface, e.sevenup),
(c.stripe, e.twin, e.goth, e.sevenup, e.waspface),
(c.stripe, e.waspface, e.inkspot, e.sevenup, e.goth),
(c.stripe, e.twin, e.waspface, e.sevenup, e.goth),
(c.stripe, e.goth, e.sevenup, e.waspface, e.inkspot),   #5
(c.puf, e.inkspot, e.goth, e.twin, e.sevenup),
(c.puf, e.inkspot, e.goth, e.sevenup, e.waspface),
(c.puf, e.inkspot, e.sevenup, e.waspface, e.goth),
(c.puf, e.inkspot, e.goth, e.waspface, e.sevenup),
(c.puf, e.waspface, e.sevenup, e.goth, e.twin),     #10
(c.puf, e.inkspot, e.sevenup, e.twin, e.waspface),
(c.bw, e.twin, e.sevenup, e.goth, e.waspface),
(c.bw, e.twin, e.sevenup, e.waspface, e.inkspot),
(c.bw, e.goth, e.twin, e.inkspot, e.sevenup),
(c.bw, e.sevenup, e.inkspot, e.waspface, e.twin),   #15
(c.bw, e.waspface, e.goth, e.twin, e.sevenup),
(c.bw, e.sevenup, e.twin, e.goth, e.waspface),
(c.pys, e.waspface, e.goth, e.inkspot, e.sevenup),
(c.pys, e.waspface, e.sevenup, e.twin, e.inkspot),
(c.pys, e.sevenup, e.twin, e.inkspot, e.goth),      #20
(c.pys, e.sevenup, e.waspface, e.twin, e.inkspot),
(c.pys, e.goth, e.waspface, e.inkspot, e.sevenup),
(c.pys, e.waspface, e.goth, e.sevenup, e.twin),
(c.nemo, e.sevenup, e.waspface, e.inkspot, e.goth),
(c.nemo, e.goth, e.sevenup, e.twin, e.waspface),    #25
(c.nemo, e.inkspot, e.sevenup, e.twin, e.waspface),
(c.nemo, e.twin, e.goth, e.sevenup, e.inkspot),
(c.nemo, e.twin, e.goth, e.inkspot, e.sevenup),
(c.nemo, e.sevenup, e.inkspot, e.goth, e.twin),
(c.quebec, e.inkspot, e.sevenup, e.twin, e.goth),   #30
(c.quebec, e.sevenup, e.inkspot, e.twin, e.goth),
(c.quebec, e.twin, e.goth, e.waspface, e.sevenup),
(c.quebec, e.inkspot, e.waspface, e.sevenup, e.goth),
(c.quebec, e.twin, e.waspface, e.sevenup, e.inkspot),
(c.quebec, e.twin, e.sevenup, e.goth, e.inkspot)    #35
]
