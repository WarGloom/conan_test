import os

from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout
from conan.tools.layout import basic_layout
from conan.tools.apple import XcodeDeps
from conan.tools.apple import XcodeToolchain


class CompressorRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    # generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires("bzip2/1.0.8")
        self.requires("gtest/1.13.0")

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
            tc.generator="Ninja"
        else:
            tc.blocks["apple_system"].values["cmake_osx_architectures"] ="x86_64;arm64"
            tc.generator="Xcode"
        tc.generate()
        pass

    def layout(self):
        # pass
        # multi = True if self.settings.get_safe("compiler") == "msvc" else False
        multi = True if  self.settings.os =="Macos" else False
        if multi:
            self.folders.generators = os.path.join(self.folders.build, "generators")
        else:
            self.folders.generators = os.path.join(self.folders.build, str(self.settings.build_type), "generators")
        print(self.folders.build)
        # cmake_layout(self)
    # def build(self):
    #     self.arch = "x86_64;arm64" 
    #     xcodebuild = XcodeBuild(Compressor)
    #     xcodebuild.build("Compressor.xcodeproj")
