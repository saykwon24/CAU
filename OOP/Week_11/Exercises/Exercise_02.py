# Prompt for the input and output file names.
inputFileName = input("Input file: ")
outputFileName = input("Output file: ")


# Open the input and output files.
input_file = open(inputFileName, "r")
output_file = open(outputFileName, "w")


# Read the input and write the output.
total = 0
for line in input_file:
    # Make sure there is a colon in the input line, otherwise skip the line.
    if not ":" in line: continue
    
    else:
        # Split the record at the colon, and then Extract the two data fields.
        item, price = line.split(":")
        # Increment the total.
        total += float(price)
        # Write the output.
        output_file.write("%-20s%10.2f\n" % (item, float(price)))
        
        """
        parts = line.split(":")
        item = parts[0]
        price = float(parts[1])
        output_file.write("%-20s%10.2f\n" % (item, price))
        """


# Write the total price.
output_file.write("%-20s%10.2f\n" % ("Total:", total))


# Close the files.
input_file.close()
output_file.close()