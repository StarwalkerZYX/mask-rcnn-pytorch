import os
import torch
from torch.utils.ffi import create_extension


sources = ['src/nms.c']
headers = ['src/nms.h']
defines = []
with_cuda = False

extra_objects = []
if torch.cuda.is_available():
    print('Including CUDA code.')
    sources += ['src/nms_cuda.c']
    headers += ['src/nms_cuda.h']
    defines += [('WITH_CUDA', None)]
    with_cuda = True
    extra_objects = ['src/cuda/nms_kernel.cu.o']

this_file = os.path.dirname(os.path.realpath(__file__))
print(this_file)
extra_objects = [os.path.join(this_file, fname) for fname in extra_objects]

extra_include_dirs = [
    '"C:/Program Files (x86)/Windows Kits/10/Include/10.0.10240.0/ucrt"',
    '"C:/Program Files (x86)/Windows Kits/10/Include/10.0.17134.0/shared"',
    '"C:/Program Files (x86)/Microsoft Visual Studio 14.0/VC/include"',
    r'"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.0\include"'
    #'"C:/Program Files (x86)/Microsoft Visual Studio/2017/Community/VC/Tools/MSVC/14.15.26726/include"',
]

ffi = create_extension(
    '_ext.nms',
    headers=headers,
    sources=sources,
    define_macros=defines,
    relative_to=__file__,
    with_cuda=with_cuda,
    extra_objects=extra_objects,
    include_dirs=extra_include_dirs,
)

if __name__ == '__main__':
    ffi.build()
