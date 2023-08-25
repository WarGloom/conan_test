git clean -d -f -x 
conan install .  -b missing $@
conan install .  -b missing  -s build_type=Debug $@
ls build
exit
conan install .  --deployer=lipo  -pr arm -b missing  $@
conan install .  --deployer=lipo_add  -pr intel -b missing  $@
conan install .  --deployer=lipo  -pr intel -b missing  -s build_type=Debug $@
conan install .  --deployer=lipo_add  -pr arm -b missing  -s build_type=Debug $@
ls build
exit
conan install .  --deployer=lipo  -pr arm -b missing  -s build_type=Release $@
conan install .  --deployer=lipo_add  -pr intel -b missing  -s build_type=Release $@
#conan install .  --deployer=lipo  -pr intel -b missing  -s build_type=Debug $@
#conan install .  --deployer=lipo_add  -pr arm -b missing  -s build_type=Debug $@

