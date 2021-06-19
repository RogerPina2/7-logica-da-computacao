int print(int a) {
    if (a == 0) {
        return 0;
    }
    print(a-1);
    println(a);
}

int main() {
    print(1);
}