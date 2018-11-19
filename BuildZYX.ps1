$PathVariable = $env:path
$PathVariable = $PathVariable+";C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\amd64"
$PathVariable = $PathVariable+";C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\bin\"
$PathVariable = $PathVariable+";C:\Program Files (x86)\Microsoft Visual Studio\2017\Community\VC\Tools\MSVC\14.15.26726\bin\Hostx64\x64"

$Env:path= $PathVariable

cd d:\GitHub\mask-rcnn-pytorch\third_party\nms\src\cuda\

nvcc -c -o nms_kernel.cu.o nms_kernel.cu -x cu -Xcompiler -fPIC -arch=sm_35

cd ../../

#$PythonExe = 'C:\Users\zhou.yongxin\AppData\Local\conda\conda\envs\PyTorch\python.exe'
$PythonExe = 'e:\Anaconda3\envs\pytorch\python.exe'
&$PythonExe build.py