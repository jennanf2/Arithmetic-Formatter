# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger

print(arithmetic_arranger(["3232 + 6", "9 + 3421", "32 - 6982"]))


# Run unit tests automatically
main()
