from ase.build import molecule
from ase.constraints import FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = molecule('H2')
atoms.calc = EMT()

d_before = atoms.get_distance(0, 1)
e_before = atoms.get_potential_energy()
print(f"Before: bond length = {d_before:.4f} Å, energy = {e_before:.6f} eV")

atoms.set_distance(0, 1, 0.9)
atoms.set_constraint(FixBondLength(0, 1))

opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.01)

d_after = atoms.get_distance(0, 1)
e_after = atoms.get_potential_energy()
print(f"After:  bond length = {d_after:.4f} Å, energy = {e_after:.6f} eV")
