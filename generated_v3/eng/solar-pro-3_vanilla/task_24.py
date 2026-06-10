from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

# Create a FCC bulk gold structure in a 2x2x2 cell
atoms = Atoms('Au',
              positions=[[0.5, 0.5, 0.5], [-0.5, -0.5, 0.5]],
              cell='4.08 4.08 4.08',  # approximate cubic cell of 2×2×2 Au
              pbc=True)

atoms.set_calculator(EMT())
opt = LBFGS(atoms, trajectory='lbfgs.traj')
opt.run(fmax=0.01)

print(f'Optimization steps: {opt.nsteps}')
print(f'Final energy: {atoms.get_potential_energy()} eV')
