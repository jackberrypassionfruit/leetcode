#include <iostream>
#include <list>
#include <string>
#include <iterator>
#include <cmath>

int main() {
    std::list<int> height = {1,8,6,2,5,4,8,3,7};

    int yesMax = 0;
    int maybeMax = 0;

    int i = 0;
    int j = height.size() - 1;

    /*
    std::list<int>::iterator it = height.begin();
    int a = std::advance(it, 0);

    auto it = height.begin();        same thing, but auto type, so shorter!
    */

    // int a = *std::next(height.begin(), 2);  
    // Indexes into the list, height. It's complicated because it is a doubly-linked list that has be accessed with an iterator object
    // also same thing, but a one liner! Notice, it creates a pointer to an integer, which is immediately dereferenced

    while (i < j) {
        int a = *std::next(height.begin(), i);
        int b = *std::next(height.begin(), j);

        maybeMax = std::min(a, b) * std::abs(i - j);
        if (maybeMax > yesMax)
        {
            yesMax = maybeMax;
        }

        if (a > b)
        {
            j -= 1;
        }
        else
        {
            i += 1;
        }
    }

    std::cout << yesMax << std::endl;

}