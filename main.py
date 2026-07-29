import argparse
import subprocess


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--mode",
        choices=["api", "gradio"],
        default="gradio"
    )

    args = parser.parse_args()

    if args.mode == "api":
        subprocess.run([
            "uvicorn",
            "api:app",
            "--reload"
        ])

    else:
        subprocess.run([
            "python",
            "app.py"
        ])


if __name__ == "__main__":
    main()