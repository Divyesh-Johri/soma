## SOMA: Solving Optical Marker-Based MoCap Automatically, ICCV'21

This repository contains the official PyTorch implementation of:

SOMA: Solving Optical Marker-Based MoCap Automatically\
Nima Ghorbani and Michael J. Black\
[Paper](https://download.is.tue.mpg.de/soma/SOMA_ICCV21.pdf) | [Supp.Mat.](https://download.is.tue.mpg.de/soma/SOMA_Suppmat.pdf) | [Video](https://www.youtube.com/watch?v=BEFCqIefLA8&t=1s&ab_channel=MichaelBlack) | [Project website](https://soma.is.tue.mpg.de/) | [Poster](https://download.is.tue.mpg.de/soma/SOMA_Poster.pdf)

![alt text](https://download.is.tue.mpg.de/soma/tutorials/soma_github_teaser.gif "mocap point clouds (black dots in the back) turned into labeled markers (colored dots)")

SOMA **automatically transforms raw marker-based mocap point clouds** (black dots in the back) into **solved SMPL-X bodies** and **labeled markers** (colored dots).

## Dependency Installation

SOMA is originally developed in Python 3.7, PyTorch 1.8.2 LTS, for Ubuntu 20.04.2 LTS. 
Below we prepare the python environment using [Anaconda](https://www.anaconda.com/products/individual), 
however, we opt for a simple pip package manager for installing dependencies.

````
sudo apt install libatlas-base-dev
sudo apt install libpython3.7
sudo apt install libtbb2
sudo apt install libfftw3
sudo apt install ffmpeg

conda create -n soma python=3.7 
conda install -c conda-forge ezc3d

pip3 install torch==1.8.2+cu102 torchvision==0.9.2+cu102 torchaudio==0.8.2 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html

````
ezc3d installation is currently not supported by pip.

Assuming that you have already cloned this repository to your local drive 
go to the root directory of SOMA code and run
````
pip install -r requirements.txt
python setup.py develop
````
Use [soma_env.txt](soma_env.txt) as reference if needed.

Install the psbody.mesh library in [https://github.com/Divyesh-Johri/mesh](https://github.com/Divyesh-Johri/mesh).
Hint: clone the mesh repository and run the following from the anaconda environment:  ````python setup.py install ````.

Copy the precompiled 
[smpl-fast-derivatives](https://download.is.tue.mpg.de/download.php?domain=soma&sfile=smpl-fast-derivatives.tar.bz2) 
into the installed Mesh library in your python site-packages folder, i.e. ````anaconda3/envs/soma/lib/python3.7/site-packages/psbody_mesh-0.4-py3.7-linux-x86_64.egg/psbody ````.

To use the rendering capabilities first install an instance of Blender-2.83 LTS on your machine.
Afterward uncompress the precompiled 
[bpy-2.83](https://download.is.tue.mpg.de/download.php?domain=soma&sfile=blender/bpy-2.83-20200908.tar.bz2) and place its contents (``` 2.83 ``` folder and ``` bpy.so ``` file) into your python site-packages folder, i.e. ````anaconda3/envs/soma/lib/python3.7/site-packages````.

Go to ```` anaconda3/envs/soma/lib/python3.7/site-packages/body_visualizer/tools/render_tools.py ````. At line 26, replace logger.sucess() with logger.success().

Last but not least, the current SOMA code relies on [MoSh++](https://github.com/Divyesh-Johri/moshpp) mocap solver. 
Please install MoSh++ following the guidelines in its repository.


## Using SOMA on TMM100
Follow directions in the [work directory setup file](src/soma_on_TMM100/setup/setup_work_dir.md). 

Then, run the following files to perform the following tasks:
- 

## Citation

Please cite the following paper if you use this code directly or indirectly in your research/projects:

```
@inproceedings{SOMA:ICCV:2021,
  title = {{SOMA}: Solving Optical Marker-Based MoCap Automatically},
  author = {Ghorbani, Nima and Black, Michael J.},
  booktitle = {Proceedings of IEEE/CVF International Conference on Computer Vision (ICCV)},
  month = oct,
  year = {2021},
  doi = {},
  month_numeric = {10}}
```

## License

Software Copyright License for **non-commercial scientific research purposes**. Please read carefully
the [terms and conditions](./LICENSE) and any accompanying documentation before you download and/or
use the SOMA data and software, (the "Data & Software"), software, scripts, and animations. 
By downloading and/or using the Data & Software (including downloading, cloning, installing, and any other use of this repository), 
you acknowledge that you have read these terms
and conditions, understand them, and agree to be bound by them. If you do not agree with these terms and conditions, you
must not download and/or use the Data & Software. 
Any infringement of the terms of this agreement will automatically terminate
your rights under this [License](./LICENSE).

## Contact

The code in this repository is developed by [Nima Ghorbani](https://nghorbani.github.io/) 
while at [Max-Planck Institute for Intelligent Systems, Tübingen, Germany](https://is.mpg.de/person/nghorbani).

If you have any questions you can contact us at [soma@tuebingen.mpg.de](mailto:amass@tuebingen.mpg.de).

For commercial licensing, contact [ps-licensing@tue.mpg.de](mailto:ps-licensing@tue.mpg.de)
