from ase.build import bulk, surface

b = bulk('Fe', 'bcc', a=2.87)
s = surface(b, (1, 1, 0), layers=4, vacuum=10)
s = s.repeat((2, 2, 1))
print(len(s))
print(s.cell)
