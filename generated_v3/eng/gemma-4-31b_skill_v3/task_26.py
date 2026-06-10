from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Ni', 'fcc', a=3.5)
atoms.calc = EMT()

# Use FrechetCellFilter for simultaneous cell and position optimization
filter_atoms = FrechetCellFilter(atoms)
opt = PreconLBFGS(filter_atoms, precon='auto')

opt.run(fmax=0.01)

print(f"Steps: {opt.trajectory.nsteps}")
print(f"Final Energy: {atoms.get_potential_energy():.4f} eV")
print(f"Cell parameters: {atoms.get_cell_lengths_and_angles()}")
