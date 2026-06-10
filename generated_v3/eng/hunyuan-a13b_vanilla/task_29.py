from ase import Atoms
from ase.md.verlet import VelocityVerlet
from ase.calculator.emt import EMT

# Setup Pd FCC 2x2x2 supercell
rows = ['Pd 0.0 0.0 0.0']
for i, x in enumerate([-0.5, 0.5]):
    for j, y in enumerate([-0.5, 0.5]):
        for k, z in enumerate([-0.5, 0.5]):
            rows.append(f'Pd {x:.3f} {y:.3f} {z:.3f}')
otic = Atoms('\n'.join(rows), pbc=True, cell=[3.5, 3.5, 3.5], element='Pd')
