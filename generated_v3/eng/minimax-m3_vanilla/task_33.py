from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = Atoms('CH4', positions=[
    (0.0000, 0.0000, 0.0000),
    (0.6276, 0.6276, 0.6276),
    (-0.6276, -0.6276, 0.6276),
    (-0.6276, 0.6276, -0.6276),
    (0.6276, -0.6276, -0.6276),
])
atoms.calc = EMT()
BFGS(atoms).run(fmax=0.001)

vib = Vibrations(atoms)
vib.run()
vib.summary()

frequencies = vib.get_frequencies()
print("\nReal vibrational frequencies (cm^-1):")
for f in frequencies:
    if isinstance(f, complex):
        if abs(f.imag) < 1e-6 and f.real > 0:
            print(f"{f.real:.2f}")
    elif f > 0:
        print(f"{f:.2f}")
