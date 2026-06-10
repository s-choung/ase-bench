from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

print(f"Initial a: {atoms.cell[0,0]:.4f} Å, Energy: {atoms.get_potential_energy():.4f} eV")

ucf = FrechetCellFilter(atoms)
BFGS(ucf).run(fmax=0.01)

print(f"Final a:   {atoms.cell[0,0]:.4f} Å, Energy: {atoms.get_potential_energy():.4f} eV")
