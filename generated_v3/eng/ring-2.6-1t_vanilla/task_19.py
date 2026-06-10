from ase import Atoms
from ase.calculators.emt import EMT   # built‑in EMT calculator

# CO₂: C at origin, O atoms at ±1.16 Å along the x‑axis
co2 = Atoms('OCO',
            positions=[(-1.16, 0, 0), (0, 0, 0), (1.16, 0, 0)],
            cell=[10, 10, 10],
            pbc=False)

co2.calc = EMT()                     # attach a calculator (not needed for distances)

# distances from the central C (index 1) to the two O atoms (indices 0 and 2)
dists = co2.get_distances(1, [0, 2], mic=False)
print('C–O distances (Å):', dists)
