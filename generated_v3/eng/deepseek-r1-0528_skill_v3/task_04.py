from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = molecule('H2O')
atoms.calc = EMT()
initial_energy = atoms.get_potential_energy()

opt = BFGS(atoms)
opt.run(fmax=0.05)
final_energy = atoms.get_potential_energy()

print(f"Initial energy: {initial_energy:.5f} eV")
print(f"Final energy: {final_energy:.5f} eV")
