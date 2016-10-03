# trompeloeil conan package

This is a [Conan.io](https://www.conan.io) package for the
[Trompeloeil](https://github.com/rollbear/trompeloeil) C++14 header
only mocking framework.

Please note that [Trompeloeil](https://github.com/rollbear/trompeloeil)
requires C++14. Make sure you build your test programs with C++14
support enabled.

## Track the `develop` branch

# Install

`$ conan install trompeloeil/develop@rollbear/testing --build`

# Project setup

In your `conanfile.txt` file, add:

```
[requires]
trompeloeil/develop@rollbear/testing
```

## Latest stable release

# Install

`$ conan install trompeloeil/v19@rollbear/stable --build`

# Project setup

In your `conanfile.txt` file, add:

```
[requires]
trompeloeil/v19@rollbear/stable
```
