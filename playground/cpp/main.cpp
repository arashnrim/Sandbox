/*
    Hello, C++!
    This file aims to explore the C++ programming language. Just to play around, of course,
    and have a simple compiled list of the syntax of C++!
*/

#include <iostream>

// ===================
// FUNCTIONS
// ===================

/*
    Declaring a function is as simple as entering the return type (void if nothing is returned)
    and the name of the function.

    Functions should be declared before the main() function (or anywhere else the function is
    being used); otherwise, the compiler may throw an error.
*/
void exampleFunction()
{
    // Enter code here
}

void helloWorld()
{
    /*
        std::cout is the equivalent of outputting content, followed by two less-than signs.
        Multiple less-than signs can be used together to concatenate the contents of the
        output, similar to using + with Python's print() function.

        In this instance, the std namespace is explicitly defined here. For more organised
        code, you can also consider adding `using namespace std;` at the start; that removes
        the need for `std` to be prepended, almost like importing in JavaScript or TypeScript!
    */
    std::cout << "Hello, world!" << std::endl;
}

void constantsAndVariables()
{
    /*
        In C++, both variables are defined by having the type of the variable followed by its
        name. While `languageName` below is technically a variable, it may be considered a
        constant in development since its value doesn't change.

        By right, though, to declare a constant, the `const` keyword should be used. This
        tells the compiler that the variable should be immutable.
    */
    std::string languageName = "C++";
    const std::string languageMascot = "???";

    /*
        languageName = "Another C variant"; <- ✓ OK
        languageMascot = "Ferris"; < - ⚠ error

        C++ will raise an error when you attempt to change the value of a constant. Constants
        are immutable, and hence their values cannot be changed.
    */

    std::cout << "languageName: " << languageName << std::endl;
    std::cout << "languageMascot: " << languageMascot << std::endl;

    /*
        On the other hand, variables are defined as is without the `const` keyword.
    */
    std::string greeting = "Good morning!";
    std::cout << "greeting (at declaration): " << greeting << std::endl;

    greeting = "Good afternoon!";
    std::cout << "greeting (after reassignment): " << greeting << std::endl;
}

/*
    The main() function is the main entry point of every C++ program; this shouldn't be too
    surprising since many programming languages do this too.

    In this case, the main() function returns an integer (therefore having the `int` keyword)
    as it always returns an exit code, as most if not all programs do.
*/
int main()
{
    exampleFunction();
    helloWorld();
    constantsAndVariables();
}