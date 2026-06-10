from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = molecule('H2O')
calc = EMT()
atoms.set_calculator(calc)

energy_before = atoms.get_potential_energy()
print(f"Energy before optimization: {energy_before} eV")

dyn = BFGS(atoms, trajectory='H2O_optimization.traj')
dyn.run(fmax=0.02)

energy_after = atoms.get_potential_energy()
print(f"Energy after optimization: {energy_after} eV")
