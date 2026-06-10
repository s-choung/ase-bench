from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# Build Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Print initial cell and energy
cell0 = atoms.get_cell_lengths_and_angles()
E0 = atoms.get_potential_energy()
print('Before optimization:')
print(f'Cell (a,b,c,α,β,γ): {cell0}')
print(f'Energy: {E0:.6f} eV')

# Optimize lattice and positions
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

# Print final cell and energy
cell1 = atoms.get_cell_lengths_and_angles()
E1 = atoms.get_potential_energy()
print('\nAfter optimization:')
print(f'Cell (a,b,c,α,β,γ): {cell1}')
print(f'Energy: {E1:.6f} eV')
