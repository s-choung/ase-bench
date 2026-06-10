from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS

# Create Ni FCC bulk
atoms = bulk('Ni', 'fcc', a=3.5)
atoms.calc = EMT()

# Preconditioned LBFGS optimizer
opt = PreconLBFGS(atoms, precon='auto')
opt.run(fmax=0.01)

# Results
steps = opt.nsteps
energy = atoms.get_potential_energy()
cell = atoms.get_cell_lengths_and_angles()  # [a, b, c, alpha, beta, gamma]

print(f'Steps: {steps}')
print(f'Final energy: {energy:.6f} eV')
print(f'Cell lengths (a,b,c): {cell[0]:.4f}, {cell[1]:.4f}, {cell[2]:.4f} Å')
print(f'Cell angles (α,β,γ): {cell[3]:.2f}, {cell[4]:.2f}, {cell[5]:.2f}°')
