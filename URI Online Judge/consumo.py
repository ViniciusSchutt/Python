dist=int(input())
cons=float(input())

consform="{:.1f}".format(cons)
float_cons = float(consform)

media = float(dist/float_cons)

print('%0.3f'%media, 'km/l')




