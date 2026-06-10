from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

atoms = fcc111('Au', size=(3, 3, 3), vacuum=1.0)
atoms.set_cell([12.0, 12.0, 12.0], scale_axes=True)

calc = EMT()
atoms.calc = calc

dyn = LBFGS(atoms, trajectory='Au_EMT.traj', fmax=0.01)
dyn.run()

print(f"Number of optimization steps: {dyn.nsteps}")
print(f"Final energy: {atoms.get_potential_energy()}")
