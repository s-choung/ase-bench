from ase.build import bulk, surface
s = surface(bulk('Fe', 'bcc', a=2.87), (1,1,0), layers=4, size=(2,2,4), vacuum=10)
print(len(s))
print(s.cell.lengths())
