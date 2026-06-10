from ase import Atoms

# Create Si atoms in diamond structure
atoms = Atoms('Si', positions=[
    (0, 0, 0),
    (0.25, 0.25, 0.25),
    (0.25, 0.75, 0.75),
    (0.75, 0.25, 0.75),
    (0.75, 0.75, 0.25),
    (0.75, 0.25, 0.25),
    (0.25, 0.75, 0.25),
    (0.25, 0.25, 0.75),
], cell=(5.43, 5.43, 5.43), pbc=True)

# Create 3x3x3 supercell
supercell = atoms.repeat((3, 3, 3))

# Print the number of atoms and cell volume
print("Number of atoms:", len(supercell))
print("Cell volume:", supercell.get_volume(), "Å³")
