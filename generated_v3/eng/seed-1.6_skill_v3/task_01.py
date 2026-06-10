from ase.build import bulk

cu_bulk = bulk('Cu', 'fcc', a=3.6)
cu_super = cu_bulk.repeat((2,2,2))
print("Cell params (a,b,c,α,β,γ):", cu_super.get_cell_lengths_and_angles())
print("Number of atoms:", len(cu_super))
