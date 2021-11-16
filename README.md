<p>
YOLOv5 🚀 is a family of object detection architectures and models pretrained on the COCO dataset, and represents <a href="https://ultralytics.com">Ultralytics</a>
 open-source research into future vision AI methods, incorporating lessons learned and best practices evolved over thousands of hours of research and development.
</p>

<!--
<a align="center" href="https://ultralytics.com/yolov5" target="_blank">
<img width="800" src="https://github.com/ultralytics/yolov5/releases/download/v1.0/banner-api.png"></a>
-->
</div>

## <div align="center">Document</div>

==Before doing every thing:==
```bash
mkdir ../png_DB
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

```python
python3 detect_2.py --weight runs/train/exp/weights/best.pt  --source test.mp4 --view-img  --conf-thres 0.4 --img-save
```
