from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule("H2O")
atoms.calc = EMT()

BFGS(atoms, logfile=None).run(fmax=0.01)

vib = Vibrations(atoms, name="h2o_emt_vib")
vib.clean()
vib.run()

freqs = vib.get_frequencies()
energies = vib.get_energies()

for i, (freq, energy) in enumerate(zip(freqs, energies), 1):
    print(f"Mode {i:2d}: {freq.real:10.2f} cm^-1   {energy.real:10.6f} eV")

vib.clean()
