import argparse
parse=argparse.ArgumentParser()
parse.add_argument("echo",type=int)
args=parse.parse_args()
print (args.echo**2)
