from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# Create H2 molecule with an initial bond length of 0.74 Å
atoms = Atoms('H2', positions=[[0, 0, 0], [0, 0, 0.74]])
atoms.calc = EMT()

# Energy and bond length before applying the constraint
bond_before = atoms.get_distance(0, 1)
energy_before = atoms.get_potential_energy()
print(f'Before constraint: bond length = {bond_before:.3f} Å, energy = {energy_before:.4f} eV')

# Apply FixBondLength constraint to keep the bond at 0.9 Å
atoms.set_constraint(FixBondLength((0, 1), 0.9))
# Adjust the geometry to satisfy the constraint
atoms.set_distance(0, 1, 0.9)

# Energy and bond length after applying the constraint
bond_after = atoms.get_distance(0, 1)
energy_after = atoms.get_potential_energy()
print(f'After constraint: bond length = {bond_after:.3f} Å, energy = {energy_after:.4f} eV')
