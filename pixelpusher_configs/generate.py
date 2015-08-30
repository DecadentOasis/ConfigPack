tree_template="""
strip1=ws2801
strip2=ws2801
strip3=ws2801
strip4=ws2801
strip5=ws2801
strip6=ws2801
strip7=ws2801
strip8=ws2801
swap=12345678
pixels=24
ws28delay=6
blank_strips_on_idle=1
data_watchdog_time=300
order1=rgb
order2=rgb
order3=rgb
order4=rgb
order5=rgb
order6=rgb
order7=rgb
order8=rgb
# strip colors, 1 through 8: red orange yellow green cyan blue purple white
start1=ff0000
start2=ff4000
start3=ff4000
start4=afaf00
start5=00ff00
start5=00afaf
start6=0000ff
start7=af00af
start8=808080
ether=192.168.111.%(ipaddr)s
netmask=255.255.255.0
gateway=192.168.111.1
"""

for i in range(1, 11):
    # IP addresses range from 192.168.111.101 to 192.168.111.110
    file("tree-pusher-%02d-pixel.rc" % (i, ), "w").write(tree_template % { "ipaddr": i+100 })

island_template="""
strip1=apa102
strip2=apa102
strip3=apa102
strip4=apa102
strip5=apa102
strip6=apa102
strip7=apa102
strip8=apa102
swap=12345678
pixels=160
order1=rgb
order2=rgb
order3=rgb
order4=rgb
order5=rgb
order6=rgb
order7=rgb
order8=rgb
# strip colors, 1 through 8: red orange yellow green cyan blue purple white
start1=ff0000
start2=ff4000
start3=ff4000
start4=afaf00
start5=00ff00
start5=00afaf
start6=0000ff
start7=af00af
start8=808080
blank_strips_on_idle=1
data_watchdog_time=300
ether=192.168.111.%(ipaddr)s
netmask=255.255.255.0
gateway=192.168.111.1
"""
for i in range(1, 4):
    # IP addresses range from 192.168.111.151 to 192.168.111.153
    file("island-pusher-%02d-pixel.rc" % (i, ), "w").write(island_template % { "ipaddr": i+150 })

palm_tree_art_car_template="""
strip1=apa102
strip2=apa102
strip3=apa102
strip4=apa102
strip5=apa102
strip6=apa102
strip7=apa102
strip8=apa102
#swap=12345678
pixels=48
order1=rgb
order2=rgb
order3=rgb
order4=rgb
order5=rgb
order6=rgb
order7=rgb
order8=rgb
# strip colors, 1 through 8: red orange yellow green cyan blue purple white
start1=ff0000
start2=ff4000
start3=ff4000
start4=afaf00
start5=00ff00
start5=00afaf
start6=0000ff
start7=af00af
start8=808080
blank_strips_on_idle=1
data_watchdog_time=300
ether=192.168.111.%(ipaddr)s
netmask=255.255.255.0
gateway=192.168.111.1
"""
for i in range(0, 8):
    # IP addresses range from 192.168.111.120 to 192.168.111.128
    file("palm-tree-pusher-%02d-pixel.rc" % (i, ), "w").write(palm_tree_art_car_template % { "ipaddr": i+120 })
