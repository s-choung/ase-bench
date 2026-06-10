from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule("H2O")
atoms.calc = EMT()

BFGS(atoms, logfile=None).run(fmax=0.01)

vib = Vibrations(atoms, name="h2o_vib")
vib.run()

freqs = vib.get_frequencies()
energies = vib.get_energies()

for i, (freq, energy) in enumerate(zip(freqs[-3:], energies[-3:]), start=1):
    print(f"Mode {i}: frequency = {freq:.2f} cm^-1, energy = {energy:.6f} eV")

vib.clean()
