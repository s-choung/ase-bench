from ase import units
from ase.build import bulk, make_supercell
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen

atoms = make_supercell(bulk('Cu'), 3 * [3, 3, 3])
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = NPTBerendsen(atoms, timestep=5 * units.fs,
                   temperature_K=300, taut=100 * units.fs,
                   pressure_arb=1.0, taup=1000 * units.fs)
print(f"Initial volume: {atoms.get_volume():.2f} Å³, Pressure: {atoms.get_pressure() / units.bar:.2f} bar")
dyn.run(200)
print(f"Final volume: {atoms.get_volume():.2f} Å³, Pressure: {atoms.get_pressure() / units.bar:.2f} bar")
