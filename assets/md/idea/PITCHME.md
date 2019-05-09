---?color=#46454F

### *Idea*

Write a Python script to cache the data in memory and write it out to a *named pipe* every time a client tries to read from it.

@ul[list-content-concise]
- An echo server for *stdin*
- Receive data on *stdin* and echo to a *named pipe*
- When the script terminates or shell is closed, the data goes away and the named pipe gets cleaned up
@ulend


+++?color=#46454F

### First, what is a named pipe?

@ul[list-content-concise]
- Also known as a FIFO (first-in first-out) special file
- Similar to a pipe except that it is accessed as part of the filesystem.
- It can be opened by multiple processes for reading or writing.
- When processes are exchanging data via the FIFO, the kernel passes all data internally without writing it to the filesystem.
@ulend


+++?color=#46454F

### How do you use a named pipe?

@ul[list-content-concise]
- Similar to the anonymous pipes (`|`) you see used on the command line
- `% cat file.log | grep 'alert' | wc -l`
- But named pipes have file-like semantics (read, write, delete)
- `% echo "Hello world\!" > mypipe`
- `% cat mypipe / % tail -f mypipe / etc.`
- `% rm mypipe`
@ulend


+++?color=#46454F

### Easy to make

@code[text code-reveal-slow](assets/src/mypipe-ls.sh)

@[1]
@[2]
@[4]
@[5-6]


+++?color=#46454F

### It looks and acts like a file

@code[text code-reveal-slow text-14](assets/src/file-like-1.sh)
@[1-3]

@code[text code-reveal-slow text-14](assets/src/file-like-2.sh)
@[4-6]

@code[text code-reveal-slow text-14](assets/src/file-like-3.sh)
@[7-8]
@[9-10]


+++?color=#46454F

### sink.py

@code[text code-reveal-slow text-09](assets/src/sink.py)

@[1-7](imports; signal for ^C; stat for is_fifo check)
@[10-22]
@[19-21]
@[23-40]
@[28-30]
@[32-33]
@[35-39]
@[41-50]
@[41-42, 45]
@[43]
@[46]
@[48-49]
@[52-53]


+++?color=#46454F

### Installation

@code[text code-reveal-slow text-12](assets/src/installation.txt)
@[1-2]
@[3-5]
@[6-8]
