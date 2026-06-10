from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.nvtberendsen import NVTBerendsen
from ase.md.nvtbussi import NVTBussi
from ase import units

atoms = bulk('Ag', 'fcc', a=4.09).repeat((2,2,2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, 500 * units.kB)

dyn = NVTBussi(atoms, timestep=5*units.fs, temperature_K=500)

def print_temp(a=atoms):
    print(f"Step: {dyn.nsteps}, T = {a.get_temperature():.2f} K")

for step in range(1, 201):
    dyn.run(1)
    if step % 50 == 0:
        print_temp()
