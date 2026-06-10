from ase.build import bulk
from ase.calculators.emt import EMT
from ase.constraints import FrechetCellFilter
from ase.optimize import BFGS

# initial Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

print("Before optimization:")
print("Cell (Å):", atoms.get_cell().lengths())
print("Energy (eV):", atoms.get_potential_energy())

# filter to allow simultaneous cell & atomic relaxation
filtered_atoms = FrechetCellFilter(atoms)

opt = BFGS(filtered_atoms, logfile=None)
opt.run(fmax=0.01)

print("\nAfter optimization:")
print("Cell (Å):", atoms.get_cell().lengths())
print("Energy (eV):", atoms.get_potential_energy())
