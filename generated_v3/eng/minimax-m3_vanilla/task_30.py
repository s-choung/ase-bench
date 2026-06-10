from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

atoms = bulk('Cu', 'fcc') * (3, 3, 3)
atoms.calc = EMT()

def P(a):
    return -a.get_stress()[:3].mean() / units.bar

V0, P0 = atoms.cell.volume, P(atoms)

MaxwellBoltzmannDistribution(atoms, temperature_K=300)

md = NPTBerendsen(atoms, timestep=5 * units.fs, temperature_K=300,
                  pressure_au=1 * units.bar,
                  taut=100 * units.fs, taup=1000 * units.fs)
md.run(200)

print(f"Initial: V={V0:.3f} A^3, P={P0:.3f} bar")
print(f"Final:   V={atoms.cell.volume:.3f} A^3, P={P(atoms):.3f} bar")
