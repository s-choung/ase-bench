from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
import numpy as np

d = 1.09
atoms = Atoms('CH4',
              positions=[(0, 0, 0),
                         (d, d, d),
                         (-d, -d, d),
                         (-d, d, -d),
                         (d, -d, -d)])

atoms.calc = EMT()

opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.001)

vib = Vibrations(atoms)
vib.run()

vib_energies = vib.get_energies()
vib_freqs = vib.get_frequencies()

print("All vibrational frequencies (cm^-1):")
for i, freq in enumerate(vib_freqs):
    print(f"  Mode {i:2d}: {freq:.4f} cm^-1")

print("\nReal vibrational frequencies only (cm^-1):")
real_freqs = [f.real for f in vib_freqs if np.isreal(f) and f.real > 10]
for i, freq in enumerate(real_freqs):
    print(f"  Mode {i:2d}: {freq:.4f} cm^-1")

vib.clean()
