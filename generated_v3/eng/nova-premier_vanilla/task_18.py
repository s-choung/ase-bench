from ase import Atoms
from ase.data import g2
from ase.calculators.emt import EMT
from ase.geometry import get_distances

mol = g2.molecule('CH4')
mol.calc = EMT()
dyn = mol.get_potential_energy()
coords = mol.get_positions()
print("Coordinates:\n", coords)
dists = get_distances(coords, cell=mol.cell, pbc=mol.pbc)
print("Bond lengths:", dists[0, 1:])
print("Formula:", mol.get_chemical_formula())
