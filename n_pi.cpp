#include"includes/fmexp.cpp"
#include<iostream>

int bbp(int n) {
    double sum = 0;
    using fmexp::pow;
    for (int k = 0; k <= n; k++) {
        int q = 8 * k + 1,
            w = 8 * k + 4,
            e = 8 * k + 5,
            r = 8 * k + 6;
        sum += 4 * (((double)pow(16, n - k, q)) / (double)q) - 2 * (((double)pow(16, n - k, w)) / (double)w) - (((double)pow(16, n - k, e)) / (double)e) - (((double)pow(16, n - k, r)) / (double)r);
    }
    return (int(sum * 16) % 16 + 16) % 16;
}

int main() {
    std::cout << bbp(10000000) << "\n";
    return 0;
}