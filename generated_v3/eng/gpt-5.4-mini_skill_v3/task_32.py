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

for i, (f, e) in enumerate(zip(freqs, energies), 1):
    print(f"Mode {i}: {f:.2f} cm^-1, {e:.6f} eV")

vib.clean()
