from ase.build import cluster

atoms = cluster("icos", size=3, lattice_constant=4.0, symbols='Au')
print(len(atoms))
print(atoms.get_center_of_mass())
