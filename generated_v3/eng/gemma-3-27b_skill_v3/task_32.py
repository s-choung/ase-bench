from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
import numpy as np

atoms = Atoms('H2O', positions=[(0.0, 0.0, 0.0), (0.0, 0.757, 0.586), (0.0, -0.757, 0.586)])
atoms.calc = EMT()
opt = BFGS(atoms)
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='vib')
vib.run()
frequencies = vib.get_frequencies()
energies = vib.get_energies()

print("Vibrational Modes:")
for i in range(len(frequencies)):
    print(f"Mode {i+1}: Frequency = {frequencies[i]:.2f} cm^-1, Energy = {energies[i]:.4f} eV")
