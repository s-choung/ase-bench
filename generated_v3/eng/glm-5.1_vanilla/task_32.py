from ase.build import molecule
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

atoms = molecule('H2O')
atoms.calc = EMT()

vib = Vibrations(atoms)
vib.run()

frequencies = vib.get_frequencies()
energies = vib.get_energies()

for i, (freq, energy) in enumerate(zip(frequencies, energies)):
    print(f"Mode {i+1}: {freq:.2f} cm^-1, {energy:.6f} eV")

vib.clean()
