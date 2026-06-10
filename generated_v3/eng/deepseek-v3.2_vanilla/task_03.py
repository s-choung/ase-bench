from ase.build import mx2

atoms = mx2(formula='MoS2', kind='2H', a=3.184, thickness=3.127, size=(1,1,1), vacuum=10)
print(f"Cell size: {atoms.cell.cellpar()}")
