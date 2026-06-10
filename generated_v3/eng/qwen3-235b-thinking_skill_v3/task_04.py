from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = molecule('H2O')
atoms.calc = EMT()
e_init = atoms.get_potential_energy()
opt = BFGS(atoms)
opt.run(fmax=0.01)
e_final = atoms.get_potential_energy()
print(f"Initial energy: {e_init:.6f} eV")
print(f"Final energy: {e_final:.6f} eV")
