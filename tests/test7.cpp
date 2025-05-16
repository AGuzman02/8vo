#numero incorrecto de argumentos

program test7;

var x : int;
var y : int;
var z : int;

void sumar(int x, int y) : void {
}

main {
    x = 2;
    y = 3;
    z = 9;
    print(sumar(x, y, z));
    print(sumar(z));
}
end