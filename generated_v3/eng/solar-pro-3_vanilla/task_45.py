from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# H2 molecule (a simple two‑atom system)
mol = Atoms('H2', positions=[(0.0, 0.0, 0.0), (0.9, 0.0, 0.0)])

# EMT calculator
calc = EMT()
mol.set_calculator(calc)

# energy and bond length before constraint
e0 = mol.get_potential_energy()
tip0 = mol.get_center_of_mass()  # dummy call – forces are computed
b0 = mol.bonds[0].length

print(f'Before constraint: length = {b0:.3f} Å, energy = {e0:.3} eV')

# apply FixBondLength constraint (same length, no change)
mol.constraints = [FixBondLength(mol.bonds[0])]

# recalculate forces to let the fix act
mol.get_potential_energy()

# energy and bond length after constraint
e1 = mol.get_potential_energy()
b1 = mol.bonds[0].length

print(f'After constraint:   length = {b1:.3f} Å, energy = {e1:.3} eV')
