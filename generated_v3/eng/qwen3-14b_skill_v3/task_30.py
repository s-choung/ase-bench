from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.units import bar, fs

atoms = bulk('Cu', 'fcc', cubic=True).repeat((3, 3, 3))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

timestep = 5 * fs
taut = 100 * fs
taup = 1000 * fs
pressure = 1 * bar

md = NPTBerendsen(atoms, timestep=timestep, temperature_K=300, pressure=pressure, taut=taut, taup=taup)
md.run(200)

initial_vol = atoms.get_volume()
initial_pres = atoms.get_pressure()
final_vol = atoms.get_volume()
final_pres = atoms.get_pressure()

print(f"Initial Volume: {initial_vol:.2f} Å³")
print(f"Final Volume: {final_vol:.2f} Å³")
print(f"Initial Pressure: {initial_pres:.2f} eV/Å³")
print(f"Final Pressure: {final_pres:.2f} eV/Å³")
