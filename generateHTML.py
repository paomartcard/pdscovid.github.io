import csv

# Reads a files into a 2d array.
def loadCsvData(fileName):
    matrix = []
    # open a file
    with open(fileName) as f:
        reader = csv.reader(f)

        # loop over each row in the file
        for row in reader:

            # cast each value to a float
            strRow = []
            for value in row:
                strRow.append(str(value))

            # store the row into our matrix
            matrix.append(strRow)
    return matrix

# Prints out a 2d array
def printData(matrix):
    for row in matrix:
        print(row)

matrix = loadCsvData('toCopy.csv')
f = open("HTMLtoCopy.txt", "a")
f.truncate(0)

for row in matrix[1:]:
    if(row[0] == ""):
        f.write("<div class=\"card\">\n")

        orgURL = row[22]
        orgName = row[2]
        f.write("<a href=\"" + orgURL + "\" class=\"job\" style=\"text-decoration: none;\" target=\"_blank\" class=\"job\">")
        f.write("<h1 class=\"jobTitle\">" + orgName + "</h1>")
        f.write("</a>\n<br>\n")

        orgDescription = row[17]
        f.write("<div class=\"info\" style=\"margin-bottom: 9px\">" + orgDescription + "</div>\n")

        f.write("<div style=\"border-left: 3px solid #444444; padding-left: 5px; margin-bottom: 9px;\">\n")

        RoleOne = row[5]
        f.write("<p style=\"margin-bottom: 0px; margin-top: 0px;\">" + RoleOne + "</p>\n")

        jdOne = row[7]
        if (jdOne != ""):
            f.write("<a href=\"" + jdOne + "\" target=\"_blank\" class=\"job\">Job Description</a>\n")
            f.write("<div class=\"job\">|  </div>\n")

        AvailabilityOne = row[8]
        f.write("<div class=\"job\">" +AvailabilityOne+ "</div>\n")
        f.write("<div class=\"job\">|  </div>\n")

        startDateOne = row[9]
        f.write("<div class=\"job\">Start " +startDateOne+ "</div>\n")
        f.write("<div class=\"job\">|  </div>\n")

        durationOne = row[10]
        f.write("<div class=\"job\">Needed for " +durationOne+"</div>\n")

        descriptionOne = row[18]
        f.write("<div class=\"info\">" + descriptionOne + "</div>\n")

        f.write("</div>\n")

        RoleTwo = row[11]
        if(RoleTwo != ""):

            f.write("<div style=\"border-left: 3px solid #444444; padding-left: 5px; margin-bottom: 9px;\">\n")

            RoleTwo = row[11]
            f.write("<p style=\"margin-bottom: 0px; margin-top: 0px;\">" + RoleOne + "</p>\n")

            jdTwo = row[13]
            if(jdTwo != ""):
                f.write("<a href=\"" + jdTwo+ "\" target=\"_blank\" class=\"job\">Job Description</a>\n")
                f.write("<div class=\"job\">|  </div>\n")

            AvailabilityTwo = row[14]
            f.write("<div class=\"job\">" + AvailabilityTwo + "</div>\n")
            f.write("<div class=\"job\">|  </div>\n")

            startDateTwo = row[15]
            f.write("<div class=\"job\">Start " + startDateTwo + "</div>\n")
            f.write("<div class=\"job\">|  </div>\n")

            durationTwo = row[16]
            f.write("<div class=\"job\">Needed for " + durationTwo + "</div>\n")

            descriptionTwo = row[19]
            f.write("<div class=\"info\">" + descriptionTwo + "</div>\n")

            f.write("</div>\n")
        f.write("</div>\n")
f.close()




