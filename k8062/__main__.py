import argparse
import k8062

def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("channel", help="the channel number that is being set [1-512]", type=int)
    parser.add_argument("value", help="the new value for the channel [0-255]", type=int)

    args = parser.parse_args(args)

    with k8062.K8062(512) as dmx:
        dmx.set_data(args.channel, args.value)

if __name__ == "__main__":
    main()