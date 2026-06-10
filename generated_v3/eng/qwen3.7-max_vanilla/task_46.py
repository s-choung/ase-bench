from ase.build import fcc111, molecule
from ase.constraints import FixAtoms, FixBondLength
from ase.optimize import BFGS
from ase.calculators.lj import LennardJones
import numpy as np

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
co = molecule('CO')

top_idx = np.argmax(slab.positions[:, 2])
co.positions -= co.positions[0]
co.positions += slab.positions[top_idx] + [0, 0, 2.0]

atoms = slab + co
atoms.calc = LennardJones()

bottom_z = min(slab.positions[:, 2])
fix_indices = np.where(np.isclose(slab.positions[:, 2], bottom_z))[0]

n = len(slab)
atoms.set_constraint([
    FixAtoms(indices=fix_indices),
    FixBondLength(n, n + 1)
])

BFGS(atoms).run(fmax=0.05)

print(f"Final energy: {atoms.get_potential_energy():.4f} eV")
print(f"C-O distance: {atoms.get_distance(n, n + 1):.4f} A")
