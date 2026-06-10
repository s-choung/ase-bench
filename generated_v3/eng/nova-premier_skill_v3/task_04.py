from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

atoms = Atoms('H2O', positions=[[0,0,0],[0,-0.757,0.587],[0,0.757,0.587]])
atoms.calc = EMT()

print(f"Initial energy: {atoms.get_potential_energy():.3f} eV")
opt = BFGS(atoms)
opt.run(fmax=0.01)
print(f"Final energy: {atoms.get_potential_energy():.3f} eV")
