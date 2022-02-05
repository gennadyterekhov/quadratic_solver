#include <iostream>
#include <cstdlib>
#include <cmath>


int main(int argc, char **argv) {

    double coef_a = 0;
    double coef_b = 0;
    double coef_c = 0;
    double D_sqrt = 0;
    double root_1 = 0;
    double root_2 = 0;

    if (argc != 4) {
        std::cout << "Expected 3 arguments, found " << argc - 1 << std::endl;

        return 1;
    }

    coef_a = atof(argv[1]);
    coef_b = atof(argv[2]);
    coef_c = atof(argv[3]);
    std::cout << "a = " << coef_a << "\n";
    std::cout << "b = " << coef_b << "\n";
    std::cout << "c = " << coef_c << "\n";

    if (coef_a == 0) {
        if (coef_b == 0) {
            if (coef_c == 0) {
                std::cout << "root is any number\n";

                return 0;     
            } else {
                std::cout << "no root. " << coef_c << " =/= 0";

                return 0;  
            }
        }
        std::cout << "a = 0, not actually a quadratic \nroot = " << -coef_c / coef_b << std::endl;

        return 0;
    }


    D_sqrt = std::sqrt(coef_b * coef_b - 4 * coef_a * coef_c);
    root_1 = (-coef_b + D_sqrt) / (2 * coef_a);
    root_2 = (-coef_b - D_sqrt) / (2 * coef_a);

    std::cout << "root 1 = " << root_1 << "\n";
    std::cout << "root 2 = " << root_2 << "\n";
    std::cout << "\n";
    return 0;
}
