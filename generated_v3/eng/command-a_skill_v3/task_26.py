from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.build import bulk
from ase.optimize.precon import PreconLBFGS

# Create Ni FCC bulk
atoms = bulk('Ni', 'fcc', a=3.5)
atoms.calc = EMT()

# Set up PreconLBFGS optimizer with precon='auto'
opt = PreconLBFGS(atoms, precon='auto', trajectory='ni_opt.traj')

# Run optimization
opt.run(fmax=0.01)

# Get results
steps = opt.get_number_of_steps()
energy = atoms.get_potential_energy()
cell_params = atoms.get_cell_lengths_and_angles()

# Print results
print(f'Steps: {steps}')
print(f'Final energy: {energy:.6f} eV')
print(f'Cell parameters: {cell_params}')
