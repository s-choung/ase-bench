from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.optimize import BFGS

atoms = Atoms('H2', positions=[[0., 0., 0.], [0.7, 0., 0.]])
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

e_before = atoms.get_potential_energy()
d_before = atoms.get_distance(0, 1)
print(f'Before: d={d_before:.3f} Å, E={e_before:.3f} eV')

atoms.set_distance(0, 1, 0.9, fix=0.5)
atoms.set_constraint(FixBondLength(0, 1))
e_after = atoms.get_potential_energy()
d_after = atoms.get_distance(0, 1)
print(f'After: d={d_after:.3f} Å, E={e_after:.3f} eV')
