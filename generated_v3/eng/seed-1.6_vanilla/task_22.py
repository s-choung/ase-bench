from ase.build import bulk, surface, molecule

# Al(111) 3-layer slab (2x1 supercell, 10Å vacuum)
al_bulk = bulk('Al', 'fcc', a=4.046)
slab = surface(al_bulk, (111), 3, size=(2,1,1))
slab.center(vacuum=10, axis=2)

# N2 molecule
n2 = molecule('N2')

# Bridge site (2.0Å above top Al layer)
top_z = max(at.z for at in slab if at.symbol == 'Al')
top_al = [at for at in slab if at.symbol == 'Al' and abs(at.z - top_z) < 1e-6]
bridge_pos = [(top_al[0].x + top_al[1].x)/2,
              (top_al[0].y + top_al[1].y)/2,
              top_z + 2.0]

# Translate N2 to bridge site (lower N at bridge z)
n2_com = n2.center_of_mass()
n2.translate([bridge_pos[0] - n2_com[0],
              bridge_pos[1] - n2_com[1],
              bridge_pos[2] + n2.get_distance(0,1)/2 - n2_com[2]])

# Final structure
final = slab + n2

# Print results
print(f'Number of atoms: {len(final)}')
print(f'Atom types: {set(final.get_chemical_symbols())}')
