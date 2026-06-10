from ase.build import bulk, surface

# Create bulk Cu
cu = bulk('Cu', 'fcc', a=3.61)

# Cut (2,1,1) surface with 3 layers and 10 Å vacuum
slab = surface(cu, (2, 1, 1), layers=3, vacuum=10.0)

print("Number of atoms:", len(slab))
print("Cell:")
print(slab.cell)
