from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

print(f"Initial cell: {atoms.cell.cellpar()[:3]}")
print(f"Initial energy: {atoms.get_potential_energy():.4f} eV")

ecf = FrechetCellFilter(atoms)
opt = BFGS(ecf, logfile='opt.log')
opt.run(fmax=0.01)

print(f"Final cell: {atoms.cell.cellpar()[:3]}")
print(f"Final energy: {atoms.get_potential_energy():.4f} eV")
