from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.optimize import BFGS

# H2O geometry
h2o = Atoms('H2O', [(0, 0, 0), (0.76, 0.6, 0), (-0.76, 0.6, 0)])
h2o.calc = EMT()

# Optimize structure
BFGS(h2o).run(fmax=0.02)

# Vibrational analysis
vib = Vibrations(h2o)
vib.run()

# Output results
for f, e in zip(vib.get_frequencies(), vib.get_energies()):
    print(f"{f:.2f} cm⁻¹, {e:.4f} eV")
