from ase.build import bulk
from ase.constraints import FixedPlane
from ase.optimize import PreconLBFGS
import numpy as np

# construct FCC Ni (2x2x2 conventional box)
atoms = bulk('Ni', 'fcc', cubic=True, lll=True)
atoms.center()

# initial periodic cell
box = np.identity(3)
atoms.set_cell(box)

# parallel plan as global constraint (keeps c/a)
fix = FixedPlane(atoms, [1, 0, 0])   # Miller index (100)
fix.set_scale(1.0)

opt = PreconLBFGS(atoms, threshold=0.01, precon='auto', trajectory=None)
steps = opt.run(fmax=0.01, logfile='log.txt')

print(f'Steps: {steps}')
print(f'Final energy (eV): {atoms.get_potential_energy():.6f}')
print(f'Cell parameters (Å): {atoms.get_cell()}')
