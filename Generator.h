#pragma once
#include <cmath>
#include <iostream>
#include <vector>
#include "Data.h"

class RandomNumberGenerator
{
private:
    int size = 10;
    long seed = 1;
    std::vector<Data> data;

public:
    //konstruktor
    RandomNumberGenerator(long seedValue, int size) {
        this->size = size;
        this->seed = seedValue;
    }

    RandomNumberGenerator() {

    }

    int nextInt(int low, int high) {
        long k;
        double value_0_1;
        long m = 2147483647l, a = 16807l, b = 127773l, c = 2836l;

        k = seed / b;
        seed = a * (seed % b) - k * c;
        if (seed < 0)
            seed = seed + m;
        value_0_1 = seed;
        value_0_1 /= m;
        return low + (int)floor(value_0_1 * (high - low + 1));
    }
    float nextFloat(int low, int high) {
        low *= 100000;
        high *= 100000;
        float val = nextInt(low, high) / 100000.0;
        return val;
    }
    //tworzy dane o zadanych wielkościach
    void create() {
        //seed = 1;
        //size  = 10;
        long sum = 0;
        long sum2 = 0;
        for (int i = 0; i < size; ++i) {
            data.push_back(Data());
            data[i].j = i+1;
        }
        for (int i = 0; i < size; ++i) {
            data[i].p = nextInt(1,29);
            sum += data[i].p;
        }
        for (int i = 0; i < size; ++i) {
            data[i].r = nextInt(1,sum);
        }
        for (int i = 0; i < size; ++i) {
            data[i].q = nextInt(1,sum);
        }
    }
    //wyświetla zawartość stworzonej instancji
    void print() {
        std::cout << "//////////////////////////////////" <<std::endl;
        std::cout << "j: [ ";
        for (int i = 0; i < size; ++i) {
            std::cout << data[i].j << " ";
        }
        std::cout << "]" <<std::endl;
        std::cout << "r: [ ";
        for (int i = 0; i < size; ++i) {
            std::cout << data[i].r << " ";
        }
        std::cout << "]" << std::endl;
        std::cout << "p: [ ";
        for (int i = 0; i < size; ++i) {
            std::cout << data[i].p << " ";
        }
        std::cout << "]" << std::endl;
        std::cout << "q: [ ";
        for (int i = 0; i < size; ++i) {
            std::cout << data[i].q << " ";
        }
        std::cout << "]" << std::endl;
        std::cout << "//////////////////////////////////" <<std::endl;
    }
    //wyswietla zawartosc wskazanego wektora danych
    static void print(std::vector<Data> data) {
        std::cout << "//////////////////////////////////" <<std::endl;
        std::cout << "j: [ ";
        for (int i = 0; i < data.size(); ++i) {
            std::cout << data[i].j << " ";
        }
        std::cout << "]" <<std::endl;
        std::cout << "r: [ ";
        for (int i = 0; i < data.size(); ++i) {
            std::cout << data[i].r << " ";
        }
        std::cout << "]" << std::endl;
        std::cout << "p: [ ";
        for (int i = 0; i < data.size(); ++i) {
            std::cout << data[i].p << " ";
        }
        std::cout << "]" << std::endl;
        std::cout << "q: [ ";
        for (int i = 0; i < data.size(); ++i) {
            std::cout << data[i].q << " ";
        }
        std::cout << "]" << std::endl;
        std::cout << "//////////////////////////////////" <<std::endl;
    }
    //ustal wielkosc oraz seed
    void setSeedAndSize () {
        std::cout << "Podaj seed: ";
        std::cin >> seed;
        std::cout << std::endl;
        std::cout << "Podaj rozmiar danych: ";
        std::cin >> size;
        std::cout << std::endl;

    }
    //przekazanie wektora danych
    std::vector<Data> get (){
        return data;
    }
};