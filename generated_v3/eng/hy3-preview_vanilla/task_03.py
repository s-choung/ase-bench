from ase.build import mx2

# Create MoS2 monolayer with 10 Å vacuum
mos2 = mx2(formula='MoS2', kind='2H', a=3.18, thickness=3.19, size=(1,1,1), vacuum=10)

print("Cell size (Å):")
print(mos2.cell)
