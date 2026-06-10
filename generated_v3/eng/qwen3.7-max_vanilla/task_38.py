from ase.build import bulk
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', cubic=True)
atoms.calc = EMT()

vib = Vibrations(atoms)
vib.run()

thermo = HarmonicThermo(vib.get_energies(), potentialenergy=atoms.get_potential_energy())
F = thermo.get_helmholtz_energy(temperature=300.0)

print(f"Helmholtz free energy at 300K: {F:.4f} eV")
