from ase.build import fcc
from ase.calculators.emt import EMT
from ase.md.npt import NPTBerendsen
from ase import units

atoms = fcc('Al', size=2)
calc = EMT()
atoms.calc = calc

p = 10 * units.GPa
T = 500 * units.K
n_steps = 100

dyn = NPTBerendsen(atoms, p, T, 0.001)
dyn.run(n_steps)

V0 = atoms.get_volume()
Vf = atoms.get_volume()

print(f"Initial volume: {V0:.3f} Ang^3")
print(f"Final volume: {Vf:.3f} Ang^3")
