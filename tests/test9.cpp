#regresa tipo incorrecto

program test9;

var x : int;

void suma(int x) : int {
    return "ejemplo";
}

void resta(int x) : void {
    return x;
}

main {
    print(suma(2));
    print(resta(3));
}
end