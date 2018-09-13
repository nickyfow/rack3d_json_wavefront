import json
import sys

# import json from stdin
data = json.load(sys.stdin)

# export mtl data
for thing in data:
    id = thing['id']
    rgb_b = thing['rgb_b']/255
    rgb_g = thing['rgb_g']/255
    rgb_r = thing['rgb_r']/255
    print("newmtl {}".format(id))
    print("Ns 96.078431")
    print("Ka 1.000000 1.000000 1.000000")
    print("Kd {} {} {}".format(rgb_r, rgb_g, rgb_b))
    print("Ks 0.500000 0.500000 0.500000")
    print("Ke 0.000000 0.000000 0.000000")
    print("Ni 1.000000")
    print("d 1.000000")
    print("illum 2")
    print("")

