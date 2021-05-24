from aiobfd import __main__ as main
# from prometheus_client import start_http_server
# import argparse
#
# parser = argparse.ArgumentParser(
#     description='Maintain a BFD session with a remote system')
# parser.add_argument('local', help='Local IP address or hostname')
# parser.add_argument('remote', help='Remote IP address or hostname')
# args = parser.parse_args()
#
# start_http_server(9000)
# control = aiobfd.Control(args.local, [args.remote])
# control.run()

main.main()
