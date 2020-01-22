pip install pascal-voc-writer

Follow all instructions in https://pjreddie.com/darknet/yolo/

Once your darknet is setup:
```
./darknet detector train cfg/fa.data  cfg/yolov3-fa.cfg darknet53.conv.74
```

./darknet detector test cfg/fa.data cfg/yolov3-fa.cfg backup/yolov3-fa_final.weights ./test1.jpg
