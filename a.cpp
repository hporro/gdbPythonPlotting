#include <iostream>
#include <cassert>

template<class T>
struct Point{
    T x,y;
};

template<class T>
struct Triangle{
    Point<T> p1, p2, p3;
};

int main(){
    Triangle<float> t = Triangle<float>{Point<float>{0,0},Point<float>{1.2,1.3},Point<float>{2,0}};
    return 0;
}
