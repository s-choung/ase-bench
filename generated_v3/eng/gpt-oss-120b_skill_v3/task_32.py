from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# Build H2O and assign EMT calculator
h2o = molecule('H2O')
h2o.calc = EMT()

# Geometry optimisation
BFGS(h2o).run(fmax=0.01)

# Vibrational analysis
vib = Vibrations(h2o, name='h2o_vib')
vib.run()
freqs = vib.get_frequencies()          # cm⁻¹
energs = vib.get_energies()            # eV

for i, (f, e) in enumerate(zip(freqs, energs), 1):
    print(f"Mode {i:2d}: {f:8.2f} cm⁻¹  {e:8.4f} eV")

vib.clean()
