import sys
import platform

info = 'OS info is \n{} \n\nPython version is {} {}'.format(
    platform.uname(), sys.version, platform.architecture())
print(info)
info.isalpha()

with open('os_info.txt', 'w') as ff:
    ff.write(info)



print('Dimon')

a = 12