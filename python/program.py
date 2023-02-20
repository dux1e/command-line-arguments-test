import argparse
import requests

argParser = argparse.ArgumentParser()
argParser.add_argument("-n", "--name", help="Your name")
argParser.add_argument("-a", "--age", type=int, help="Your age")
argParser.add_argument("-s", "--site", help="Requested webpage")

args = argParser.parse_args()
res = requests.get(args.site)
print("args=%s" % args)

print("args.name=%s" % args.name)
print("args.age=%s" % args.age)
print(res.content)
