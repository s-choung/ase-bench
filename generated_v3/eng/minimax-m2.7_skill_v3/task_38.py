from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.phonons import Phonons
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)

ph = Phonons(atoms, atoms.calc, delta=0.05)
ph.run()
ph.read()

vib_energies = ph.get_energies()
thermo = HarmonicThermo(vib_energies=vib_energies)
F = thermo.get_helmholtz_energy(temperature=300)
print(f"Helmholtz free energy at 300K: {F:.4f} eV")
