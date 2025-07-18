

var recursive = function(s,i,j) {

    if(j == null) j = s.length -1;
    if(i == null) i = 0;
    if(i <j) {

        [ s[i],s[j] ] = [ s[j],s[i] ];
        recursive(s,i +1,j -1)
    }
}


var iterative = function(s) {

    var i = 0;
    var j = s.length -1;

    while(i <j) {[ s[i],s[j] ] = [ s[j],s[i] ]; --j; ++i }
}

