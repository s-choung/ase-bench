from ase import Atoms
from ase.build import bulk
from ase.cell import maxcell

si = bulk('Si', 'diamond', a=5.43)
supercell = si.repeat((2, 2, 2))
num_atoms = len(supercell)
cell_lengths = supercell.get_cell_lengths_and_angles()
cell_volume = cell_lengths[0] * cell_lengths[1] * cell_lengths[2]

print(f"Number of atoms: {num_atoms}")
print(f"Cell volume: {cell_volume:.4f} angstroms**3")
