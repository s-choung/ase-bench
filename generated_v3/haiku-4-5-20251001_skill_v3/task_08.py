from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('N2')
atoms.calc = EMT()

opt = BFGS(atoms)
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='vib')
vib.run()

freqs = vib.get_frequencies()
print("Vibrational frequencies (cm⁻¹):")
for i, f in enumerate(freqs):
    print(f"Mode {i}: {f:.2f} cm⁻¹")

vib.summary()
vib.clean()
