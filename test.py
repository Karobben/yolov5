#!/usr/bin/env python3

from utils import Chain_detect
import pandas as pd
import math

File = "/mnt/8A26661926660713/Github/yolov5/csv/20210712-C0147-WASH_backgroud-5th-29C_6d_Trim.mp4.csv"
"csv/20210712-C0147-WASH_backgroud-5th-29C_6d_Trim.mp4.csv"
TB = pd.read_csv(File, sep=" ", header = None)
#TB = TB[TB[0]==2410]
for frame in range(2400,2412):
    tmp = TB[TB[0]==frame]
    AA = Chain_detect.Chain_finder(tmp)
    print(frame)
    print(AA.Chain_result)
