from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.geometry import get_distance

# Create H2 molecule, arbitrary initial bond length
h2 = Atoms('H2', positions=[[0, 0, 0], [0, 0, 1.0]])
h2.calc = EMT()
ene_before = h2.get_potential_energy()
bond_before = get_distance(h2.positions, 0, 1)

# Apply FixBondLength constraint to set bond to 0.9 Å
h2.set_constraint(FixBondLength(0, 1, 0.9))
# Move atoms to match the fixed bond length
h2.positions[1] = [0, 0, 0.9]
ene_after = h2.get_potential_energy()
bond_after = get_distance(h2.positions, 0, 1)

print(f'Before constraint: Bond = {bond_before:.3f} Å, Energy = {ene_before:.3f} eV')
print(f'After constraint:  Bond = {bond_after:.3f} Å, Energy = {ene_after:.3f} eV')
