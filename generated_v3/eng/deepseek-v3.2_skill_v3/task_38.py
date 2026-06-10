from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

vib = Vibrations(atoms, name='cu_vib', delta=0.01)
vib.run()
vib_energies = vib.get_energies()
vib.clean()

thermo = HarmonicThermo(vib_energies=vib_energies)
F = thermo.get_helmholtz_energy(temperature=300)

print(f"Vibrational frequencies (cm⁻¹): {vib.get_frequencies()}")
print(f"Helmholtz free energy at 300K: {F:.6f} eV")
