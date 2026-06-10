"""T8 Vanilla: Vibration analysis of N2 molecule"""
from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibration

n2 = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)])
n2.calc = EMT()

vib = Vibration(n2)
vib.run()
frequencies = vib.get_frequencies()
print(f"Frequencies (cm^-1): {frequencies}")
vib.summary()
