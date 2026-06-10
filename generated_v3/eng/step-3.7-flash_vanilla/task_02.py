from ase.build import bulk, surface, molecule

slab = surface(bulk('Pt', 'fcc'), (1, 1, 1), layers=4, vacuum=10)
z_top = slab.positions[:, 2].max()
ads = slab[slab.positions[:, 2] == z_top][0].position + [0, 0, 1.8]
co = molecule('CO')
co.translate(ads - co.positions[0])
print(len(slab + co))
