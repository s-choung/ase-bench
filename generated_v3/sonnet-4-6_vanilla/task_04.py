from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

water = Atoms('H2O',
              positions=[[0, 0.76, -0.5],
                         [0, -0.76, -0.5],
                         [0, 0, 0.1]],
              )

water.calc = EMT()

e_before = water.get_potential_energy()
print(f"Energy before optimization: {e_before:.4f} eV")

opt = BFGS(water, trajectory='water_opt.traj')
opt.run(fmax=0.01)

e_after = water.get_potential_energy()
print(f"Energy after optimization:  {e_after:.4f} eV")
print(f"Energy difference: {e_after - e_before:.4f} eV")
print(f"Optimized positions:\n{water.get_positions()}")
