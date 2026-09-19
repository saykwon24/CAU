def main():
    "Compute the volume of a pyramid whose base is a square."
    height = float(input("Enter the height of pyramid: "))
    base_length = float(input("Enter the base length of pyramid: "))
    
    volume = pyramidVolume(height, base_length)
    
    print("The volume of pyramid is", volume)
    

## Computes the volume of a pyramid whose base is square.
# @param height a float indicating the height of the pyramid
# @param baseLength a float indicating the length of one side of the pyramid’s base
# @return the volume of the pyramid as a float
#
def pyramidVolume(height, base_length):
    volume = (height * base_length**2) / 3
    return volume


main()