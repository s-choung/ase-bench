from ase.build import bulk

hcp_ti = bulk('Ti', 'hcp', a=2.95, c=1.59*2.95)
print("Cell vectors:", hcp_ti.cell[:])
print("Atomic positions:", hcp_ti.get_positions())
