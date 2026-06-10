from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.io import write

h2o = molecule('H2O')
calc = EMT()
h2o.calc = calc

dyn = BFGS(h2o, trajectory='h2o_vibrations.traj')
dyn.run(fmax=0.02)

write('h2o_optimized.xyz', h2o)

from ase.vibes import calculate_vibrational_modes
modes = calculate_vibrational_modes(h2o)

print("Vibrational Modes:")
for i, mode in enumerate(modes):
    freq = mode[0]
    energy = mode[1]
    print(f"Mode {i+1}: Frequency = {freq:.2f} cm^-1, Energy = {energy:.4f} eV")
