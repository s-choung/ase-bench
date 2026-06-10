from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.optimize import QuasiNewton

# initial H2 with bond 1.0 Å
mol = Atoms('H2', positions=[[0, 0, 0], [0, 0, 1.0]])
mol.calc = EMT()

e_before = mol.get_potential_energy()
d_before = mol.get_distance(0, 1)
print(f'Before: bond = {d_before:.4f} Å, energy = {e_before:.4f} eV')

# fix bond length to 0.9 Å
mol.set_constraint(FixBondLength(0, 1, distance=0.9))

opt = QuasiNewton(mol, logfile=None)
opt.run(fmax=0.01)

e_after = mol.get_potential_energy()
d_after = mol.get_distance(0, 1)
print(f'After : bond = {d_after:.4f} Å, energy = {e_after:.4f} eV')
