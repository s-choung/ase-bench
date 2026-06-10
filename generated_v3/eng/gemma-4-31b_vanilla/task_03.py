from ase import Atoms
from ase.build import make_supercell
from ase.calculators.emt import EMT

# MoS2 monolayer structure
# Mo at (0,0,0), S at (0.33, 0, 1.5) and (-0.33, 0, -1.5) relative to Mo
atoms = Atoms('MoS2',
              positions=[(0, 0, 0), (0.33, 0, 1.5), (-0.33, 0, -1.5)],
              cell=[3.16, 3.16, 10.0], 
              pbc=[True, True, True])

# Adjust cell to ensure 10A vacuum (total height = layer thickness + 10)
# MoS2 thickness is roughly 3.1A; setting z to 13.1 for 10A gap
atoms.set_cell([3.16, 3.16, 13.1])

atoms.calc = EMT()
print(f"Cell size: {atoms.get_cell()}")
