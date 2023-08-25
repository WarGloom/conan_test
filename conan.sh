#!/bin/bash 
git clean -d -f -x 
#conan install .  -b missing -of build $@
if [ "$1" = "mac" ]; then
conan install .  --deployer=lipo  -pr arm -b missing $2
conan install .  --deployer=lipo_add  -pr intel -b missing  $2
conan install .  --deployer=lipo  -pr intel -b missing  -s build_type=Debug $2
conan install .  --deployer=lipo_add  -pr arm -b missing  -s build_type=Debug $2
conan install .  --deployer=lipo  -pr intel -b missing  -s build_type=RelWithDebInfo $2
conan install .  --deployer=lipo_add  -pr arm -b missing  -s build_type=RelWithDebInfo $2
echo INSTALL FAT BINARIES
else
conan install .  -b missing  -s build_type=Release $2
conan install .  -b missing  -s build_type=Debug $2
conan install .  -b missing  -s build_type=RelWithDebInfo $2
fi
tree -d build
cmake --list-presets all
echo $1
exit
conan install .  -b missing  -s build_type=Release $@
conan install .  -b missing  -s build_type=Debug $@
conan install .  -b missing  -s build_type=RelWithDebInfo $@

conan install .  -b missing  -s build_type=Release -of build  $@
conan install .  -b missing  -s build_type=Debug -of build  $@
exit
ls build
exit
conan install .  --deployer=lipo  -pr arm -b missing  -s build_type=Release $@
conan install .  --deployer=lipo_add  -pr intel -b missing  -s build_type=Release $@
#conan install .  --deployer=lipo  -pr intel -b missing  -s build_type=Debug $@
#conan install .  --deployer=lipo_add  -pr arm -b missing  -s build_type=Debug $@

