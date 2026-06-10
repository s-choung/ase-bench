from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

atoms = molecule("H2O")
atoms.calc = EMT()

BFGS(atoms, logfile=None).run(fmax=0.01)

vib = Vibrations(atoms, name="h2o_vib")
vib.run()

freqs = vib.get_frequencies()
energies = vib.get_energies()

def fmt(x):
    return f"{x.real:.6f}" if abs(x.imag) < 1e-8 else f"{x.imag:.6f}i"

print("Mode   Frequency (cm^-1)   Energy (eV)")
for i, (f, e) in enumerate(zip(freqs, energies), 1):
    print(f"{i:4d}   {fmt(f):>17s}   {fmt(e):>11s}")

vib.clean()
