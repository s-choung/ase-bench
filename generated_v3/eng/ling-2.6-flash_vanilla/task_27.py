from ase.build import bulk
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.NVTBussi import NVTBussi
from ase import units

atoms = bulk('Ag', 'fcc', a=4.09).repeat(2)
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

calc = EMT()
atoms.calc = calc
timestep = 5 * units.fs

thermostat = NVTBussi(atoms, timestep, temperature_K=300, taut=100 * units.fs)

for step in range(200):
    atoms.get_forces()
    thermostat.run(steps=1)
    if step % 50 == 0:
        T = atoms.get_temperature()
        print(f"Step {step}: T = {T:.1f} K")
