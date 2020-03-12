a> Did you stop after `cmake`? That's just the configuration step (like qmake), then you actually need to **build**, see the installation instructions.

## Installing Gudhi

@mglisse, I ran `make` and `sudo make install` after `cmake`, as I was [suggested to](#https://github.com/GUDHI/gudhi-devel/issues/241#issuecomment-596572300). I apologize for not attaching the output of that command. The output for both should be attached now [here](#https://github.com/ChemGuy88/oda/blob/master/gudhiTroubleshooting/makeOutput.txt) and [here](#https://github.com/ChemGuy88/oda/blob/master/gudhiTroubleshooting/makeInstallOutput.txt).

I run:

```
cd ~/Library/Python/3.7/lib/python/site-packages/gudhi/build
cmake -DPython_ADDITIONAL_VERSIONS=3 -DCMAKE_BUILD_TYPE=Release -DQGLVIEWER_INCLUDE_DIR=/usr/local/lib/QGLViewer.framework/Headers -DWITH_GUDHI_EXAMPLE=ON ..
make
```

`make` returns some output with 4 warnings and 1 error ([output file](#))

## Installing Gudhi Python Package

@VincentRouvreau.
