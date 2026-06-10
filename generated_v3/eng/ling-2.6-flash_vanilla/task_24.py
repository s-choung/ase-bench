from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

a = 4.08  # Approximate lattice constant for Au in Angstrom
atoms = Atoms('Au', cell=[[0, a, a], [a, 0, a], [a, a, 0]], pbc=True)
atoms.set_calculator(EMT())
atoms.center(vacuum=5.0)

optimizer = LBFGS(atoms, trajectory=None)
optimizer.run(fmax=0.01)

print(f"Optimization steps: {optimizer.nsteps}")
print(f"Final energy: {atoms.get_potential_energy():.4f} eV")
