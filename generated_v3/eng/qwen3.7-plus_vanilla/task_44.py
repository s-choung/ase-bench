from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms

atoms = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
atoms.set_tags([1 if z < atoms.positions[:, 2].mean() else 0 for _, _, z in atoms.positions])
atoms.set_constraint(FixAtoms(mask=[atom.tag == 1 for atom in atoms]))

pos_before = atoms.positions.copy()
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.05)

fixed_idx = [i for i, atom in enumerate(atoms) if atom.tag == 1]
print("Fixed atom coordinates before optimization:\n", pos_before[fixed_idx])
print("Fixed atom coordinates after optimization:\n", atoms.positions[fixed_idx])
