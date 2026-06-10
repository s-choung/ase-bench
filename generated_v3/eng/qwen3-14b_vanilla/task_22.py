from ase.build import fcc111, molecule

slab = fcc111('Al', size=(3, 3, 3), vacuum=10)
positions = slab.get_positions()
z_coords = positions[:, 2]
max_z = max(z_coords)
surface_indices = [i for i in range(len(z_coords)) if z_coords[i] == max_z]
pos1, pos2 = positions[surface_indices[:2]]
bridge = [(pos1[0] + pos2[0]) / 2, (pos1[1] + pos2[1]) / 2, max_z + 2.0]

n2 = molecule('N2')
n2.translate([bridge[0] - n2.get_positions()[0][0], 
              bridge[1] - n2.get_positions()[0][1], 
              bridge[2] - n2.get_positions()[0][2]])

final = slab + n2
print("Number of atoms:", len(final))
print("Atom types:", final.get_chemical_symbols())
