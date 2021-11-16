<p>
About YOLOv5:<br>
YOLOv5 🚀 is a family of object detection architectures and models pretrained on the COCO dataset, and represents <a href="https://ultralytics.com">Ultralytics</a>
 open-source research into future vision AI methods, incorporating lessons learned and best practices evolved over thousands of hours of research and development.
</p>

<!--
<a align="center" href="https://ultralytics.com/yolov5" target="_blank">
<img width="800" src="https://github.com/ultralytics/yolov5/releases/download/v1.0/banner-api.png"></a>
-->
</div>

## <div align="center">Document &#129712;蝇  </div>

==Before doing every thing:==
```bash
mkdir ../png_DB csv
mkdir ../png_DB/png
```
<pre>
├── png_DB
│   └── png
└── yolov5
    ├── csv
    ├── data
    ├── mask
    ├── models
    ├── other_tools
    ├── runs
    └── utils

</pre>

See the [YOLOv5 Docs](https://docs.ultralytics.com) for full documentation on training, testing and deployment.

---

Thanks for Yolov5, the words below is the torturous of this repository

some scripts:

Detect_2.py
A customized script for specific output.

Quick start:


:fly:
:mosquito:
:microbe:

```python
mkdir csv ../png_DB
mkdir ../png_DB/png

python3 detect_2.py --weight runs/train/exp/weights/best.pt  --source test.mp4 --view-img  --conf-thres 0.4 --chain-det
python3 path_ink.py -i test.mp4
```

To do work


Training:
  - [x] 5 k training set
  - [ ] 10k training set
  - [ ] 20k training set
  - [ ] 50k training set
  - [ ] 100k training set

Features:
  - [X] path ink
  - [X] save images and annotations
  - [X] Flies detection
  - [X] Flies head detection
  - [X] Chasing Behaviors
    - [ ] Chasing duration
  - [ ] Chains
    - [X] Chain by radium
    - [ ] Chasing correction
    - [ ] Chasing duration
  - [ ] Mating
  - [ ] Tracking
    - [ ] Tracking by latest dots
    - [ ] Tracking correction
    - [ ] Tracking Tracking
    - [ ] Movement statistics
