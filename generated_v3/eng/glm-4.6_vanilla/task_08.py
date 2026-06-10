from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

n2 = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])
n2.calc = EMT()

vib = Vibrations(n2)
vib.run()
freqs = vib.get_frequencies()

print('Vibrational frequencies (cm^-1):')
for i, freq in enumerate(freqs):
    if abs(freq) > 1e-5:
        print(f'Mode {i+1}: {freq:.2f}')

vib.clean()
