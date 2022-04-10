#include <iostream>
#include <list>
#include <string>
#include <iterator>
#include <algorithm>

int main() {
    std::list<int> height = {1,8,6,2,5,4,8,3,7};

    int yesMax = 0;
    int maybeMax = 0;

    int i = 0;
    int j = height.size() - 1;

    std::list<int>::iterator it = height.begin();
    // auto it = height.begin();        same thing, but auto type, so shorter!
    std::advance(it, 0);
    // int *it = std::next(height.begin(), 2);  same thing, but a one liner! Notice, it createsa pointer to an integer

    // while (i < j) {


    // }


    std::cout << *it << std::endl;

}