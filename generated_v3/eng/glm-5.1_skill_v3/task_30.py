from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc').repeat((3, 3, 3))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

vol_i = atoms.get_volume()
pres_i = -atoms.get_stress()[:3].sum() / 3 / units.bar
print(f"Initial Volume: {vol_i:.2f} Å^3, Pressure: {pres_i:.2f} bar")

md = NPTBerendsen(atoms, 5 * units.fs, temperature_K=300,
                  pressure_au=1 * units.bar, taut=100 * units.fs,
                  taup=1000 * units.fs, compressibility_au=1.14)
md.run(200)

vol_f = atoms.get_volume()
pres_f = -atoms.get_stress()[:3].sum() / 3 / units.bar
print(f"Final Volume: {vol_f:.2f} Å^3, Pressure: {pres_f:.2f} bar")
