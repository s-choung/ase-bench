from ase import Atoms
from ase.build import fcc111, molecule
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
co = molecule('CO')
from ase.build import add_adsorbate
add_adsorbate(slab, co, height=1.8, position='ontop')

bottom_layer_indices = [i for i, atom in enumerate(slab) if atom.position[2] < slab.cell[2, 2] / 2 - 1.0]
slab.set_constraint(FixAtoms(indices=bottom_layer_indices))

slab.set_constraint(FixBondLength(0, 1))

slab.calc = EMT()
opt = BFGS(slab)
opt.run(fmax=0.05)

final_energy = slab.get_potential_energy()
co_distance = np.linalg.norm(slab.positions[0] - slab.positions[1])

print(f"Final energy: {final_energy:.4f} eV")
print(f"C-O distance: {co_distance:.4f} Angstrom")
