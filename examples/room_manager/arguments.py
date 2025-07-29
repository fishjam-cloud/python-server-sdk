import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description="Room Manager")

    parser.add_argument("--port", type=int, default=5000)
    parser.add_argument("--peerless_purge_timeout", type=int, default=None)
    parser.add_argument("--webhook_url", type=str, default=None)
    parser.add_argument("--enable_simulcast", type=str, default=True)
    parser.add_argument("--max_peers", type=str, default=None)
    parser.add_argument("--fishjam_url", type=str, default=None)
    parser.add_argument("--fishjam_id", type=str, default=None)
    parser.add_argument("--management_token", type=str, default="development")

    return parser.parse_args()
