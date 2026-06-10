from ase.build import bulk
from ase.calculators.emt import EMT
from ase.geometry import get_distances
import numpy as np

cu = bulk('Cu', 'fcc', a=3.6).repeat((2,2,2))
d = get_distances(cu.get_positions(), [cu[0].position], cell=cu.cell, pbc=True)[:,0]
print(f"Min: {np.min(d):.3f} Å", f"Max: {np.max(d):.3f} Å")
