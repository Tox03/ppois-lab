#include <iostream>
#include <string>
#include <cstring>
#include "ui/ConsoleMenu.h"

int main(int argc, char* argv[]) {
    ConsoleMenu menu;

    bool demo_mode = false;
    for (int i = 1; i < argc; ++i) {
        if (std::strcmp(argv[i], "--demo") == 0) {
            demo_mode = true;
            break;
        }
    }

    if (demo_mode) {
        menu.runDemo(std::cout);
    } else {
        menu.run(std::cin, std::cout);
    }

    return 0;
}
