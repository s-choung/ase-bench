from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule('N2')
atoms.calc = EMT()

opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='n2_vib')
vib.run()

energies = vib.get_energies()
freqs_cm1 = [e / 0.0001239841984332003 for e in energies]

for i, f in enumerate(freqs_cm1, 1):
    print(f"Mode {i}: {f.real:.2f} cm^-1" + (" (imag)" if abs(f.imag) > 1e-8 else ""))

vib.clean()
