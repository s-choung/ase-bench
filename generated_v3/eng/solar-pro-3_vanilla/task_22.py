from ase import Atoms, Atom
from ase.build import make_supercell
from ase.spacegroup import crystal

# 3‑layer Al(111) slab
# 3 × 4 cell with 5 × 4 surface cell, vacuum 10 Å
super_cell = Atoms('Al', [(0, 0, 0), (0, 4, 0),
                          (5, 0, 0), (5, 4, 0),
                          (0, 0, 5), (0, 4, 5),
                          (5, 0, 5), (5, 4, 5)], pbc=True)
super_cell = make_supercell(super_cell, [[3, 0, 0], [0, 3, 0], [0, 0, 3]])  # 3x3 Al bulk

# Remove atoms beyond 5 layers from the surface
slab = crystal('Al', [(0, 0, 0)], spacegroup=164,
               settings=[3, 3, 3, 90, 90, 90])
slab = slab[:45]                     # 5 layers in bulk view
slab = slab.substitute(0, slab[:, 0])  # keep only the first surface layer
slab.translate([5, 2, 5])             # shift surface to (0,0,0)
slab = slab[slab.z <= 2.5]            # take three Al layers (z=0,1,2)

# Apply vacuum padding (reorder to have layers at 0, 1, 2 Å)
slab.sort(key=lambda s: s.z)
slab = slab[[i for i in range(len(slab)) if abs(slab[i].z - int(slab[i].z)) < 1e-3]]  # layers only
slab.set_cell((slab.cell[0], slab.cell[1], slab.cell[2] + slab.cell[2]))

# Roof‑style capping (top layer at z≈3 Å)
if slab[-1].z < 2.9:
    slab += Atoms('Al', positions=[(0, 0, 2.9)], pbc=False)
    slab = slab.repeat([1,1,1])
    slab.translate([0,0,slab[0].z])   # align caps

# Adsorb N2 as 'Nid' atoms (ET+ = 0, ET- = 1)
N2 = (Atom('Nid', [0, 0, 0.5]), Atom('Nid1', [0, 0, -0.5]))
slab += (N2[0] + (5.0, slab[0].z + 0.5),  # bridge site, half height
         N2[1] + (5.0, slab[0].z - 0.5))

# Output
print(f'Number of atoms: {len(slab)}')
print('Atom types:', set(slab.get_chemical_symbols()))
