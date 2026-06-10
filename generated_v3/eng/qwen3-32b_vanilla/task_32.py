from ase import Molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

h2o = Molecule('H2O')
h2o.calc = EMT()
vib = Vibrations(h2o)
vib.run()
freqs = vib.get_frequencies()

for freq in freqs:
    cm_inv = freq * 33.356
    eV = freq * 0.0020678
    print(f"{cm_inv:.2f} cm⁻¹   {eV:.6f} eV")
