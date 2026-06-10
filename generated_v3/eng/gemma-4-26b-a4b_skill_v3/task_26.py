from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS
from ase.filters import FrechetCellFilter

# Setup Ni FCC bulk
atoms = bulk('Ni', 'fcc', a=3.5)
atoms.calc = EMT()

# Apply Filter for cell + position optimization
filt = FrechetCellFilter(atoms)

# Optimization with PreconLBFGS
opt = PreconLBFGS(filt, precon='auto')
opt.run(fmax=0.01)

# Output results
print(f"Steps: {opt.nsteps}")
print(f"Final Energy: {atoms.get_potential_energy():.4f} eV")
print(f"Cell Parameters: {atoms.get_cell_lengths_and_angles()}")
