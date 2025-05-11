program ejemplo;

var x : int;
var y : int;

void suma(int a, int b) : int {
    var r : int;
    r = a + b;
    return r;
}

main {
    x = 5;
    y = suma(x, 3);

    if (y > 5) {
        print("mayor");
    } else {
        print("menor o igual");
    }

    while (x > 0) {
        print(x);
        x = x - 1;
    }
}
end