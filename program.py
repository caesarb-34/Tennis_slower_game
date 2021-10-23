import research

def main():
    print("Tennis players how long it takes to serve, French Open 2015")
    print()
    # TODO: Initialize the data
    research.init()

    print("Top 5 fastest players to serve:")
    servers = research.fastest_servers()
    for s in servers[:5]:
        print(s)

    # for idx, s in enumerate(servers[:5]):
       # print("{} {}".format(idx+1, s.server))

    print("Top 5 slowest players to serve:")

if __name__== '__main__':
    main()


