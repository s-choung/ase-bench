from ase.build import fcc111, molecule
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.io import write
import numpy as np

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0, orthogonal=True)
co = molecule('CO')
co.rotate(90, 'y', rotate_cell=False)
co.translate(slab.get_positions().mean(axis=0) + [0, 0, 2.0])

atoms = slab + co
atoms.set_cell(slab.get_cell())
atoms.set_pbc(True)

z = atoms.get_positions()[:, 2]
bottom = np.isclose(z, z.min())
c_idx = len(atoms) - 2
o_idx = len(atoms) - 1
atoms.set_constraint([FixAtoms(mask=bottom), FixBondLength(c_idx, o_idx)])

atoms.calc = EMT()
opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.05)

energy = atoms.get_potential_energy()
co_dist = atoms.get_distance(c_idx, o_idx)
print(f"Final energy: {energy:.6f} eV")
print(f"C-O distance: {co_dist:.6f} Å")
