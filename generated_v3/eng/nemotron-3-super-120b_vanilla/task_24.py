from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc', a=4.05)
atoms.calc = EMT()
opt = LBFGS(atoms)
opt.run(fmax=0.01)
steps = opt.get_number_of_steps()
energy = atoms.get_potential_energy()
print(f'Optimization steps: {steps}')
print(f'Final energy: {energy:.6f} eV')
