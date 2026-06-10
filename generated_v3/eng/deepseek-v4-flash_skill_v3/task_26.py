from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.filters import FrechetCellFilter

# Create Ni FCC bulk with initial guess for lattice constant
atoms = bulk('Ni', 'fcc', a=3.52)
atoms.calc = EMT()

# Use FrechetCellFilter to optimize both cell and atomic positions
filter = FrechetCellFilter(atoms)
opt = PreconLBFGS(filter, precon='auto')
nsteps = opt.run(fmax=0.01)

# Get final energy and cell parameters
energy = atoms.get_potential_energy()
a, b, c = atoms.cell.lengths()

print(f'Steps: {opt.get_number_of_steps()}')
print(f'Final energy: {energy:.6f} eV')
print(f'Cell parameters: a={a:.4f}, b={b:.4f}, c={c:.4f} Å')
