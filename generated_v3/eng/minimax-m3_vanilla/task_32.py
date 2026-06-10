from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# H2O molecule
atoms = Atoms('H2O', positions=[[0, 0, 0], [0.96, 0, 0], [-0.24, 0.93, 0]])
atoms.calc = EMT()

# Optimize geometry
BFGS(atoms).run(fmax=0.001)

# Vibrational analysis
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()   # cm^-1
energies = vib.get_energies()   # eV

print("Vibrational modes of H2O (EMT):")
print(f"{'Mode':<6}{'Freq (cm^-1)':<18}{'Energy (eV)':<15}")
for i, (f, e) in enumerate(zip(freqs, energies)):
    if f.imag != 0:
        label = f"{f.imag:.2f}i"
    else:
        label = f"{f.real:.2f}"
    print(f"{i+1:<6}{label:<18}{e.real:.6f}")

vib.clean()
