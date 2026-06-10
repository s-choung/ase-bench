from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

h2o = Atoms('H2O', positions=[(0, 0, 0), (0, 0, 0.957), (0.957, 0, 0)])
h2o.set_calculator(EMT())

vib = Vibrations(h2o)
vib.run()
vib.summary()

for i, freq in enumerate(vib.get_frequencies()):
    if freq > 0:
        energy_eV = freq * 0.000123984  # cm^-1 to eV
        print(f"Mode {i+1}: {freq:.1f} cm^-1, {energy_eV:.4f} eV")
