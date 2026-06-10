from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('N2')
atoms.calc = EMT()

opt = BFGS(atoms, trajectory=None)
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='vib_n2')
vib.run()

freqs = vib.get_frequencies()
print("N2 진동 주파수 (cm⁻¹):")
for i, f in enumerate(freqs):
    print(f"  Mode {i}: {f:.4f} cm⁻¹")

vib.summary()
vib.clean()
