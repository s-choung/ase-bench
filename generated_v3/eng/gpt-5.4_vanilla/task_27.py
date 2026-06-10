from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nvtberendsen import NVTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase import units

atoms = bulk('Ag', 'fcc', a=4.09, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

T = 500.0
dt = 5.0 * units.fs
steps = 200

MaxwellBoltzmannDistribution(atoms, temperature_K=T)
Stationary(atoms)
ZeroRotation(atoms)

dyn = NVTBerendsen(atoms, timestep=dt, temperature_K=T, taut=100 * units.fs)

def report():
    print(f"step={dyn.nsteps:4d} T={atoms.get_temperature():8.2f} K")

report()
dyn.attach(report, interval=50)
dyn.run(steps)
