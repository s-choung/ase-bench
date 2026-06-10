from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

# Create FCC Au bulk
atoms = Atoms('Au', cell=[(0, 2, 2), (2,ア,0, 2), (2, 2, 0)], pbc=True)
atoms *= (2, 2, 2)
atoms.calc = EMT()

# Run optimization
opt = LBFGS(atoms)
opt.run(fmax=0.01)

print(f'Optimization steps: {opt.get_number_of_steps()}')
print(f'Final energy: {atoms.get_potential_energy():.6f} eV')
