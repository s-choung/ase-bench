from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

h2o = molecule('H2O')
h2o.calc = EMT()

vib = Vibrations(h2o)
vib.run()

eV_to_cm1 = 8065.54
for i, energy in enumerate(vib.get_energies()):
    freq_cm1 = energy * eV_to_cm1
    print(f"Mode {i}: {freq_cm1:.2f} cm^-1, {energy:.6f} eV")
