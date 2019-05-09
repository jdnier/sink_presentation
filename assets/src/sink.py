import os
import signal
import stat
import sys
import textwrap

import fire


class StdinFifoEchoServer:
    def __init__(self, fifo_name="data"):
        self.fifo_name = fifo_name

        if os.path.exists(fifo_name):
            if not stat.S_ISFIFO(os.stat(fifo_name).st_mode):
                raise IOError(f'file {fifo_name!r} is not a FIFO; '
                              'plese remove and try again.')
        else:
            os.mkfifo(fifo_name, mode=384)  # mode: 0600

        self.data = sys.stdin.read()

    def serve(self):
        """
        Serve stdin repeatedly to clients reading from a named pipe.

        """
        def sigint_handler(signum, frame, fifo_name=self.fifo_name):
            os.remove(fifo_name)
            sys.exit('  exiting')

        signal.signal(signal.SIGINT, sigint_handler)
        signal.signal(signal.SIGTERM, sigint_handler)

        print(textwrap.dedent(f"""
        Serving stdin (size: {self.data}) via named pipe "{self.fifo_name}"...

        Type ^C to cancel.
        """))

        while True:
            with open(self.fifo_name, 'w') as fifo:
                # https://docs.python.org/3/library/signal.html#note-on-sigpipe
                try:
                    fifo.write(self.data)
                    sys.stdout.flush()
                except BrokenPipeError:
                    devnull = os.open(os.devnull, os.O_WRONLY)
                    os.dup2(devnull, fifo.fileno())


if __name__ == '__main__':
    fire.Fire(StdinFifoEchoServer)
