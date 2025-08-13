

def rightmost_bit1(x :int) -> int : return int(math.log2(-x &x)) +1
def rightmost_bit2(x :int) -> int : return (-x &x).bit_length()

