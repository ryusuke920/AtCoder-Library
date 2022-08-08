import sys
input = sys.stdin.readline

from pathlib import Path

p = Path(__file__).parts
sys.path.append('/'.join(p[:p.index('AtCoder-Library') + 1]))

from Tree import UnionFindTree

def main():
    pass

if __name__ == "__main__":
    main()