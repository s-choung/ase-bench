from ase import db
from ase.build import bulk

# create Cu slab of (111) with 5 Å lateral size, fix the top layer
slab = bulk('Cu', 'fcc', a=4.0).lanl2dz
slab.set_pbc(True)
slab.translate([0,0,-2])          # start 2 layers below midplane
slab.relax(keep=['top'])          # relax everything but keep top layer fixed

# add slabs with 2, 3, 4 layers to an ASE database
db.save('cu_slabs.db',  # could be a list: [slab2, slab3, slab4]
        {'layers': 2},          # 2‑layer slab (copy)
        {'layers': 3},          # 3‑layer slab
        {'layers': 4})          # 4‑layer slab

# retrieve the 3‑layer slab and print its atom count
s3 = db.select('cu_slabs.db', layers=3)[0]
print('Number of atoms in 3‑layer slab:', len(s3))
