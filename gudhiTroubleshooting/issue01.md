Thanks to both @mglisse and @VincentRouvreau for their replies. First comes my response to [mglisee](#CMake), and then a response to [VincentRouvreau](#FixingHomebrewlinks).

## <a name="CMake"></a> CMake

I reduced the number of missing Qt5 components to just QGLViewer since my last post by erasing `CMakeCache.txt` and refreshing `$PATH$`. I installed QGLViewer according to the Mac OS X instructions in the [QGLViewer website](http://libqglviewer.com/installUnix.html).

> Did cmake say anything interesting before that?

Previously I got the following output with some CMake warnings, most of which I was able to avoid by implementing this [solution](https://stackoverflow.com/a/58085634/5478086) from StackOverflow.

```
(base) 06:00 PM [4] ~/Library/Python/3.7/lib/python/site-packages/gudhi/build --> cmake -DPython_ADDITIONAL_VERSIONS=3 ..
-- The C compiler identification is AppleClang 11.0.0.11000033
-- The CXX compiler identification is AppleClang 11.0.0.11000033
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc
-- Check for working C compiler: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/cc -- works
-- Detecting Ccompiler ABI info
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


CMake Warning at /usr/local/lib/cmake/boost_system-1.72.0/libboost_system-variant-shared.cmake:64 (message):
  Target Boost::system already has an imported location
  '/usr/local/lib/libboost_system-mt.dylib', which will be overwritten with
  '/usr/local/lib/libboost_system.dylib'
Call Stack (most recent call first):
  /usr/local/lib/cmake/boost_system-1.72.0/boost_system-config.cmake:57 (include)
  /usr/local/lib/cmake/Boost-1.72.0/BoostConfig.cmake:120 (find_package)
  /usr/local/lib/cmake/Boost-1.72.0/BoostConfig.cmake:185 (boost_find_component)
  /usr/local/Cellar/cmake/3.16.5/share/cmake/Modules/FindBoost.cmake:443 (find_package)
  src/cmake/modules/GUDHI_third_party_libraries.cmake:3 (find_package)
  CMakeLists.txt:17 (include)


CMake Warning at /usr/local/lib/cmake/boost_filesystem-1.72.0/libboost_filesystem-variant-shared.cmake:64 (message):
  Target Boost::filesystem already has an imported location
  '/usr/local/lib/libboost_filesystem-mt.dylib', which will be overwritten
  with '/usr/local/lib/libboost_filesystem.dylib'
Call Stack (most recent call first):
  /usr/local/lib/cmake/boost_filesystem-1.72.0/boost_filesystem-config.cmake:57 (include)
  /usr/local/lib/cmake/Boost-1.72.0/BoostConfig.cmake:120 (find_package)
  /usr/local/lib/cmake/Boost-1.72.0/BoostConfig.cmake:185 (boost_find_component)
  /usr/local/Cellar/cmake/3.16.5/share/cmake/Modules/FindBoost.cmake:443 (find_package)
  src/cmake/modules/GUDHI_third_party_libraries.cmake:3 (find_package)
  CMakeLists.txt:17 (include)


CMake Warning at /usr/local/lib/cmake/boost_unit_test_framework-1.72.0/libboost_unit_test_framework-variant-shared.cmake:64 (message):
  Target Boost::unit_test_framework already has an imported location
  '/usr/local/lib/libboost_unit_test_framework-mt.dylib', which will be
  overwritten with '/usr/local/lib/libboost_unit_test_framework.dylib'
Call Stack (most recent call first):
  /usr/local/lib/cmake/boost_unit_test_framework-1.72.0/boost_unit_test_framework-config.cmake:57 (include)
  /usr/local/lib/cmake/Boost-1.72.0/BoostConfig.cmake:120 (find_package)
  /usr/local/lib/cmake/Boost-1.72.0/BoostConfig.cmake:185 (boost_find_component)
  /usr/local/Cellar/cmake/3.16.5/share/cmake/Modules/FindBoost.cmake:443 (find_package)
  src/cmake/modules/GUDHI_third_party_libraries.cmake:3 (find_package)
  CMakeLists.txt:17 (include)


CMake Warning at /usr/local/lib/cmake/boost_program_options-1.72.0/libboost_program_options-variant-shared.cmake:64 (message):
  Target Boost::program_options already has an imported location
  '/usr/local/lib/libboost_program_options-mt.dylib', which will be
  overwritten with '/usr/local/lib/libboost_program_options.dylib'
Call Stack (most recent call first):
  /usr/local/lib/cmake/boost_program_options-1.72.0/boost_program_options-config.cmake:57 (include)
  /usr/local/lib/cmake/Boost-1.72.0/BoostConfig.cmake:120 (find_package)
  /usr/local/lib/cmake/Boost-1.72.0/BoostConfig.cmake:185 (boost_find_component)
  /usr/local/Cellar/cmake/3.16.5/share/cmake/Modules/FindBoost.cmake:443 (find_package)
  src/cmake/modules/GUDHI_third_party_libraries.cmake:3 (find_package)
  CMakeLists.txt:17 (include)


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
-- Build type:
-- USING CXXFLAGS = ' '
-- USING EXEFLAGS = ' '
-- Requested component: MPFR
-- Requested component: GMPXX
-- Requested component: GMP
-- Found Eigen3: /usr/local/include/eigen3 (found suitable version "3.3.7", minimum required is "3.1.0") diff found in /usr/bin/diff
-- boost include dirs:/usr/local/include
-- boost library dirs:/usr/local/lib
-- Found PythonInterp: /Users/herman/opt/anaconda3/bin/python3 (found version "3.7.4")
++ Python module cython - Version 0.29.13 found
++ Python module pytest - Version 5.2.1 found
++ Python module matplotlib - Version 3.1.1 found
++ Python module numpy - Version 1.17.2 found
++ Python module scipy - Version 1.3.1 found
++ Python module sphinx - Version 2.2.0 found
++ Python module sklearn - Version 0.21.3 found
PYTHON_MODULE_NAME = ot
     - PYTHON_MODULE_RESULT = 1
     - PYTHON_MODULE_VERSION =
     - PYTHON_MODULE_ERROR = Traceback (most recent call last):
  File "<string>", line 1, in <module>
ModuleNotFoundError: No module named 'ot'

-- Checking to see if CXX compiler accepts flag -Wall
-- Checking to see if CXX compiler accepts flag -Wall - yes
-- Performing Test GUDHI_CAN_USE_CXX11_THREAD_LOCAL_RESULT
-- Performing Test GUDHI_CAN_USE_CXX11_THREAD_LOCAL_RESULT - Failed
++ Release compilation flags are:  -Wall -pedantic -O3 -DNDEBUG
++ GUDHI_SUB_DIRECTORIES list is:";test;utilities"
++ GudhUI will not be compiled because QGLViewer is not found
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
++ Python documentation module will not be compiled because POT was not found
++ GUDHI_MODULES list is:"common;Alpha_complex;Bitmap_cubical_complex;Bottleneck_distance;Contraction;Cech_complex;Hasse_complex;Persistence_representations;Persistent_cohomology;Rips_complex;Simplex_tree;Skeleton_blocker;Spatial_searching;Subsampling;Tangential_complex;Toplex_map;Witness_complex;Nerve_GIC;python"
++ GUDHI_MISSING_MODULES list is:"GudhUI;python-documentation;cpp-documentation" CMake Warning at /usr/local/lib/cmake/CGAL/CGAL_enable_end_of_configuration_hook.cmake:99 (message):
  =======================================================================

  CGAL performance notice:

  The variable CMAKE_BUILD_TYPE is set to "".  For performance reasons, you
  should set CMAKE_BUILD_TYPE to "Release".

  Set CGAL_DO_NOT_WARN_ABOUT_CMAKE_BUILD_TYPE to TRUE if you want to disable
  this warning.

  =======================================================================
Call Stack (most recent call first):
  CMakeLists.txt:9999 (CGAL_run_at_the_end_of_configuration)


-- Configuring done
-- Generating done
-- Build files have been written to: /Users/herman/Library/Python/3.7/lib/python/site-packages/gudhi/build
```

> Did cmake find parts of Qt5 but not some components, or did it not find it at all? You can use cmake-gui or ccmake to examine the result.

Originally the only message I got regarding Qt5 was the one in my original post (its components were missing). But running `cmake` again with the commands you recommended I get the following:

1. I don't have `cmake-gui` installed, so I couldn't try it out.
2. I run `ccmake` with the `c` (configure) option and get the following output:

  ```
  BUILD_TESTING                   *OFF                                                                                                           
 Boost_FILESYSTEM_LIBRARY_RELEA  */usr/local/lib/libboost_filesystem-mt.dylib                                                                   
 Boost_INCLUDE_DIR               */usr/local/include                                                                                            
 Boost_PROGRAM_OPTIONS_LIBRARY_  */usr/local/lib/libboost_program_options-mt.dylib                                                              
 Boost_SYSTEM_LIBRARY_RELEASE    */usr/local/lib/libboost_system-mt.dylib                                                                       
 Boost_THREAD_LIBRARY_RELEASE    */usr/local/lib/libboost_thread-mt.dylib                                                                       
 Boost_UNIT_TEST_FRAMEWORK_LIBR  */usr/local/lib/libboost_unit_test_framework-mt.dylib                                                          
 CGAL_CTEST_DISPLAY_MEM_AND_TIM  *OFF                                                                                                           
 CGAL_DEV_MODE                   *OFF                                                                                                           
 CGAL_DIR                        */usr/local/lib/cmake/CGAL                                                                                     
 CGAL_TEST_DRAW_FUNCTIONS        *OFF                                                                                                           
 CGAL_WITH_GMPXX                 *OFF                                                                                                           
 CMAKE_BUILD_TYPE                *                                                                                                              
 CMAKE_EXECUTABLE_FORMAT         *MACHO                                                                                                         
 CMAKE_INSTALL_PREFIX            */usr/local                                                                                                    
 CMAKE_OSX_ARCHITECTURES         *                                                                                                              
 CMAKE_OSX_DEPLOYMENT_TARGET     *                                                                                                              
 CMAKE_OSX_SYSROOT               */Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.15.sdk           
 DIFF_PATH                       */usr/bin/diff                                                                                                 
 EIGEN3_INCLUDE_DIR              */usr/local/include/eigen3                                                                                     
 GCOVR_PATH                      *GCOVR_PATH-NOTFOUND                                                                                           
 GIT_EXECUTABLE                  */usr/bin/git                                                                                                  
 GMPXX_INCLUDE_DIR               */usr/local/include                                                                                            
 GMPXX_LIBRARIES                 */usr/local/lib/libgmpxx.dylib                                                                                 
 GMPXX_LIBRARIES_DIR             */usr/local/lib                                                                                                
 GMP_INCLUDE_DIR                 */usr/local/include                                                                                            
 GMP_LIBRARIES                   */usr/local/lib/libgmp.dylib                                                                                   
 GMP_LIBRARIES_DIR               */usr/local/lib                                                                                                
 GNUPLOT_PATH                    *GNUPLOT_PATH-NOTFOUND                                                                                         
 GPROF_PATH                      *GPROF_PATH-NOTFOUND                                                                                           
 MPFR_INCLUDE_DIR                */usr/local/include                                                                                            
 MPFR_LIBRARIES                  */usr/local/lib/libmpfr.dylib                                                                                  
 MPFR_LIBRARIES_DIR              */usr/local/lib                                                                                                
 QGLVIEWER_INCLUDE_DIR           *QGLVIEWER_INCLUDE_DIR-NOTFOUND                                                                                
 QGLVIEWER_LIBRARY_DEBUG         *QGLVIEWER_LIBRARY_DEBUG-NOTFOUND                                                                              
 QGLVIEWER_LIBRARY_RELEASE       *QGLVIEWER_LIBRARY_RELEASE-NOTFOUND                                                                            
 Qt5Core_DIR                     */usr/local/opt/qt/lib/cmake/Qt5Core                                                                           
 Qt5Gui_DIR                      */usr/local/opt/qt/lib/cmake/Qt5Gui                                                                            
 Qt5OpenGL_DIR                   */usr/local/opt/qt/lib/cmake/Qt5OpenGL                                                                         
 Qt5Widgets_DIR                  */usr/local/opt/qt/lib/cmake/Qt5Widgets                                                                        
 Qt5Xml_DIR                      */usr/local/opt/qt/lib/cmake/Qt5Xml                                                                            
 Qt5_DIR                         */usr/local/opt/qt/lib/cmake/Qt5                                                                               
 SPHINX_PATH                     */Users/herman/Library/Python/3.7/bin/sphinx-build                                                             
 WITH_GUDHI_BENCHMARK            *OFF                                                                                                           
 WITH_GUDHI_BOOST_TEST_COVERAGE  *OFF                                                                                                           
 WITH_GUDHI_EXAMPLE              *OFF                                                                                                           
 WITH_GUDHI_PYTHON               *ON                                                                                                            
 WITH_GUDHI_PYTHON_RUNTIME_LIBR  *ON                                                                                                            
 WITH_GUDHI_TEST                 *ON                                                                                                            
 WITH_GUDHI_USE_TBB              *ON                                                                                                            
 WITH_GUDHI_UTILITIES            *ON                                                                                                            
 WITH_MODULE_GUDHI_Alpha_comple  *ON                                                                                                            
 WITH_MODULE_GUDHI_Bitmap_cubic  *ON                                                                                                            
 WITH_MODULE_GUDHI_Bottleneck_d  *ON                                                                                                            
 WITH_MODULE_GUDHI_Cech_complex  *ON                                                                                                            
 WITH_MODULE_GUDHI_Contraction   *ON                                                                                                            
 WITH_MODULE_GUDHI_Hasse_comple  *ON                                                                                                            
 WITH_MODULE_GUDHI_Nerve_GIC     *ON                                                                                                            
 WITH_MODULE_GUDHI_Persistence_  *ON                                                                                                            
 WITH_MODULE_GUDHI_Persistent_c  *ON                                                                                                            
 WITH_MODULE_GUDHI_Rips_complex  *ON                                                                                                            
 WITH_MODULE_GUDHI_Simplex_tree  *ON                                                                                                            
 WITH_MODULE_GUDHI_Skeleton_blo  *ON                                                                                                            
 WITH_MODULE_GUDHI_Spatial_sear  *ON                                                                                                            
 WITH_MODULE_GUDHI_Subsampling   *ON                                                                                                            
 WITH_MODULE_GUDHI_Tangential_c  *ON                                                                                                            
 WITH_MODULE_GUDHI_Toplex_map    *ON                                                  
  ```

> Maybe you just need to tell it where Qt is with Qt5_DIR.

How do I do that?

> You could check if there are files with a name similar to libQt5Widgets.so.5 (maybe .dylib on mac?) in your brew directory, same with xml and opengl.

```bash
find /usr/local/Homebrew/Library/Taps/homebrew -name "libQt5*"
# no results
find /usr/local/Homebrew -name "libQt5*"
# no results
find /usr/local/Cellar -name "libQt5*"
# Returns the following:
/usr/local/Cellar/qt/5.14.1/lib/libQt5DeviceDiscoverySupport.prl
/usr/local/Cellar/qt/5.14.1/lib/libQt5QmlDebug.prl
/usr/local/Cellar/qt/5.14.1/lib/libQt5EdidSupport.a
/usr/local/Cellar/qt/5.14.1/lib/libQt5PacketProtocol.a
/usr/local/Cellar/qt/5.14.1/lib/libQt5EdidSupport.prl
/usr/local/Cellar/qt/5.14.1/lib/libQt5PlatformCompositorSupport.prl
/usr/local/Cellar/qt/5.14.1/lib/libQt5FontDatabaseSupport.a
/usr/local/Cellar/qt/5.14.1/lib/libQt5UiTools.a
/usr/local/Cellar/qt/5.14.1/lib/libQt5GraphicsSupport.prl
/usr/local/Cellar/qt/5.14.1/lib/libQt5GraphicsSupport.a
/usr/local/Cellar/qt/5.14.1/lib/libQt5ClipboardSupport.prl
/usr/local/Cellar/qt/5.14.1/lib/libQt5ThemeSupport.prl
/usr/local/Cellar/qt/5.14.1/lib/libQt5QmlDebug.a
/usr/local/Cellar/qt/5.14.1/lib/libQt5DeviceDiscoverySupport.a
/usr/local/Cellar/qt/5.14.1/lib/libQt5QmlDevTools.prl
/usr/local/Cellar/qt/5.14.1/lib/libQt5UiTools.prl
/usr/local/Cellar/qt/5.14.1/lib/libQt5FontDatabaseSupport.prl
/usr/local/Cellar/qt/5.14.1/lib/libQt5QmlDevTools.a
/usr/local/Cellar/qt/5.14.1/lib/libQt5ThemeSupport.a
/usr/local/Cellar/qt/5.14.1/lib/libQt5ServiceSupport.a
/usr/local/Cellar/qt/5.14.1/lib/libQt5PacketProtocol.prl
/usr/local/Cellar/qt/5.14.1/lib/libQt5EventDispatcherSupport.a
/usr/local/Cellar/qt/5.14.1/lib/libQt5Bootstrap.prl
/usr/local/Cellar/qt/5.14.1/lib/libQt5ServiceSupport.prl
/usr/local/Cellar/qt/5.14.1/lib/libQt5ClipboardSupport.a
/usr/local/Cellar/qt/5.14.1/lib/libQt5Bootstrap.a
/usr/local/Cellar/qt/5.14.1/lib/libQt5OpenGLExtensions.a
/usr/local/Cellar/qt/5.14.1/lib/libQt5FbSupport.prl
/usr/local/Cellar/qt/5.14.1/lib/libQt5AccessibilitySupport.a
/usr/local/Cellar/qt/5.14.1/lib/libQt5PlatformCompositorSupport.a
/usr/local/Cellar/qt/5.14.1/lib/libQt5FbSupport.a
/usr/local/Cellar/qt/5.14.1/lib/libQt5EventDispatcherSupport.prl
/usr/local/Cellar/qt/5.14.1/lib/libQt5OpenGLExtensions.prl
/usr/local/Cellar/qt/5.14.1/lib/libQt5AccessibilitySupport.prl
```

> I am not a pro of cmake, the first thing that comes to mind is running cmake with the --trace option, and looking at the parts that talk about Qt...

```bash
cd /Users/herman/Library/Python/3.7/lib/python/site-packages/gudhi
cmake --trace -DPython_ADDITIONAL_VERSIONS=3 ..
```

Returns [this output](#https://raw.githubusercontent.com/ChemGuy88/oda/master/cmakeTrace.txt) with over 15,000 lines and 3207 mentions of "Qt5" (2.4 MB text file).

## <a name="FixingHomebrewlinks"></a> Fixing Homebrew links

- [x] Fix link

``` bash
# brew install glfw
brew link --force qt5 && sudo ln -s /usr/local/Cellar/qt/5.14.1/mkspecs /usr/local/mkspecs && ln -s /usr/local/Cellar/qt/5.14.1/plugins /usr/local/plugins
brew link --force qt5 && ln -s /usr/local/Cellar/qt/5.14.1/plugins /usr/local/plugins
```

- [x] Then install QGLViewer

```bash
cd ~/libQGLViewer-2.7.2/
qmake -spec macx-xcode
# Output:
Info: creating stash file /Users/herman/libQGLViewer-2.7.2/.qmake.stash
Info: creating cache file /Users/herman/libQGLViewer-2.7.2/.qmake.cache
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/QGLViewer/QGLViewer.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/designerPlugin/qglviewerplugin.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/animation/animation.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/callback/callback.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/cameraLight/cameraLight.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/clippingPlane/clippingPlane.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/constrainedCamera/constrainedCamera.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/constrainedFrame/constrainedFrame.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/drawLight/drawLight.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/fastDraw/fastDraw.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/frameTransform/frameTransform.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/frustumCulling/frustumCulling.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/interface/interface.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/keyboardAndMouse/keyboardAndMouse.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/keyFrames/keyFrames.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/luxo/luxo.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/manipulatedFrame/manipulatedFrame.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/mouseGrabber/mouseGrabber.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/multiSelect/multiSelect.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/multiView/multiView.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/overpainting/overpainting.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/screenCoordSystem/screenCoordSystem.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/select/select.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/simpleViewer/simpleViewer.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/standardCamera/standardCamera.xcodeproj'
WARNING: Ignored (not found) '/Users/herman/libQGLViewer-2.7.2/examples/stereoViewer/stereoViewer.xcodeproj'
```

I tried to run `cmake` again despite the warnings from the QGLViewer install, but CMake says that the Gudhi UI was still not installed. Maybe I need to pass `-CMAKE_BUILD_TYPE="Release"`? What is the syntax to do that? Is it like this:

`cmake -DPython_ADDITIONAL_VERSIONS=3 -CMAKE_BUILD_TYPE="Release" ..` ?
