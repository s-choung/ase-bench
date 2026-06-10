from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = molecule('H2O')
atoms.calc = EMT()

e_initial = atoms.get_potential_energy()
print(f'Initial energy: {e_initial:.6f} eV')

opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.05)

e_final = atoms.get_potential_energy()
print(f'Final energy: {e_final:.6f} eV')
