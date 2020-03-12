Thanks again @VincentRouvreau for helping me out with this issue.

## Installing QGLviewer

I tried

```
qmake -spec macx-g++ PREFIX=/usr/local
```

But it gave me this output and error:

```
Info: creating stash file /Users/herman/install/libQGLViewer-2.7.2/QGLViewer/.qmake.stash
Project ERROR: failed to parse default search paths from compiler output
```

According to some online sources[\[1\]](https://github.com/visualfc/goqt/issues/57)[\[2\]](https://forum.qt.io/topic/87941/compiling-qt-5-10-0-with-gcc-on-macos-10-13/4) the "preferred compiler" on mac OS is `clang`, so I tried something different and did the following.

```
qmake -spec macx-clang PREFIX=/usr/local # Returns no output.
make                                     # Returns over 700 lines of output, which are attached (makeOutput.txt)
sudo make install                        # returns over 200 lines of output, which are attached (makeInstallOutput.txt)
```

## Compiling GudhUI

According to the [CMake documentation](https://cmake.org/cmake/help/v3.17/manual/cmake.1.html) all the options need to be prefixed with `-D`. (Scroll down to "Create or update a CMake `CACHE` entry" in the linked documentation.)

```
cmake -DPython_ADDITIONAL_VERSIONS=3 -DCMAKE_BUILD_TYPE=Release -DQGLVIEWER_INCLUDE_DIR=/usr/local/lib/QGLViewer.framework/Headers ..
```

The entire output is below.

I don't get the bug you describe, but when I try to run an example in IPython3 I get the following:

```
In [1]: %run ~/Downloads/rips_complex_from_points_example.py
#####################################################################
RipsComplex creation from points
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
/Users/herman/Downloads/rips_complex_from_points_example.py in <module>()
     19 print("#####################################################################")
     20 print("RipsComplex creation from points")
---> 21 rips = gudhi.RipsComplex(points=[[0, 0], [1, 0], [0, 1], [1, 1]], max_edge_length=42)
     22
     23 simplex_tree = rips.create_simplex_tree(max_dimension=1)

AttributeError: module 'gudhi' has no attribute 'RipsComplex'
```

Is this part of the same issue or should I open a new one?

#### CMake output for GUDHI:

```
-- The C compiler identification is AppleClang 11.0.0.11000033
-- The CXX compiler identification is AppleClang 11.0.0.11000033
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++
-- Check for working CXX compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- GUDHI version : 3.1.1
-- Found Boost: /usr/local/lib/cmake/Boost-1.72.0/BoostConfig.cmake (found suitable version "1.72.0", minimum required is "1.56.0") found components: system filesystem unit_test_framework program_options thread
-- Found GMP: /usr/local/lib/libgmp.dylib  
-- Found GMPXX: /usr/local/lib/libgmpxx.dylib  
-- Using header-only CGAL
-- Targetting Unix Makefiles
-- Using /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ compiler.
-- DARWIN_VERSION=19
-- Mac Leopard detected
-- Found MPFR: /usr/local/lib/libmpfr.dylib  
-- Found Boost: /usr/local/lib/cmake/Boost-1.72.0/BoostConfig.cmake (found suitable version "1.72.0", minimum required is "1.48")  
-- Boost include dirs: /usr/local/include
-- Boost libraries:    
-- CGAL version: 5.00.2.100.
-- Build type: Release
-- USING CXXFLAGS = ' -O3 -DNDEBUG'
-- USING EXEFLAGS = ' '
-- Requested component: MPFR
-- Requested component: GMPXX
-- Requested component: GMP
-- Found Eigen3: /usr/local/include/eigen3 (found suitable version "3.3.7", minimum required is "3.1.0")
diff found in /usr/bin/diff
-- boost include dirs:/usr/local/include
-- boost library dirs:/usr/local/lib
-- Found PythonInterp: /Library/Frameworks/Python.framework/Versions/3.7/bin/python3 (found version "3.7.3")
++ Python module cython - Version 0.29.15 found
++ Python module pytest - Version 5.3.5 found
++ Python module matplotlib - Version 3.1.1 found
++ Python module numpy - Version 1.16.4 found
++ Python module scipy - Version 1.3.0 found
++ Python module sphinx - Version 2.4.3 found
++ Python module sklearn - Version 0.22.1 found
++ Python module ot - Version 0.6.0 found
-- Checking to see if CXX compiler accepts flag -Wall
-- Checking to see if CXX compiler accepts flag -Wall - yes
-- Performing Test GUDHI_CAN_USE_CXX11_THREAD_LOCAL_RESULT
-- Performing Test GUDHI_CAN_USE_CXX11_THREAD_LOCAL_RESULT - Failed
++ Release compilation flags are:  -Wall -pedantic -O3 -DNDEBUG
++ GUDHI_SUB_DIRECTORIES list is:";test;utilities"
-- Performing Test CGAL_CAN_USE_CXX11_THREAD_LOCAL_RESULT
-- Performing Test CGAL_CAN_USE_CXX11_THREAD_LOCAL_RESULT - Failed
++ /usr/local/lib/libboost_thread-mt.dylib => UNIX_LIB_FILE_NAME = boost_thread-mt
** Add Boost /usr/local/lib
++ /usr/local/lib/libgmp.dylib => UNIX_LIB_FILE_NAME = gmp
** Add gmp /usr/local/lib
++ /usr/local/lib/libgmpxx.dylib => UNIX_LIB_FILE_NAME = gmpxx
** Add gmpxx /usr/local/lib
++ /usr/local/lib/libmpfr.dylib => UNIX_LIB_FILE_NAME = mpfr
** Add mpfr /usr/local/lib/libmpfr.dylib
++ GUDHI_MODULES list is:"common;Alpha_complex;Bitmap_cubical_complex;Bottleneck_distance;Contraction;Cech_complex;Hasse_complex;Persistence_representations;Persistent_cohomology;Rips_complex;Simplex_tree;Skeleton_blocker;Spatial_searching;Subsampling;Tangential_complex;Toplex_map;Witness_complex;Nerve_GIC;GudhUI;python-documentation;python"
++ GUDHI_MISSING_MODULES list is:"cpp-documentation"
-- Configuring done
-- Generating done
-- Build files have been written to: /Users/herman/Library/Python/3.7/lib/python/site-packages/gudhi/build
```
