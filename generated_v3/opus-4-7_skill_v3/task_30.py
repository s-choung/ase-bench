from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

print(f"Initial volume: {atoms.get_volume():.4f} Å³")
print(f"Initial pressure: {-atoms.get_stress(voigt=False).trace()/3 / units.bar:.4f} bar")

dyn = NPTBerendsen(atoms, timestep=5*units.fs, temperature_K=300,
                   pressure_au=1.0*units.bar, taut=100*units.fs, taup=1000*units.fs,
                   compressibility_au=4.57e-5/units.bar)
dyn.run(200)

print(f"Final volume: {atoms.get_volume():.4f} Å³")
print(f"Final pressure: {-atoms.get_stress(voigt=False).trace()/3 / units.bar:.4f} bar")
print(f"Final temperature: {atoms.get_temperature():.2f} K")
