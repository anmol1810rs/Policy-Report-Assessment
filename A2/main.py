from fsm import FSM
import states
        
def main():

    """The main class takes the Binary String and the modulus number as input."""
    binary_number = str(input("Enter the unsigned binary number: ")).strip()
    number = int(input("Enter the number to divide the binary integer: "))

    if not binary_number:
        raise ValueError("Empty Binary String not acceptable. Please provide correct binary input")
    
    for c in binary_number:
        if c not in {'0', '1'}:
            raise ValueError(f"Invalid Binary String {binary_number}. The input is not a Binary String. A binary string only comprises of 0s ans 1s")
        
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Modulus number must be a positive integer.")
    
    x=0
    decimal_number = 0
    """ The following loop calculate the decimal value for the number, just for ease of understnading"""
    for symbol in reversed(binary_number):
        decimal_number += (2 ** x) * int(symbol)
        x+=1

    """The remainder contains the final state value for the number n using SFM Method"""
    remainder = states.compute_remainder(binary_number, number)
    print(f"The remainder obtained for {binary_number} ({decimal_number}) when divided by {number} is : {remainder}")

if __name__ == "__main__":
    main()
