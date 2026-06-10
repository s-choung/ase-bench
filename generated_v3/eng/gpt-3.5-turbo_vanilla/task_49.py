from ase import Atoms
from ase.build import bulk, stack
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.eos import calculate_eos

# Calculate equilibrium lattice constant using Equation of State
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
volumes, energies = calculate_eos(EMT(), atoms, 'fcc')

# Create (111) 4-layer slab with equilibrium lattice constant
slab = stack(atoms, (1, 1, 4))

# Attach EMT calculator and fix bottom 2 layers
slab.set_calculator(EMT())
slab[:(2 * len(atoms))] = slab[:(2 * len(atoms))].position

# Run BFGS surface relaxation
relax = BFGS(slab)
relax.run(fmax=0.01)

# Print final energy and average z-coordinate for each layer
print('Final Energy:', slab.get_potential_energy())
for i in range(4):
    avg_z = slab[i * len(atoms):(i + 1) * len(atoms)].get_positions()[:, 2].mean()
    print(f'Layer {i+1}: Average z-coordinate = {avg_z}')
