from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Ag', 'fcc', a=4.09) * (2, 2, 2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

dyn = Bussi(atoms, timestep=5 * units.fs, temperature_K=500)

step_counter = [0]

def print_temp(atoms):
    step_counter[0] += 1
    if step_counter[0] % 50 == 0:
        T = atoms.get_temperature()
        print(f"Step {step_counter[0]}: T = {T:.1f} K")

dyn.run(200, observers=[print_temp])
