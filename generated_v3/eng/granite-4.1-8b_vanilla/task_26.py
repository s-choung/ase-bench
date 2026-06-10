from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS
from ase.io import write

# Create Ni FCC bulk structure
a = 3.52  # Ni lattice constant in Å
bulk_fcc_Ni = Atoms('Ni', positions=[[0, 0, 0], [a/2, a/2, 0], [a/2, 0, a/2], [0, a/2, a/2]],
                   cell=(a, a, a), pbc=True)

# Set up EMT calculator with automatic preconditioner
calc = EMT(label='EMT', precon='auto')
bulk_fcc_Ni.calc = calc

# Optimize using PreconLBFGS
opt = PreconLBFGS(bulk_fcc_Ni, trajectory=None, logfile=None)
opt.run(fmax=0.01)

# Output results
print(f'Number of steps: {opt.get_nsteps()}')
print(f'Final energy: {opt.get_potential_energy():.6f}')
print('Final cell parameters (Å):')
print(bulk_fcc_Ni.cell)
