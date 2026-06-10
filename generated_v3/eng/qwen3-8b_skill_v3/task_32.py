from ase.build import molecule
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('H2O')
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)
vib = Vibrations(atoms, name='h2o_vib')
vib.run()
freqs = vib.get_frequencies()
energies = vib.get_energies()
for f, e in zip(freqs, energies):
    print(f"{f:.1f} cm⁻¹, {e:.6f} eV")
