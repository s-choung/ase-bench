from ase import units
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = molecule('H2O')
atoms.calc = EMT()

energy_before = atoms.get_potential_energy()
opt = BFGS(atoms, trajectory='opt.traj')
opt.run(fmax=0.01)
energy_after = atoms.get_potential_energy()

print(f"Energy before optimization: {energy_before:.3f} eV")
print(f"Energy after optimization: {energy_after:.3f} eV")
