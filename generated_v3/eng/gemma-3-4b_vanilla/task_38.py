from ase.calculators.emt import EMT
from ase.calculators.lj import LJ
from ase.build import bulk
from ase.geom import Point
from ase.energy import Helmholtz
import numpy as np

cu = bulk('Cu', size=(4, 4, 4))
cu.calc = EMT()
cu.calc.kpts = (1, 1, 1)

lj_calc = LJ()
cu.calc = lj_calc

point = Point(np.array([0., 0., 0.]))
cu.set_cell(point.direction*cu.lattice)

freqs = cu.get_frequencies()
print("Vibrational Frequencies (cm^-1):", freqs[:, 0])

he_energy = Helmholtz(cu, T=300.0, zero_of_charge=True)
print("Helmholtz Free Energy (eV):", he_energy.value)
