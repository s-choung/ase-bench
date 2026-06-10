from ase.build import bulk

si = bulk('Si', 'diamond', a=5.43)
si_super = si.repeat((3, 3, 3))

print(len(si_super))
print(si_super.get_volume())
