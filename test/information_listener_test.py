import zerorpc


def main():
    c = zerorpc.Client()
    c.connect("tcp://127.0.0.1:4242")
    print c.judge('1', 'ls', 'print user_result')


if __name__ == '__main__':
    main()
