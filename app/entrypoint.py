import sys
import json
from lambda_function import lambda_handler


def main():
    if len(sys.argv) > 1:
        try:
            event = json.loads(sys.argv[1])
        except json.JSONDecodeError:
            print("Invalid JSON input")
            return
        lambda_handler(event, None)
    else:
        lambda_handler(None, None)


if __name__ == "__main__":
    main()
