from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', cubic=True)
atoms.calc = EMT()

vib = Vibrations(atoms)
vib.run()

# Filter out acoustic (near-zero) and imaginary (negative) modes
vib_energies = [e for e in vib.get_energies() if e > 1e-4]

thermo = HarmonicThermo(vib_energies=vib_energies)
F = thermo.get_helmholtz_energy(temperature=300)

print(f"{F:.6f} eV")
