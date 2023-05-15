{\rtf1\ansi\ansicpg1252\cocoartf2708
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fswiss\fcharset0 ArialMT;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0\c84706;\cssrgb\c100000\c100000\c100000;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import time\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 from rplidar import RPLidar\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 \'a0\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 \'a0\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 PORT_NAME = '/dev/ttyUSB0'\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 lidar = RPLidar(PORT_NAME)\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 distList = []\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 try:\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 for scan in lidar.iter_scans():\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 for (_,angle,distance) in scan:\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 #convert mm to feet\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 if (angle < 135 or angle > 115):\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 feet = distance/304.8\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 #if (feet < 13):\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 distList.append(feet)\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 avgDist = sum(distList) / len(distList)\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 print(avgDist, sep="\\n")\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 distList = []\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 time.sleep(0.05)\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 except KeyboardInterrupt:\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 print("stopping")\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 finally:\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 lidar.stop()\AppleTypeServices \'a0
\f1\fs24 \cb1 \

\f0\fs29\fsmilli14667 \AppleTypeServices\AppleTypeServicesF65539 \cb3 lidar.disconnect()\AppleTypeServices \'a0
\f1\fs24 \cb1 \
}