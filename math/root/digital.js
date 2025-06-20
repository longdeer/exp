function mathematical(n) {
    return (r = n %9) ? r : n ? 9 : n
}
function recursive(n) {
    return n <10 ? n : recursive(Array.prototype.reduce.call(n.toString(),(A,V) => Number(V) +A,0))
}
function iterative(n) {
    var sum;

    while(9 <n) {
        sum = 0;

        while(n) {

            sum += n %10;
            n = Math.floor(n /10);
        }
        n = sum;
    }
    return n;
}