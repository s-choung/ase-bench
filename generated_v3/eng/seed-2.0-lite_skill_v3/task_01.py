from ase.build import bulk

# Create primitive cubic Cu FCC bulk with standard experimental lattice constant
cu_bulk = bulk('Cu', 'fcc', a=3.615, cubic=True)
# Generate 2x2x2 supercell
cu_supercell = cu_bulk.repeat((2, 2, 2))

# Output required system information
print(f"Total number of atoms in 2x2x2 supercell: {len(cu_supercell)}")
cell_lat_ang = cu_supercell.get_cell_lengths_and_angles()
print(f"Supercell lattice parameters (a,b,c [Å], α,β,γ [°]): {cell_lat_ang.round(2)}")
print(f"Full 3x3 supercell cell matrix:\n{cu_supercell.get_cell().round(2)}")
