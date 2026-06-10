from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Setup H2O
h2o = Atoms('H2O', [(0, 0, 0), (0.757, 0.586, 0), (-0.757, 0.586, 0)])
h2o.calc = EMT()

# Optimize geometry
BFGS(h2o).run(fmax=0.01)

# Compute vibrations
vib = Vibrations(h2o)
vib.run()
vib.summary()

# Convert and print
for freq in vib.get_frequencies():
    cm = freq * units.invcm
    e = freq * units._e / units._hbar
    print(f"{cm:.2f} cm^-1, {e:.4f} eV")
