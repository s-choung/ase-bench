from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True).repeat(2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)

def get_state():
    e_tot = atoms.get_potential_energy() + atoms.get_kinetic_energy()
    return e_tot, atoms.get_temperature()

e_i, t_i = get_state()
print(f"Initial: T = {t_i:.2f} K, E = {e_i:.4f} eV")

dyn = Langevin(atoms, timestep=5*units.fs, temperature_K=300, friction=0.01)
dyn.run(100)

e_f, t_f = get_state()
print(f"Final:   T = {t_f:.2f} K, E = {e_f:.4f} eV")
