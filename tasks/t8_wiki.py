"""T8 Wiki: Vibration analysis of N2 molecule"""
from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

n2 = Atoms('N2', positions=[(0, 0, 0), (0, 0, 1.1)])
n2.calc = EMT()

vib = Vibrations(n2, name='n2_vib')
vib.run()
frequencies = vib.get_frequencies()
print(f"Frequencies (cm^-1): {frequencies}")
vib.summary()
vib.clean()
