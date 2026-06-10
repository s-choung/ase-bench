from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS
from ase.io import Trajectory

atoms = bulk('Ni', 'fcc', a=3.5)
atoms.calc = EMT()

opt = PreconLBFGS(atoms, precon='auto', trajectory='ni_opt.traj')
opt.run(fmax=0.01)

print(f"Steps: {opt.get_number_of_steps()}")
print(f"Final Energy: {atoms.get_potential_energy():.4f} eV")
print(f"Cell Parameters: {atoms.cell.cellpar()}")
