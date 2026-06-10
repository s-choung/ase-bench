from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

V0 = atoms.get_volume()

# Pressure conversion: 10 GPa → eV/Å³
P_GPa = 10
P_eVA3 = P_GPa * 1e9 * 1e-30 / units.eV * (units.m ** 3 / units.Angstrom ** 3)
# 1 GPa = 1e9 Pa; 1 Pa = 1 J/m³; 1 eV/Å³ = (1.60218e-19 J)/(1e-30 m³)
# Or, simpler: 1 GPa = 0.006241509126 eV/Å³ (ASE units)
P_eVA3 = P_GPa * 0.006241509126

dyn = NPTBerendsen(
    atoms,
    timestep=2 * units.fs,
    temperature_K=500,
    taut=100 * units.fs,
    pressure=P_eVA3,
    taup=1000 * units.fs,
    compressibility=1e-5  # 1/bar; default is fine for metals
)
print(f'Initial cell volume: {V0:.3f} Å³')
dyn.run(100)
V1 = atoms.get_volume()
print(f'Final cell volume: {V1:.3f} Å³')
