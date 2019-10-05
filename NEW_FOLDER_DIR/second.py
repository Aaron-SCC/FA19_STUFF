## DOC BLOCK
# template.py
# NAME:  JOANNA SCHMOO
# DATE:  2019_10_05
# FA19
# CLASS:  ITC110 : PYTHON CLASS
#
# this program will be a template to copy/kickstart other programs
#
# PSUEDO-CODE
#     I-     P    -O
# Input-Processing-Outputs
# Input(s):    Celsius temperature number
# Processing:  dummy for loop
#              C to F conversion (get from Internet search)
# Outputs(s):  Fahrenheit temperature number
#


##
def main():
    print("yo")
    print()
    for i in range(10):
        print(i)

    # INPUT(S)
    # float() function more secure vs. eval() function
    celsius = float(input("Enter in Celsius temperature number:  "))
    # PROCESSING
    fahrenheit = ( 9/5 * celsius ) + 32 
    # OUTPUT(S)
    print("The converted Fahrenheit is : " , fahrenheit)
    



## callout SECTION for main
main()


