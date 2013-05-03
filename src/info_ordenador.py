import os, platform

def CPUinfo():
  # infofile on Linux machines:
  infofile = '/proc/cpuinfo'
  cpuinfo = {}

  if os.path.isfile(infofile):
    f = open(infofile, 'r')
    for line in f:
      try:
	name, value = [w.strip() for w in line.split(':')]
      except:
	continue
      if name == 'model name':
	cpuinfo['CPU type'] = value
      elif name == 'cache size':
	cpuinfo['cache size'] = value
      elif name == 'cpu MHz':
	cpuinfo['CPU speed'] = value + ' Hz'
      elif name == 'vendor_id':
	cpuinfo['vendor ID'] = value
    f.close()
  return cpuinfo

def SOinfo():
  SOinfo=[platform.uname(), platform.platform()]
  return SOinfo

def InterpretePYinfo():
  InterpretePython_info=[platform.python_version(), platform.python_build()]
  return InterpretePython_info
  
if __name__ == '__main__':
  print CPUinfo()
  print SOinfo()
  print InterpretePYinfo()