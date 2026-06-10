from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.thermodynamics import HarmonicThermo
import numpy as np

atoms = fcc111('Cu', size=3)
calc = EMT()
atoms.calc = calc

thermo = HarmonicThermo(atoms, calc.get_supercell(2, 2, 2))
thermo.run(300)

free_energy = thermo.results['Gibbs']
print(free_energy / 96485.33)
