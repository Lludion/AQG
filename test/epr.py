from obj import *

a = [1,2,3,4]
g = [[1],[2],[3],[4]]

ide = lambda x: x
h = lambda x : (x+1)%2 	# will be improved later
cnot = lambda x : x 	# will be improved later

s = [ide,h,cnot,ide] # later

skel = Skeleton(a,g,s,{0,1},2)

stat = State([[2],[3],[4],[]],d=([[0,0],[],[],[]],[[],[],[],[]]),s=skel)
conf = Config(stat)
aqc = AQC(skel,conf)

print(aqc)
