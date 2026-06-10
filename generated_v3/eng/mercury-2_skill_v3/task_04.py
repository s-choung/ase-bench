from ase import units
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Build water molecule
atoms = molecule('H2O')
atoms.calc = EMT()

# Energy before optimization
E_before = atoms.get_potential_energy()
print('Energy before:', E_before, 'eV')

# Geometry optimization
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Energy after optimization
E_after = atoms.get_potential_energy()
print('Energy after:', E_after, 'eV')
