from ase.build import bulk
from ase.md.npt import NPTBerendsen
from ase.calculators.emt import EMT

atoms = bulk('Al', 'fcc', a=4.05, cubic=True).repeat((2,2,2))
atoms.set_calculator(EMT())
initial = atoms.get_volume()
pressure = 10 * 1e9 / 1.60218e11
npt = NPTBerendsen(atoms, temperature=500, pressure=pressure, tstep=1.0)
npt.run(100)
final = atoms.get_volume()
print(f'Initial volume: {initial:.4f} A^3')
print(f'Final volume: {final:.4f} A^3')
