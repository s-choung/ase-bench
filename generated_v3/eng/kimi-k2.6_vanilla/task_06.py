from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Cu', 'fcc', cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, 300 * units.kB)

def report(label):
    print(f"{label}: T={atoms.get_temperature():.2f} K, E={atoms.get_total_energy():.6f} eV")

report("Initial")
Langevin(atoms, 5 * units.fs, 300 * units.kB, friction=0.01).run(100)
report("Final")
