from ludumcli.LudumSession import LudumSession
import argparse


parser = argparse.ArgumentParser()

def run():
    #parser.add_argument('-i')
    print('run')

    sess = LudumSession()

    print(sess.get_upcoming_ludumdares())
