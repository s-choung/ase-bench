from ase import Atoms
from ase.md.nptberendsen import NPTBerendsen
from ase.calculators.emt import EMT
from ase.units import fs, bar

a = 3.6
cu = Atoms('Cu', positions=[[0, 0, 0]], cell=[[a, 0, 0], [0, a, 0], [0, 0, a]], pbc=True)
cu = cu * (3, 3, 3)
cu.calc = EMT()

print(cu.get_volume(), cu.get_stress()[-1] / bar)

dyn = NPTBerendsen(cu, timestep=5 * fs, temperature=300, pressure=1 * bar, taut=100 * fs, taup=1000 * fs)
dyn.run(200)

print(cu.get_volume(), cu.get_stress()[-1] / bar)
