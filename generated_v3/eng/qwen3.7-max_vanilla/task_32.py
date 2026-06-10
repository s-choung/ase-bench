from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.units import invcm

h2o = molecule('H2O', vacuum=3.0)
h2o.calc = EMT()

vib = Vibrations(h2o)
vib.run()

for i, freq in enumerate(vib.get_frequencies()):
    print(f"Mode {i}: {freq:8.2f} cm^-1 | {freq * invcm:8.5f} eV")
