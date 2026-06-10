from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength

# Initial H2 with bond length 1.2 Å
atoms = Atoms('H2', positions=[(0,0,0), (1.2,0,0)])
atoms.calc = EMT()

print('Before constraint: bond length =', atoms.get_distance(0,1), 'Å, energy =', atoms.get_potential_energy(), 'eV')

# Apply FixBondLength constraint targeting 0.9 Å
atoms.set_constraint(FixBondLength(0,1,bondlength=0.9))
atoms.set_distance(0,1,0.9,fix=1)

print('After constraint: bond length =', atoms.get_distance(0,1), 'Å, energy =', atoms.get_potential_energy(), 'eV')
