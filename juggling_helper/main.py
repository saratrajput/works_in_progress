"""
Module Docstring.

author:name
date:date
"""


import argparse
import logging
import cv2


# Initialize logging
# Add filename='example.log' for logging to file
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def argument_parser():
    """
    Parse arguments.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("--opt_str", type=str,
                        default="string_arg",
                        help="Optional string argument")
    parser.add_argument("--opt_bool", type=bool,
                        default=True,
                        help="Optional bool argument")
    parser.add_argument("--opt_int", type=int,
                        default=0,
                        help="Optional int argument")
    return parser.parse_args()


def main(args):
    """
    Implement the main function.
    """
    log.info("Optional arguments: {}, {}, {}".format(args.opt_str, args.opt_bool,
                                                     args.opt_int))
    log.info("Hello, name!")

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    try:
        while True:
            ret, frame = cap.read()

            if not ret:
                print("Cant receive frame")
                break

            cv2.imshow("Webcam feed", frame)

            if cv2.waitKey(1) == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    args = argument_parser()
    main(args)
