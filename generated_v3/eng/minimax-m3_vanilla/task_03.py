from ase.build import mx2

# Create MoS2 monolayer
atoms = mx2(formula='MoS2', a=3.18, thickness=3.19, size=(1,1,1))

# Add 10 Angstroms of vacuum along the c-axis
atoms.center(axis=2, vacuum=10)

# Print cell size (a, b, c, alpha, beta, gamma)
print("Cell parameters:", atoms.cell.cellpar())
