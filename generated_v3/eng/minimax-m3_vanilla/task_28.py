from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

dt = 5 * units.fs
n_steps = 200
seg = 50
T0, T1 = 300, 600
n_segs = n_steps // seg

md = Langevin(atoms, dt, friction=0.01, temperature_K=T0)

for i in range(n_segs):
    T = T0 + (T1 - T0) * (i + 1) / n_segs
    md.set_temperature(T)
    md.run(seg)
    print(f"Step {(i+1)*seg}: T = {atoms.get_temperature():.2f} K (target = {T:.1f} K)")
