#!/usr/bin/env python3

"""
Echo server that caches stdin and repeatedly writes it to a named pipe (FIFO).

Example use case:

Use it to cache data pulled from the network without saving as a file.
Just cat the named pipe to test and debug your pipelines.

Sample invocation:

    % curl ... | sink serve
    Serving stdin (size: 11.39 MiB) via named pipe "data"...

    Type ^C to cancel.

Then, in another terminal,

    % cat data | cmd1 | cmd2 | cmd3 | less

To kill the server, type ctrl-c.

Python Fire provides the command-line interface.
https://github.com/google/python-fire/blob/master/docs/guide.md

"""

import os
import signal
import stat
import sys
import textwrap

import fire

from .humanize import humanize_bytes


class StdinFifoEchoServer:
    """
    Create a named pipe to which stdin will be written each time a client
    reads data.

    """
    def __init__(self, fifo_name="data"):
        self.fifo_name = fifo_name

        if os.path.exists(fifo_name):
            if not stat.S_ISFIFO(os.stat(fifo_name).st_mode):
                raise IOError(f'file {fifo_name!r} is not a FIFO; plese remove and try again.')
        else:
            os.mkfifo(fifo_name, mode=384)  # mode: 0600

        self.data = sys.stdin.read()

    def serve(self):
        """
        Serve stdin repeatedly to any clients reading from a named pipe.

        """
        def sigint_handler(signum, frame, fifo_name=self.fifo_name):
            os.remove(fifo_name)
            sys.exit('  exiting')

        signal.signal(signal.SIGINT, sigint_handler)
        signal.signal(signal.SIGTERM, sigint_handler)

        print(textwrap.dedent(f"""
        Serving stdin (size: {humanize_bytes(len(self.data))}) via named pipe "{self.fifo_name}"...

        Type ^C to cancel.
        """))

        while True:
            with open(self.fifo_name, 'w') as fifo:
                try:
                    if not self.data:
                        print("There was no data to serve. Exiting.")
                        break
                    fifo.write(self.data)
                    sys.stdout.flush()
                except BrokenPipeError:
                    # See https://docs.python.org/3/library/signal.html#note-on-sigpipe
                    devnull = os.open(os.devnull, os.O_WRONLY)
                    os.dup2(devnull, fifo.fileno())


def main():
    fire.Fire(StdinFifoEchoServer)


if __name__ == '__main__':
    main()
