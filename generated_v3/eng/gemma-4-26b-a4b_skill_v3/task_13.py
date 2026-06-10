from ase.build import bulk

# Create Si bulk with diamond structure
# diamond lattice constant is provided; cubic=True ensures the cell is defined by a=b=c
atoms = bulk('Si', 'diamond', a=5.43, cubic=True)

# Create a 3x3x3 supercell
atoms = atoms.repeat((3, 3, 3))

# Print required information
print(f"Number of atoms: {len(atoms)}")
print(f"Cell volume: {atoms.get_volume():.3f} Å^3")
