from ase import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc')
atoms.calc = EMT()
opt = LBFGS(atoms)
opt.run(fmax=0.01)
print(f"Steps: {opt.nsteps}, Energy: {atoms.get_potential_energy()}")
