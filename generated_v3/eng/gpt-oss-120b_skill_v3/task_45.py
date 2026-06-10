from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixBondLength
from ase.geometry import get_distances

# --- H2 initial -------------------------------------------------
h2 = molecule('H2')
h2.calc = EMT()
d0 = get_distances(h2.positions, h2.positions, h2.get_pbc(), h2.get_cell())[1][0, 1]
e0 = h2.get_potential_energy()
print(f'Initial   bond length = {d0:.3f} Å, energy = {e0:.6f} eV')

# --- set target bond length (0.9 Å) -------------------------------
h2.set_positions([[0, 0, 0], [0, 0, 0.9]])   # Å
h2.set_constraint(FixBondLength(0, 1))

# Re‑evaluate energy (constraint does not affect single‑point calc)
e1 = h2.get_potential_energy()
d1 = get_distances(h2.positions, h2.positions, h2.get_pbc(), h2.get_cell())[1][0, 1]
print(f'Constrained bond length = {d1:.3f} Å, energy = {e1:.6f} eV')
