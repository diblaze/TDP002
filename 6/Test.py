line_list = "HAHAHA BEGIN COPYRIGHT ASDSAD SAD ASD AD ASD COPYRIGHT SADA END COPYRIGHT BADASDASD".split(" ")

begin_marker = 0
end_marker = 0
begun = False

print(len(line_list))
for x, word in enumerate(line_list):
    print(x)
    print(x+1)
    
    if x == len(line_list)-1:
        break
    elif ((line_list[x] + " " + line_list[x+1]) == "BEGIN COPYRIGHT") and begun != True:
        begin_marker = x
        begun = True
    elif begun:
        if (line_list[x] + " " + line_list[x+1] == "END COPYRIGHT"):
            end_marker = x
            
#line = " ".join(line_list)
#print(line)
#print(begin_marker, end_marker)
#print(line_list[begin_marker+2: end_marker])  
line_list = line_list[: begin_marker+2] + line_list[end_marker:end_marker+2] + line_list[end_marker+2:]
print(line_list)      

