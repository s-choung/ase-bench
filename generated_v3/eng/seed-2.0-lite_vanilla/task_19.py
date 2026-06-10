from ase import Atoms

# Initialize CO2 molecule with specified coordinates
atoms = Atoms('CO2', positions=[[0.0, 0.0, 0.0], [-1.16, 0.0, 0.0], [1.16, 0.0, 0.0]])
atoms.set_cell([10, 10, 10])
atoms.set_pbc([False, False, False])

# Calculate and output all pairwise interatomic distances
interatomic_dists = atoms.get_distances()
print("Pairwise interatomic distances (Å):\n", interatomic_dists)
