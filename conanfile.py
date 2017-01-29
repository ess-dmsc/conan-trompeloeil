from conans import ConanFile, CMake

class TrompeloeilConan(ConanFile):
    name = "trompeloeil"
    version = "v23"
    license = "Boost"
    author = "Bjorn Fahller (bjorn@fahller.se)"
    url = "https://github.com/rollbear/trompeloeil-conan.git"
    settings = None # header only

    def build(self):
        None # header only

    def source(self):
        self.run("git clone https://github.com/rollbear/trompeloeil.git --branch v23")

    def package(self):
        self.copy("*.hpp", dst="include", src="trompeloeil")
