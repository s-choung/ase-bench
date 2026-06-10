from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase import units

atoms = bulk('Pd', 'fcc') * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)

e_start = atoms.get_total_energy()

md = VelocityVerlet(atoms, 2 * units.fs)
md.run(200)

e_end = atoms.get_total_energy()
print(f"Total energy difference (E_end - E_start): {e_end - e_start:.6e} eV")
