from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms

slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

bottom_layer = [a.index for a in slab if a.tag >= 3]
slab.set_constraint(FixAtoms(indices=bottom_layer))

print(f"총 원자 수: {len(slab)}")
