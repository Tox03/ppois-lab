#include "ui/MenuManager.h"
#include "ui/TuringUI.h"
#include "ui/MarkovUI.h"
#include <iostream>
#include <string>

void MenuManager::runMainMenu() {
    int choice = -1;
    while (choice != 0) {
        std::cout << "\n============================================\n";
        std::cout << "        КОМПЛЕКС АБСТРАКТНЫХ МАШИН (Лаб. 1) \n";
        std::cout << "============================================\n";
        std::cout << "1. Машина Тьюринга\n";
        std::cout << "2. Нормальные алгорифмы Маркова\n";
        std::cout << "0. Выход\n";
        std::cout << "--------------------------------------------\n";
        std::cout << "Выберите абстрактную машину: ";

        if (!(std::cin >> choice)) {
            std::cin.clear();
            std::string dummy;
            std::getline(std::cin, dummy);
            continue;
        }

        switch (choice) {
            case 1:
                TuringUI::interactiveMode();
                break;
            case 2:
                MarkovUI::interactiveMode();
                break;
            case 0:
                std::cout << "До свидания!\n";
                break;
            default:
                std::cout << "Неизвестный пункт меню. Пожалуйста, попробуйте снова.\n";
        }
    }
}
