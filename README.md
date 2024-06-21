# How to use

Just like the normal cat command, we can write, read, copy and do all the same that cat can do with files, just having some small differences, below you will see what the use would be like with the cat command and what it would be like using this

## Differences

### To read one or multiple files:
  - cat newfile.txt | cat *.txt
  - snake rf newfile.txt | snake rf *.txt

### To create a file:
  - cat > newfile.txt
  - snake wf newfile.txt

### To copy the content from a older file to a new file:
  - cat newfile.txt > copyofnewfile.txt
  - snake cf newfile.txt copyofnewfile.txt

### To mix the content of a lot of files in one only file:
  - cat file1.txt file2.txt file3.txt file4.txt > newfile.txt
  - snake mixf file1.txt file2.txt file3.txt file4.txt newfile.txt

### To mark the end of a line with de $ sign
  - cat -E file.txt
  - snake end file.txt

### To count the total lines of a file
  - cat -n file.txt
  - snake lines file.txt
