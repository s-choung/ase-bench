from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
ZeroRotation(atoms)

initial_volume = atoms.get_volume()
initial_stress = atoms.get_stress()
initial_pressure = -(initial_stress[0] + initial_stress[1] + initial_stress[2])/3

dyn = NPTBerendsen(atoms, 
                   timestep=5*units.fs, 
                   temperature_K=300, 
                   pressure=1.0*units.bar, 
                   taut=100*units.fs, 
                   taup=1000*units.fs)
dyn.run(200)

final_volume = atoms.get_volume()
final_stress = atoms.get_stress()
final_pressure = -(final_stress[0] + final_stress[1] + final_stress[2])/3

print(f'Initial Volume: {initial_volume:.3f} A³\nInitial Pressure: {initial_pressure:.3f} eV/A³')
print(f'Final Volume: {final_volume:.3f} A³\nFinal Pressure: {final_pressure:.3f} eV/A³')
