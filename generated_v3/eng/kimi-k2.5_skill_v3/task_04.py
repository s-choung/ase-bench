from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = molecule('H2O')
atoms.center(vacuum=5.0)
atoms.calc = EMT()

print('Before:', atoms.get_potential_energy())

BFGS(atoms, logfile=None).run(fmax=0.01)

print('After:', atoms.get_potential_energy())
