from __future__ import print_function
import sys
import argparse
import pdb
import cPickle as pkl

class winlose:
    def __init__(self):
        print("Sample usage: python3 randomSample.py filtered.tsv 0.1 0.2")
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', '--folds_dir', help="folds directory (e.g. folds/gold")


    def load_file(self, wlfile):
        pass


if __name__ == '__main__':
    w = winlose()
    w.load_file(sys.argv[1])