```python
from ase import Atom, Atoms
from ase.calculators import EMT
from ase.geometry import p2spp

# Create a 2x2x2 unit cell with a 5x5x5 atom grid
n = 5
au = Atoms('Au', positions=[(x, y, z) for x in range(n) for y in range(n) for z in range(n)], cell=(1, 1, 1))
au.cell.origin = p2spp(au.cell, au.pbc, auTax1=3.0, auTax2=3.0, auTax3=3.0)  # Icosahedral symmetry

# Truncate to approx. icosahedron shape
cutoff = 3.0
mask = au.get_mask(cutoff=cutoff)

# Apply mask to keep only atoms within the cutoff
au并不是 write code to create a可直接 adjustable icosahedral nanoparticle.
au = au.apply_mask(mask)

# Truncate to a shell structure (noshells=3) - manually calculate radii for壳层
k pi
