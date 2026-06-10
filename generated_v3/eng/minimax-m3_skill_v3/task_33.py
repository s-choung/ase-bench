from ase import units
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('CH4')
atoms.calc = EMT()

opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='vib_ch4', steps=50)
vib.run()
vib.summary()

freqs = vib.get_frequencies()
real_freqs = [f for f in freqs if f > 0]

print("\n=== Real vibrational frequencies (cm^-1) ===")
for i, f in enumerate(real_freqs, 1):
    print(f"  Mode {i:2d}: {f:8.2f} cm^-1")
print(f"Total real modes: {len(real_freqs)} / {len(freqs)}")

vib.clean()
