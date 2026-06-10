from ase.build import Bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = Bulk('Au', 'fcc', a=4.08)
atoms.set_calculator(EMT())
opt = LBFGS(atoms, fmax=0.01)
opt.optimize()
print(f"Steps: {opt.nsteps}")
print(f"Final energy: {atoms.get_potential_energy()} eV")
