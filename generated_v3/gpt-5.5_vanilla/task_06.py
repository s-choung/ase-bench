from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation

atoms = bulk("Cu", "fcc", a=3.615, cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
ZeroRotation(atoms)

def report(label):
    epot = atoms.get_potential_energy()
    ekin = atoms.get_kinetic_energy()
    print(f"{label} T = {atoms.get_temperature():.2f} K")
    print(f"{label} E_pot = {epot:.6f} eV")
    print(f"{label} E_kin = {ekin:.6f} eV")
    print(f"{label} E_tot = {epot + ekin:.6f} eV")

report("Initial")

dyn = Langevin(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    friction=0.01 / units.fs,
)
dyn.run(100)

report("Final")
