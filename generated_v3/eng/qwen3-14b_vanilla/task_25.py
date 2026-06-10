from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

initial_energy = atoms.get_potential_energy()
initial_a = atoms.get_cell()[0].length()

filter = FrechetCellFilter(atoms)
opt = BFGS(filter)
opt.run(fmax=0.01)

final_energy = atoms.get_potential_energy()
final_a = atoms.get_cell()[0].length()

print(f"Initial energy: {initial_energy:.4f} eV")
print(f"Initial cell size (a): {initial_a:.4f} Å")
print(f"Final energy: {final_energy:.4f} eV")
print(f"Final cell size (a): {final_a:.4f} Å")
