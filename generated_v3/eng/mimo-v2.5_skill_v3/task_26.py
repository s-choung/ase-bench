from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.filters import FrechetCellFilter

# Build Ni FCC bulk and set calculator
atoms = bulk('Ni', 'fcc', a=3.52, cubic=True)
atoms.calc = EMT()

# Optimize cell and positions using PreconLBFGS with FrechetCellFilter
fcopt = FrechetCellFilter(atoms)
opt = PreconLBFGS(fcopt, precon='auto', logfile='-')
opt.run(fmax=0.01)

# Get and print results
nsteps = opt.get_number_of_steps()
energy = atoms.get_potential_energy()
cell = atoms.get_cell()

print(f"Optimization completed in {nsteps} steps")
print(f"Final energy: {energy:.6f} eV")
print(f"Cell parameters (Å):")
print(f"  a = {cell.lengths()[0]:.4f}")
print(f"  b = {cell.lengths()[1]:.4f}")
print(f"  c = {cell.lengths()[2]:.4f}")
print(f"  α = {cell.angles()[0]:.2f}°")
print(f"  β = {cell.angles()[1]:.2f}°")
print(f"  γ = {cell.angles()[2]:.2f}°")
