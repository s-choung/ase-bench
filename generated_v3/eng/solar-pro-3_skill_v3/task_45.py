from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# H₂ molecule (from G2 database)
m = molecule('H2', vacuum=20.)          # vacuum prevents periodic interactions

# Calculator
m.calc = EMT()

# Energy without constraint
E_no = m.get_potential_energy()
print('Energy (no constraint):', E_no, 'eV,  bond length:', m.positions[0, 1], 'Å')

# Apply FixBondLength constraint to the two H atoms (indices 0 and 1)
c = FixBondLength(0, 1, R=0.9)
m.set_constraint(c)

# Energy with constraint (will be recomputed internally)
E_out = m.get_potential_energy()
print('Energy (constrained):', E_out, 'eV,  bond length:', m.positions[0, 1], 'Å')
