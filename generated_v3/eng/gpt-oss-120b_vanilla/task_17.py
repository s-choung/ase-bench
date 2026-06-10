from ase.build import bulk, surface
from ase.calculators.emt import EMT

# bulk Cu
cu_bulk = bulk('Cu', 'fcc', a=3.6)

# (2,1,1) surface, 3 layers, 10 Å vacuum
cu_surf = surface(cu_bulk, (2, 1, 1), layers=3, vacuum=10.0)

# attach a simple calculator (optional)
cu_surf.calc = EMT()

print("Number of atoms:", len(cu_surf))
print("Cell dimensions ( Å ):\n", cu_surf.get_cell())
