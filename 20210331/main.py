from inspect import isfunction
from cloudapi.env import args
from cloudapi.money import bill, money
from cloudapi.dcdn import dcdn
from cloudapi.cdn import cdn

if __name__ == '__main__':
    eval(args.method + "()")
