import network
 
def connect():
  ssid = "ODVX"
  password = "v074av0x"
 
  station = network.WLAN(network.STA_IF)
 
  if station.isconnected() == True:
      print("Already connected")
      return
 
  station.active(True)
  station.connect(ssid, password)
 
  while station.isconnected() == False:
      pass
 
  print("Connection successful")
  ip = station.ifconfig()
  print(ip)
  return ip[0]

