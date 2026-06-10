from ase import Atoms
from ase.geometry import get_distances

positions = [[0, 0, -1.16], [0, 0, 0], [0, 0, 1.16]]  # O, C, O
symbols = ['O', 'C', 'O']
cell = [10, 10, 10]

co2 = Atoms(symbols=symbols, positions=positions, cell=cell, pbc=False)

dmat = get_distances(co2.get_positions(), co2.get_positions(), cell=co2.get_cell(), pbc=co2.get_pbc())[1]
print(dmat)
