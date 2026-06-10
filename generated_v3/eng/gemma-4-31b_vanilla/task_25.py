from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import ExpCellFilter

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

print(f"Initial cell: {atoms.get_cell()[0,0]:.3f} Å")
print(f"Initial energy: {atoms.get_total_energy():.4f} eV")

ecf = ExpCellFilter(atoms)
opt = BFGS(ecf, trajectory='opt.traj')
opt.run(fmax=0.01)

print(f"Final cell: {atoms.get_cell()[0,0]:.3f} Å")
print(f"Final energy: {atoms.get_total_energy():.4f} eV")
