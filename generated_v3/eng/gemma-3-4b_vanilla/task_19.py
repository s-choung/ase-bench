from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import fcc111
from ase.geometry import get_distances

c = Atoms([(0, 0, 0)], site=0, basis=0)
o = Atoms(positions=[(1.16, 0, 0), (-1.16, 0, 0), (0, 1.16, 0), (0, -1.16, 0), (0, 0, 1.16), (0, 0, -1.16)])
co2 = c + o
co2.cell = (10, 10, 10)
co2.pbc = False

calc = EMT()
co2.calc = calc
co2.get_distances()

distances = get_distances(co2)
print(distances)
