#Build NMS

 使用PowerShell
```
$PathVariable = $env:path
$PathVariable = $PathVariable+";C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\amd64"
$PathVariable = $PathVariable+";C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\bin\"
$Env:path= $PathVariable

cd d:\GitHub\mask-rcnn-pytorch\third_party\nms\src\cuda\

nvcc -c -o nms_kernel.cu.o nms_kernel.cu -x cu -Xcompiler -fPIC -arch=sm_35

cd ../../

$PythonExe = 'C:\Users\zhou.yongxin\AppData\Local\conda\conda\envs\PyTorch\python.exe'
&$PythonExe build.py

cd ../
```

 cd roialign/roi_align/src/cuda/
 nvcc -c -o crop_and_resize_kernel.cu.o crop_and_resize_kernel.cu -x cu -Xcompiler -fPIC -arch=sm_35
 cd ../../
 python build.py
 cd ../../