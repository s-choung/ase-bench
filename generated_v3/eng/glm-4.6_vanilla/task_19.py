from ase import Atoms

# Create CO2 molecule: C at origin, O atoms at +/- 1.16 Angstrom on x-axis
atoms = Atoms(symbols=['C', 'O', 'O'],
              positions=[[0.0, 0.0, 0.0], [-1.16, 0.0, 0.0], [1.16, 0.0, 0.0]],
              cell=[10, 10, 10],
              pbc=False)

# Calculate distances
d_co = atoms.get_distances(0, 1)[0]
d_oo = atoms.get_distances(1, 2)[0]

print(f"C-O distance: {d_co:.3f} Angstrom")
print(f"O-O distance: {d_oo:.3f} Angstrom")
