from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('H2O')
atoms.calc = EMT()
opt = BFGS(atoms)
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='h2o_vib')
vib.run()
freqs = vib.get_frequencies()
energies = vib.get_energies()

for i, (f, e) in enumerate(zip(freqs, energies)):
    print(f"Mode {i}: frequency = {f:.2f} cm⁻¹, energy = {e:.4f} eV")

vib.clean()
