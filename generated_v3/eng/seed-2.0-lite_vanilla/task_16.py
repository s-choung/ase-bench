from ase.build import bulk, surface

# Generate Fe BCC (110) slab with specified dimensions
fe_bulk = bulk('Fe', 'bcc')
slab = surface(fe_bulk, (1,1,0), layers=4, size=(2,2,1), vacuum=10.0)

# Print required system properties
print(f"Total number of atoms: {len(slab)}")
cell_params = slab.cell.cellpar()
print(f"Cell dimensions (Å) [a, b, c]: {cell_params[0]:.3f}, {cell_params[1]:.3f}, {cell_params[2]:.3f}")
