from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]])
atoms.calc = EMT()

opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.001)

vib = Vibrations(atoms)
vib.run()

print("N2 vibrational frequencies:")
vib.summary()

freqs = vib.get_frequencies()
print("\nFrequency values (cm^-1):")
for i, f in enumerate(freqs):
    print(f"  Mode {i}: {f:.4f} cm^-1")
