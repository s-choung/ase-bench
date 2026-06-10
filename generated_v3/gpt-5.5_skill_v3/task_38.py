import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk("Cu", "fcc", a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

BFGS(FrechetCellFilter(atoms), logfile=None).run(fmax=0.01)

vib = Vibrations(atoms, name="cu_bulk_vib")
vib.run()

freqs = vib.get_frequencies()
vib_energies = np.real(vib.get_energies())
vib_energies = vib_energies[vib_energies > 1e-5]

thermo = HarmonicThermo(vib_energies=vib_energies, potentialenergy=atoms.get_potential_energy())
F = thermo.get_helmholtz_energy(temperature=300.0, verbose=False)

print("F_helmholtz_300K_eV =", F)

vib.clean()
