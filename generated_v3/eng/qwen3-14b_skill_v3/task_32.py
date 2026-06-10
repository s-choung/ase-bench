from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('H2O')
atoms.calc = EMT()

opt = BFGS(atoms)
opt.run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()
energies = vib.get_energies()

for i in range(len(freqs)):
    print(f"Mode {i+1}: Frequency = {freqs[i]:.2f} cm⁻¹, Energy = {energies[i]:.6f} eV")
