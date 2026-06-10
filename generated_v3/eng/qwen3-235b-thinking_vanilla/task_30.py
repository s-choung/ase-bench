from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.nptberendsen import NPTBerendsen

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, 300)

def get_pressure_bar(atoms):
    s = atoms.get_stress()
    return -(s[0] + s[1] + s[2]) / 3 * (units.eV / units.Ang**3) / units.bar

v0 = atoms.get_volume()
p0 = get_pressure_bar(atoms)
print(f"Initial volume: {v0:.2f} Å³, pressure: {p0:.2f} bar")

dyn = NPTBerendsen(atoms, 5*units.fs, 300, 1.0, 100*units.fs, 1000*units.fs)
dyn.run(200)

v1 = atoms.get_volume()
p1 = get_pressure_bar(atoms)
print(f"Final volume: {v1:.2f} Å³, pressure: {p1:.2f} bar")
