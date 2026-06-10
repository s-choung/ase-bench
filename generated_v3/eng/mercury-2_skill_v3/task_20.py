from ase.build import nanotube

# (6,6) armchair carbon nanotube, 4 repeats of the primitive cell
tube = nanotube(6, 6, length=4, bond=1.42, symbol='C')

print('Number of atoms:', tube.get_number_of_atoms())

a, b, c, alpha, beta, gamma = tube.get_cell_lengths_and_angles()
print('Cell lengths (Å):', a, b, c)
print('Cell angles (deg):', alpha, beta, gamma)
