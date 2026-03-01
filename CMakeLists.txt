cmake_minimum_required(VERSION 3.10.0)
project(SubnetTrainer VERSION 0.1.0 LANGUAGES C CXX)

# Packages
find_package(Python REQUIRED COMPONENTS Interpreter Development)
include(FetchContent)
FetchContent_Declare(
    pybind11
    GIT_REPOSITORY https://github.com/pybind/pybind11.git
    GIT_TAG        v2.13.6
)
FetchContent_MakeAvailable(pybind11)

# Output Files
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin)

# Output for specific build types
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG ${CMAKE_SOURCE_DIR}/bin/Debug)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE ${CMAKE_SOURCE_DIR}/bin/Release)

# Executable
add_executable(SubnetTrainer main.cpp)
target_link_libraries(SubnetTrainer PRIVATE pybind11::embed)
