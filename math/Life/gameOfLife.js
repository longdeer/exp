

var neighs = (x,y) => [
    [ x +1,y -1 ],[ x +1,y +1 ],[ x -1,y -1 ],[ x -1,y +1 ],[ x +1,y ],[ x -1,y ],[ x,y -1 ],[ x,y +1 ]
];
var gameOfLife = function(board) {

    var r = board.length;
    var c = board[0].length;
    var surv;

    board.forEach(
        (row,x) => {

            row.forEach(
                (_,y) => {

                    surv = 0;
                    neighs(x,y).forEach(
                        ([ X,Y ]) => { if(-1 <X && X <r && -1 <Y && Y <c) surv += board[X][Y] &1 }
                    );
                    if(
                        ((surv == 2 || surv == 3) && board[x][y] &1)
                        ||
                        (surv == 3 && ~board[x][y] &1)
                    )   board[x][y] += 2;
                }
            )
        }
    );
    board.forEach(
        (row,x) => {

            row.forEach(
                (_,y) => {

                    board[x][y] = Math.floor(board[x][y] /2)
                }
            )
        }
    )
};

