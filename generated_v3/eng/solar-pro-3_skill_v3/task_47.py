from ase import Atoms
from ase.neighborlist import natural_cutoffs
from ase.build import bulk

# Build a 3×3×3 Cu FCC supercell
latt = bulk('Cu', 'fcc', a=4.0)
atoms = bulk('Cu', 'fcc').repeat((3, 3, 3))

# Assign tags (0‑based indices)
atoms.tag = np.arange(len(atoms))

# Precompute neighborlist (natural cutoffs, sorted)
nl = natural_cutoffs(tol=1e-5, sorted=True)
nl.update(atoms)

# Count unique neighbors per atom
nbr_list = nl.get_neighbors(atoms)
unique_counts = [len(set(nnbr)) for nbr in nbr_list]

print('Coordination number per atom:', unique_counts)
print('Average coordination number:', np.mean(unique_counts))
