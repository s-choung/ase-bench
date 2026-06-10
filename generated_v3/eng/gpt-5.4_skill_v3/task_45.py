from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

atoms = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.9]])
atoms.calc = EMT()

d_before = atoms.get_distance(0, 1)
e_before = atoms.get_potential_energy()

atoms.set_constraint(FixBondLength(0, 1))
d_after = atoms.get_distance(0, 1)
e_after = atoms.get_potential_energy()

print(f'Before constraint: bond length = {d_before:.3f} Å, energy = {e_before:.6f} eV')
print(f'After constraint:  bond length = {d_after:.3f} Å, energy = {e_after:.6f} eV')
