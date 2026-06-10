from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('H2O')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

vib = Vibrations(atoms, name='h2o_vib')
vib.run()
freqs = vib.get_frequencies()
energies = vib.get_energies()

for i, (freq, energy) in enumerate(zip(freqs, energies)):
    print(f"Mode {i}: {freq:.1f} cm^-1, {energy:.4f} eV")

vib.clean()
