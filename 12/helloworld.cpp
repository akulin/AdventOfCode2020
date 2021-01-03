#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
#include <unordered_set>
#include <cmath>
#include <iostream>

using namespace std;

void rotate(int* x, int* y, int count) {
    for (size_t i = 0; i < count; i++)
    {
        int temp = *x;
        *x = *y;
        *y = -temp;
    }
}


void solve() {
    long long x = 0;
    long long y = 0;
    int waypointX = 10;
    int waypointY = 1;
    
    int directionsX[] = {1, 0, -1, 0};
    int directionsY[] = {0, -1, 0, 1};
    int direction = 0;
    for (std::string line; std::getline(std::cin, line);) {
        char c = line[0];
        int arg =  std::stoi(line.substr(1));
        switch (c)
        {
            case 'N':
                waypointY += arg;
                break;
            case 'S':
                waypointY -= arg;
                break;
            case 'E':
                waypointX += arg;
                break;
            case 'W':
                waypointX -= arg;
                break;
            case 'R':
                rotate(&waypointX, &waypointY, arg / 90);
                break;
            case 'L':
                rotate(&waypointX, &waypointY, 4 - arg / 90);
                break;
            case 'F':
                x += waypointX * arg;
                y += waypointY * arg;
                break;
            default:
                break;
        }
       
    }
    cout << x << " " << y << endl;
    cout << abs(x) + abs(y) << endl;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    solve();
    return 0;
}
