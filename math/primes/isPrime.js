var isPrime = function(n) {

    if(n <2) return false;
    if(n == 2 || n == 3) return true;
    if(n%2 == 0 || n%3 == 0) return false;

    var i = 5;
    var j = n **.5;

    while(i <= j) {
        if(n%i == 0 || n%(i+2) == 0) return false;
        i += 6;
    }
    return true;
}