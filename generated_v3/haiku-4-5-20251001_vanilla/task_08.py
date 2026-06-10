from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.constraints import StrainFilter

atoms = molecule('N2')
atoms.center(vacuum=5.0)
atoms.calc = EMT()

vib = Vibrations(atoms)
vib.run()
vib.summary()

frequencies = vib.get_frequencies()
print("\nVibrational frequencies (cm^-1):")
for i, freq in enumerate(frequencies):
    print(f"Mode {i}: {freq:.2f} cm^-1")
