from ase.build import surface
from ase.calculators import EMT, LJ
from ase.io import write

# Create a Cu bulk
bulk = surface('Cu', (2, 1, 1), size=(4, 4, 4), symmetry='p')

# Add vacuum
bulk.vacuum(10.0)

# Set calculator
bulk.calc = EMT()
bulk.calc.kpoints.set((1, 1, 1))

# Calculate LJ forces
bulk.calc = LJ()

# Write the structure to a file
write('Cu_surface.xyz', bulk)

# Print number of atoms and cell
print(f"Number of atoms: {len(bulk)}")
print(f"Cell: {bulk.cell}")
