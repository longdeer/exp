var fibGenerator = function*() {

    var a = 0;
    var b = 1;

    while(true)
    {
        yield a;
        [ a,b ] = [ a +b,a ];
    }
};