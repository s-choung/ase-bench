from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule("H2O")
atoms.calc = EMT()

BFGS(atoms, logfile=None).run(fmax=1e-3)

vib = Vibrations(atoms, name="h2o_emt_vib")
vib.run()

freqs = vib.get_frequencies()
energies = vib.get_energies()

for i, (f, e) in enumerate(zip(freqs, energies), 1):
    print(f"mode {i:2d}: frequency = {f:.6f} cm^-1, energy = {e:.8f} eV")

vib.clean()
