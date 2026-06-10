from ase.build import molecule
from ase import units
from ase.calculators.emt import EMT
from ase.calculators.ideal import IdealGasThermo
from ase.geometry import Molecule
from ase.constraints import FixAtoms
import numpy as np

N = 2
natoms = N
geom = np.array([[0, 0, 0], [1, 0, 0]])
molecules = molecule('N2', N=N, geometry='linear', scale=1.0)
molecules.set_cell([2*units.Angstrom, 0, 0])

calc = EMT(lwave=False, lkpath='gr', lsigma=0.05)
molecules.calc = calc

freqs = calc.frequencies
print("Vibrational Frequencies:")
print(freqs)

constraints = FixAtoms(cells=[[0, 0, 0], [1, 0, 0]])
molecules.add_constraint(constraints)

ig = IdealGasThermo(T=298.15, P=1.0)
molecules.calc = ig

print("Gibbs Free Energy:")
print(ig.gibbs_energy)
