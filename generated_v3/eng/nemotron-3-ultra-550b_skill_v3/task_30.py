from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms = atoms * (3, 3, 3)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

vol0 = atoms.get_volume()
press0 = atoms.get_stress(voigt=False).trace() / 3.0 / units.bar
print(f"Initial volume: {vol0:.2f} Å^3, Pressure: {press0:.2f} bar")

dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    pressure_au=1.0 * units.bar,
    taut=100 * units.fs,
    taup=1000 * units.fs,
)
dyn.run(200)

vol1 = atoms.get_volume()
press1 = atoms.get_stress(voigt=False).trace() / 3.0 / units.bar
print(f"Final volume: {vol1:.2f} Å^3, Pressure: {press1:.2f} bar")
