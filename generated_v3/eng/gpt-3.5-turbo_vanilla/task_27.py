from ase import Atoms
from ase.calculators.emt import EMT
from ase.md import MDAnalysis
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.io import write
from ase.constraints import FixInternals

atoms = Atoms('Ag4',
              scaled_positions=[(0, 0, 0), (0.5, 0.5, 0), (0.5, 0, 0.5), (0, 0.5, 0.5)],
              cell=[2, 2, 2],
              pbc=True)

atoms.set_calculator(EMT())
MaxwellBoltzmannDistribution(atoms, 500)
atoms.set_constraint(FixInternals(atoms))
dyn = MDAnalysis(atoms, 5 * 500, 300)
dyn.set_timestepping(200)
for i in range(200):
    dyn.run(50)
    print(f'Step {i*50}, Temp: {atoms.get_temperature()} K')
