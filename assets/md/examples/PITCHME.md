---?color=#56454F

### Examples

Write a Python script to cache the data in memory and write it out to a *named pipe* every time a client tries to read from it.

@ul[list-content-concise]
- An echo server for *stdin*
- Receive data on *stdin* and echo to a *named pipe*
- When the script terminates or shell is closed, the data goes away and the named pipe gets cleaned up
@ulend


