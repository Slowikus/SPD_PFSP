//
// Created by Slowikus on 08.04.2021.
//

#ifndef LAB4_DATA_H
#define LAB4_DATA_H

struct Data{

    long j = 0; //numer
    long r = 0; //czas przygotowania
    long p = 0; //czas wykonania
    long q = 0; //czas stygnięcia

};
struct compareQforQueue {
    bool operator()(const Data &a, const Data &b) {
        return a.q < b.q;
    }
};
#endif //LAB4_DATA_H
