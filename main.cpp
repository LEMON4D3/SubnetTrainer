#include <pybind11/embed.h>
namespace py = pybind11;

int main(int, char**){
    py::scoped_interpreter guard{};
    py::module_ MainPy = py::module_::import("main");
    MainPy.attr("main")();

    return 0;
}
