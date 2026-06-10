from ase import Atoms
from ase.build import bulk, surface

# Create copper bulk structure
a = 3.61  # lattice constant of copper in angstrom
bulk_Cu = bulk('Cu', 'fcc', a=a)

# Create (2,1,1) surface with 3 layers and 10 angstroms vacuum
slab = surface(bulk_Cu, (2,1,1), 3, vacuum=10)

print('Number of atoms:', len(slab))
print('Cell:', slab.get_cell())
