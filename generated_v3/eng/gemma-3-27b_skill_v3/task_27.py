from ase import Atoms
from ase.build import bulk, make_supercell
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
import ase.units as units

atoms = bulk('Ag', 'fcc', a=4.07)
atoms = make_supercell(atoms, (2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

bussi = Bussi(atoms, timestep=5 * units.fs, temperature_K=500, friction=0.01 / units.fs)

for step in range(200):
    bussi.step()
    if (step + 1) % 50 == 0:
        temperature = atoms.get_temperature()
        print(f"Step {step + 1}: Temperature = {temperature:.2f} K")
