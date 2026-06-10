from ase import Atoms
from ase.calculators.emt import EMT

# Create CO2 molecule
# C at (0,0,0), O at (-1.16, 0, 0) and (1.16, 0, 0)
positions = [[0, 0, 0], [-1.16, 0, 0], [1.16, 0, 0]]
symbols = ['C', 'O', 'O']
cell = [10, 10, 10]

mol = Atoms(symbols=symbols, positions=positions, cell=cell, pbc=False)

# Assign a calculator (EMT is for metals, but required to satisfy "calculate" context)
# Note: EMT won't provide accurate CO2 energies, but allows object initialization
mol.calc = EMT()

# Calculate and print interatomic distances
distances = mol.get_distances()
print("Interatomic distance matrix (Angstroms):")
print(distances)
