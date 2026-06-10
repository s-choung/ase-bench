from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.6); atoms.calc = EMT()
BFGS(atoms).run(fmax=0.01)

vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()
energies = units.Hz * freqs * units._hbar  # Convert cm-1 to eV
vib.clean()

thermo = HarmonicThermo(vib_energies=energies)
A = thermo.get_helmholtz_energy(temperature=300)
print(f"Helmholtz free energy: {A:.4f} eV")
