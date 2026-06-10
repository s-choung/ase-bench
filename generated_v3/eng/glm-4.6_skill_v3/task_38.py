from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)

potential_energy = atoms.get_potential_energy()

vib = Vibrations(atoms)
vib.run()
vib_energies = vib.get_energies()
vib.clean()

thermo = HarmonicThermo(vib_energies=vib_energies, potentialenergy=potential_energy)
helmholtz_energy = thermo.get_helmholtz_energy(temperature=300.0)

print(f"Helmholtz free energy at 300 K: {helmholtz_energy:.4f} eV")
