from ase.build import bulk, surface
from ase.calculators.emt import EMT

# Create Cu bulk and cut (2,1,1) surface with 3 layers
atoms = bulk('Cu', 'fcc', a=3.6)
slab = surface(atoms, (2, 1, 1), layers=3, vacuum=10.0)

# Attach a calculator (EMT is for metals, though Cu is not standard for EMT, 
# we use it as per instructions to fulfill the "use built-in" requirement)
slab.set_calculator(EMT())

print(f"Number of atoms: {len(slab)}")
print("Cell dimensions:")
print(slab.get_cell())
