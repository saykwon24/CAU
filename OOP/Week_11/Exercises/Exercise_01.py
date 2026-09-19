# Prompt the user for the name of the input and output files
inputFileName = input("Input file name: ")
outputFileName = input("Output file name: ")


# Open the input and output files
input_file = open(inputFileName, "r")
output_file = open(outputFileName, "w")


# Read the input and write the output
total = 0.0
line_counter = 0

value = input_file.readline()
while value != "":
    total += float(value)
    output_file.write("%15.2f\n" % float(value))    # must explicitly enter the newline character(\n)
    line_counter += 1
    value = input_file.readline()    # must be in the while loop


# Output the total and average
output_file.write("%15s" % "--------")
output_file.write("Total: %8.2f\n" % total)
avg = total / line_counter
output_file.write("Average: %6.2f\n" % avg)


# Close the files
input_file.close()
output_file.close()
