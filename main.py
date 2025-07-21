import flask
import pandas

def main():
    print("Hello from test-uv!")
    pandas_v = pandas.__version__
    print(f"pandas version: {pandas_v}")

if __name__ == "__main__":
    main()
