from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

opt = BFGS(atoms, logfile=None)
opt.run(fmax=0.001)

vib = Vibrations(atoms)
vib.run()

vib_energies = vib.get_energies()

real_vib_energies = vib_energies[vib_energies.imag == 0].real
real_vib_energies = real_vib_energies[real_vib_energies > 0]

print(f"Number of real positive vibrational modes: {len(real_vib_energies)}")
print(f"Vibrational energies (eV): {real_vib_energies}")

thermo = HarmonicThermo(vib_energies=real_vib_energies)

T = 300.0
F = thermo.get_helmholtz_energy(temperature=T, verbose=True)

print(f"\nHelmholtz free energy at {T} K: {F:.6f} eV")

vib.clean()
