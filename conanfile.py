from conans import ConanFile, CMake
from conans.tools import download, unzip, replace_in_file
import os

class PbjsonConan(ConanFile):
    name = "pbjson"
    version = "0.0.1"
    ZIP_FOLDER_NAME = "conan-%s-%s" % (name, version)
    url = "https://github.com/0x7f/conan-pbjson"
    license = "https://github.com/0x7f/conan-pbjson/blob/master/LICENSE"
    export = "*"
    settings = "os", "compiler", "build_type", "arch"
    requires = "RapidJSON/1.0.2@SamuelMarks/stable", "Protobuf/2.6.1@memsharded/testing"
    generators = "cmake"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"

    def source(self):
        zip_name = "v%s.zip" % self.version
        download("https://github.com/0x7f/conan-pbjson/archive/%s" % zip_name, zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin") # From bin to bin
        self.copy("*.dylib*", dst="bin", src="lib") # From lib to bin

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake %s %s' % (self.ZIP_FOLDER_NAME, cmake.command_line))
        self.run('cmake --build . %s' % (cmake.build_config))

    def package(self):
        self.copy("*.hpp", dst="include", src="%s/src" % self.ZIP_FOLDER_NAME)
        self.copy("*.h", dst="include", src="%s/src" % self.ZIP_FOLDER_NAME)
        self.copy("*.lib", dst="lib", src="lib")
        self.copy("*.a", dst="lib", src="lib")

    def package_info(self):
        self.cpp_info.libs = ["pbjson"]

