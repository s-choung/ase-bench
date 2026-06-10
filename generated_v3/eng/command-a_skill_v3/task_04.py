from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create H2O molecule
H2O = Atoms('H2O', positions=[[0, 0, 0], [0, 0.757, 0.586], [0, -0.757, 0.586]])
H2O.calc = EMT()

# Print initial energy
initial_energy = H2O.get_potential_energy()
print(f'Initial energy: {initial_energy:.6f} eV')

# Optimize geometry
dyn = BFGS(H2O, trajectory='H2O_opt.traj')
dyn.run(fmax=0.001)

# Print final energy
final_energy = H2O.get_potential_energy()
print(f'Final energy: {final_energy:.6f} eV')
