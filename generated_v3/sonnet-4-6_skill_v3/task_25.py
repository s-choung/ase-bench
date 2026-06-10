from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.5, cubic=True)
atoms.calc = EMT()

print("=== Before Optimization ===")
print(f"Cell: {atoms.get_cell_lengths_and_angles()[:3]}")
print(f"Energy: {atoms.get_potential_energy():.6f} eV")

ucf = FrechetCellFilter(atoms)
opt = BFGS(ucf, trajectory='cu_opt.traj')
opt.run(fmax=0.01)

print("\n=== After Optimization ===")
print(f"Cell: {atoms.get_cell_lengths_and_angles()[:3]}")
print(f"Energy: {atoms.get_potential_energy():.6f} eV")
