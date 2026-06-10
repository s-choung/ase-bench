from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

print("=== Before Optimization ===")
print(f"Cell: {atoms.cell.lengths()}")
print(f"Energy: {atoms.get_potential_energy():.6f} eV")

filtered = FrechetCellFilter(atoms)
opt = BFGS(filtered, logfile=None)
opt.run(fmax=0.01)

print("\n=== After Optimization ===")
print(f"Cell: {atoms.cell.lengths()}")
print(f"Energy: {atoms.get_potential_energy():.6f} eV")
