> Did you stop after `cmake`? That's just the configuration step (like qmake), then you actually need to **build**, see the installation instructions.

## Installing Gudhi

@mglisse, when I run

```
cd ~/gudhi/
mkdir build
cd build/
cmake -DPython_ADDITIONAL_VERSIONS=3 -DCMAKE_BUILD_TYPE=Release -DQGLVIEWER_INCLUDE_DIR=/usr/local/lib/QGLViewer.framework/Headers -DWITH_GUDHI_EXAMPLE=ON ..
make
```

[Output for `cmake`](#https://github.com/ChemGuy88/oda/blob/master/gudhiTroubleshooting/Output_Gudhi_cmake.txt)
[Output for `make`](#https://github.com/ChemGuy88/oda/blob/master/gudhiTroubleshooting/Output_Gudhi_make.txt)

## Installing Gudhi Python Package

@VincentRouvreau

### Compiling

asdf

### Via Miniconda

I have installed Gudhi via Conda, and I see the python package installed at /usr/local/Caskroom/miniconda/base/pkgs/gudhi-3.1.1-py37he63e17b_1, but in IPython3 when I type "gu", it won't autocomplete to "gudhi". Compare to when I type "nu", it will autocomplete to numpy.
