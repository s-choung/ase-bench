from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nvtberendsen import NVTBerendsen
from ase import units

atoms = bulk('Ag', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()

dyn = NVTBerendsen(atoms, timestep=5 * units.fs, temperature_K=500, taut=100 * units.fs)
dyn.set_temperature(temperature_K=500)

def log():
    print(f"step={dyn.nsteps:4d} T={atoms.get_temperature():.2f} K")

log()
dyn.attach(log, interval=50)
dyn.run(200)
