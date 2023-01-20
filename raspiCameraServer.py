    from cscore import CameraServer
import cv2
import numpy as np
from networktables import NetworkTablesInstance

ntinst = NetworkTablesInstance.getDefault()
ntinst.startClientTeam(4903)
ntinst.startDSClient()
nt = ntinst.getTable('SmartDashboard');

cs = CameraServer()
CameraServer.enableLogging()

width, height = 160, 120;

cs.startAutomaticCapture().setResolution(width, height)

sink = cs.getVideo()

output = cs.putVideo("April Tags", width, height)

input_img = None

while True:
  time, input_img = sink.grabFrame(input_img)

  if time == 0: # There is an error
      output.notifyError(sink.getError())
      continue

  #
  # Insert processing code here
  #

  nt.putBoolean("outputting", True);

  output_img = input_img

  output.putFrame(output_img)
