from ase import Atoms
from ase.cell import Cell
from ase.constraints import FixAtoms
from ase.filters import FrechetCellFilter, ExpCellFilter
from ase.spacegroup import crystal

# Build Cu FCC (2x2x2) supercell using bulk + scaling
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
# Optionally relax cells & positions
opt = BFGS(FrechetCellFilter(atoms)).run(fmax=0.05)
# Optionally fix positions to avoid further relaxation
atoms.set_constraint(FixAtoms())

# Compute distances from atom 0 to every other atom with periodic BCs
positions = atoms.get_positions()
dists = get_distances(positions[0], positions, mic=True)

# Print results
print('Min distance (Å):', dists.min())
print('Max distance (Å):', dists.max())
