from ase.lattice.bulk import bulk
from ase.build import slab
from ase.units import Angstrom

# Create bulk BCC Fe
fe_bulk = bulk('Fe', 'bcc', a=2.866 * Angstrom)

# Create BCC(110) slab with 4 layers and specified size
slab = slab(
    fe_bulk,
    plane=['1', '1', '0'],
    size=(2, 2, 4),
    vacuum=10 * Angstrom,
    orthogonal=True
)

# Print the number of atoms and cell size
print(f"Number of atoms: {len(slab)}")
print(f"Cell size: {slab.cell.toarray().flatten()}")
