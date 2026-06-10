from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nvtbussi import NVTBussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Ag').repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)

dyn = NVTBussi(atoms, timestep=5.0 * units.fs, temperature_K=500, taut=100 * units.fs)

dyn.attach(lambda: print(f"Step {dyn.get_number_of_steps():4d}, Temperature: {atoms.get_temperature():.2f} K"), interval=50)

dyn.run(200)
