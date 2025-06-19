function mathematical(n) {
    return (r = n %9) ? r : n ? 9 : n
}
function recursive(n) {
    return n <10 ? n : recursive(Array.prototype.reduce.call(n.toString(),(A,V) => Number(V) +A,0))
}