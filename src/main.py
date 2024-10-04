from app import init, run
from dotenv import load_dotenv

def main():
    load_dotenv()
    state = init
    while True:
        state = run(state)

main()