from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

h2o = Atoms('H2O', positions=[[0, 0, 0], [1, 0, 0], [0, 1, 0]])
h2o.calc = EMT()

vib = Vibrations(h2o)
vib.run()
for i, freq in enumerate(vib.get_frequencies()):
    energy = freq * 0.0016  # meV to eV, then /1000
    if freq.imag != 0:
        print(f"Mode {i+1}: imaginary frequency {freq.imag:.2f} cm^-1, energy {energy:.4f} eV")
    else:
        print(f"Mode {i+1}: {freq:.2f} cm^-1, energy {energy:.4f} eV")
