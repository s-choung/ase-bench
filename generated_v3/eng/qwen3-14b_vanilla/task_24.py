from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc', a=4.08)
atoms.set_calculator(EMT())
opt = LBFGS(atoms)
opt.run(fmax=0.01)
print(f'Steps: {opt.nsteps}, Energy: {atoms.get_potential_energy()} eV')
