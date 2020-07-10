# Use Field Calculator with Start and End points of line

def NorthAzimuth(x1,y1,x2,y2):
  degBearing = math.degrees(math.atan2((x2 - x1),(y2 - y1)))
  if (degBearing < 0):
      degBearing += 360.0
  return degBearing



NorthAzimuth( !Start_X! , !Start_Y! , !End_X! , !End_Y! )