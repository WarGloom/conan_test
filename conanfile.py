import os

from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout
from conan.tools.layout import basic_layout
from conan.tools.apple import XcodeDeps
from conan.tools.apple import XcodeToolchain
from conan.tools.cmake.utils import is_multi_configuration


class CompressorRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    # generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires("bzip2/1.0.8")
        self.requires("gtest/1.13.0")

    def _is_multi(self):
        gen = self.conf.get("tools.cmake.cmaketoolchain:generator")
        print("AAAA",gen)
        if gen:
            return is_multi_configuration(gen)
        else:
            compiler = self.settings.get_safe("compiler")
            if compiler == "msvc":
                return  True
            else:
                return False
    
    def build_requirements(self):
        #self.tool_requires("cmake/3.27.2")
        pass
    def generate(self):
        print(self.settings.os)
        if self.settings.os =="Macos":
           xcode = XcodeDeps(self)
           xcode.generate()
           tc = XcodeToolchain(self)
           tc.generate()
        # else:   
        deps = CMakeDeps(self)
        deps.check_components_exist = True
        deps.set_property("*", "cmake_find_mode", "config")
        deps.generate()
        tc = CMakeToolchain(self)
        print(self.conf.get("tools.cmake.cmaketoolchain:generator"))
        for require, dependency in self.dependencies.items():
            self.output.info("Dependency is direct={}: {}".format(require.direct, dependency.ref))
        if self.settings.os !="Macos":
            print("tc.generator: " , tc.generator)#="Ninja"
            # tc.generator="Ninja Multi-Config" # ???
        else:
            tc.blocks["apple_system"].values["cmake_osx_architectures"] ="x86_64;arm64"
            print("aAaa", tc.generator)
            tc.generator="Xcode"
        tc.generate()
        pass

    def layout(self):
        # pass
        if self.settings.os =="Macos":
            cmake_layout(self, generator="Xcode")
        #     self.folders.generators = os.path.join(self.folders.build, "generators")
        else:
            cmake_layout(self)
        #     self.folders.generators = os.path.join(self.folders.build, str(self.settings.build_type), "generators")
        # print(self.folders.build)

    # def build(self):
    #     self.arch = "x86_64;arm64" 
    #     xcodebuild = XcodeBuild(Compressor)
    #     xcodebuild.build("Compressor.xcodeproj")
