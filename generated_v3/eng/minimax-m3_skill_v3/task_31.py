from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)
atoms.calc = EMT()

V0 = atoms.get_volume()
print(f"Initial cell volume: {V0:.4f} Ang^3")

pressure_GPa = 10.0
pressure_eV_A3 = pressure_GPa * units.GPa
print(f"Target pressure: {pressure_eV_A3:.6f} eV/Ang^3 ({pressure_GPa} GPa)")

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

dyn = NPTBerendsen(atoms, timestep=1.0 * units.fs, temperature_K=500,
                   pressure_au=pressure_eV_A3,
                   taut=0.5 * units.fs, taup=1.0 * units.fs)
dyn.run(100)

V1 = atoms.get_volume()
print(f"Final cell volume:   {V1:.4f} Ang^3")
