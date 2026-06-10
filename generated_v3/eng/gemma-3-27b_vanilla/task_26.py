from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS

atoms = fcc111('Ni', size=(3, 3, 3))

calc = EMT(precon='auto')
atoms.calc = calc

dyn = PreconLBFGS(atoms, trajectory='Ni_optimization.traj')
dyn.run(fmax=0.01)

print(f"Number of steps: {dyn.steps}")
print(f"Final energy: {atoms.get_potential_energy()}")
print(f"Final cell parameters: {atoms.cell}")
