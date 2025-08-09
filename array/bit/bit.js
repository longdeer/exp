

function BIT(size) { this.size = size; this.inner = new Array(size).fill(0) }
BIT.prototype.update = function(i) {

    var j = i +1;
    while(j <this.size) { ++this.inner[j]; j += j& -j }
}
BIT.prototype.query = function(i) {

    var j = i +1;
    var s = 0;
    while(0 <j) { s += this.inner[j]; j -= j& -j }
    return s
}

