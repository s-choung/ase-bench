from ase import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = bulk('Au', 'fcc', a=4.0)
atoms.calc = EMT()
opt = LBFGS(atoms)
opt.run(fmax=0.01)
print(f"Optimization steps: {opt.nsteps}")
print(f"Final potential energy: {atoms.get_potential_energy()} eV")
