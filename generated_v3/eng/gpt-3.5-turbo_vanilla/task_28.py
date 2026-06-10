from ase import Atoms
from ase.calculators.emt import EMT
from ase.md import Langevin

# Create Cu FCC 2x2x2 supercell
cell = [[0, 4.05, 4.05], [4.05, 0, 4.05], [4.05, 4.05, 0]]
atoms = Atoms('Cu8', scaled_positions=[(0, 0, 0), (0, 0.5, 0.5),
                                      (0.5, 0, 0.5), (0.5, 0.5, 0),
                                      (0.25, 0.25, 0.25), (0.25, 0.75, 0.75),
                                      (0.75, 0.25, 0.75), (0.75, 0.75, 0.25)],
              cell=cell, pbc=True)
atoms.set_calculator(EMT())

# Initialize Langevin dynamics
dyn = Langevin(atoms, timestep=5.0 * 1e-15, temperature=300.0, friction=0.002)

# Temperature ramp from 300K to 600K
for i in range(200):
    if i % 50 == 0:
        print(f'Step {i}: Current temperature = {dyn.get_temperature()} K')
    dyn.run(1)
    dyn.set_temperature((300 + i * 300 / 200))
