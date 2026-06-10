from ase.build import mx2
from ase import Atoms

# MoS2 monolayer (primitive cell)
atoms = mx2('MoS2', a=3.16, c=12.3, nlayers=1)

# Add 10 Å vacuum along the z‑direction
atoms.center(vacuum=10.0, axis=2)

print('Cell size:')
print(atoms.cell)
