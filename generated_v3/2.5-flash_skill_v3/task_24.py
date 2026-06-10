from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Au', 'fcc', a=4.08)
atoms.calc = EMT()

optimizer = LBFGS(FrechetCellFilter(atoms), trajectory='au_fcc_opt.traj')
steps = optimizer.run(fmax=0.01)

final_energy = atoms.get_potential_energy()
print(f"Optimization completed in {steps} steps.")
print(f"Final potential energy: {final_energy:.4f} eV")
