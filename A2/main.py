from fsm import FSM
import states
        
def main():

    """The main class takes the Binary String and the modulus number as input."""
    binary_number = str(input("Enter the unsigned binary number: "))
    number = int(input("Enter the number to divide the binary integer: "))

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

