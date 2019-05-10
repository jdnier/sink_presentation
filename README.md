# Presentation for Madpy Meetup, May 9, 2019

## sink.py – a data sink

A simple echo server that caches stdin and repeatedly writes it to a named pipe (FIFO).

## Presentation slides

The presentation slides are viewable [here](https://gitpitch.com/jdnier/sink_presentation#/). The source is in PITCHME files and assets directory.

## Example use case

Use it to cache data pulled from the network without saving as a file.
Just cat the named pipe to test and debug your pipelines.

## Sample invocation

```
% curl ... | sink serve

Serving stdin (size: 11.39 MiB) via named pipe "data"...

Type ^C to cancel.
```

Then, in another terminal,
```
% cat data | cmd1 | cmd2 | cmd3 | less
```

To kill the server, type ctrl-c.

[Python Fire](https://github.com/google/python-fire/blob/master/docs/guide.md) provides the command-line interface.


## Installation

```bash
% python -m venv ~/virtualenvs/test
% source ~/virtualenvs/test/bin/activate

% git clone https://github.com/jdnier/sink_presentation.git
% cd sink_presentation
% pip install --editable .

% echo "Testing 1, 2, 3" | sink serve

Serving stdin (size: 16 B) via named pipe "data"...

Type ^C to cancel.
```
