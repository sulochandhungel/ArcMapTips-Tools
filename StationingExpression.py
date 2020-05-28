def FindLabel ( esri__measure ):
 EM = str(int(round(esri__measure)))
 if len(EM) == 0:
  return "0+00"
 elif len(EM) == 1:
  return "0+0{0}".format(*EM)
 elif len(EM) == 2:
  return "0+{0}{1}".format(*EM)
 elif len(EM) == 3:
  return "{0}+{1}{2}".format(*EM)
 elif len(EM) == 4:
  return "{0}{1}+{2}{3}".format(*EM)
 elif len(EM) == 5:
  return "{0}{1}{2}+{3}{4}".format(*EM)
 elif len(EM) == 6:
  return "{0}{1}{2}{3}+{4}{5}".format(*EM)
