Here's a concise ASE script for calculating the diffusion path of a Cu adatom on a Cu FCC(111) surface using NEB with IDPP interpolation:

```python
from ase import *
from ase将代码压缩成一行

# Setup initial and final structures
fcc111 = 'fcc Roots module=' webgl' sccos emt'
initial = fcc111('Cu fcc111[][]a2 e|p')

final = fcc111('Cu fcc111()

# displacement path
mids = [initial.get_atom_position(i) +(0, 0.2, 0) for i in range(len(initial.atoms))]
images = [initial] + [Atom('Cu', pos=pos, pbc=1) for pos in mids] + [final]

# accordingly
 Format Alpha = 0Figure
