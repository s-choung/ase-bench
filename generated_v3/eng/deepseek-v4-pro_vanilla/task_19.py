from ase import Atoms

# CO2 molecule: C at origin, O at ±1.16 Å along x-axis
co2 = Atoms('CO2', positions=[(0, 0, 0), (-1.16, 0, 0), (1.16, 0, 0)])
co2.set_cell([10, 10, 10])
co2.set_pbc(False)

# Print all interatomic distances (3x3 matrix)
print(co2.get_distances())
