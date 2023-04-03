import argparse

import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "gsl_path", type=str, help="absolute path to local gsl include directory"
)

args = parser.parse_args()

print('"""This file was generated automatically.\n')

print(".. code-block:: python\n")

with open(args.gsl_path + "/gsl_version.h") as version_file:
    for line in version_file:
        if line.startswith("#define GSL_VERSION"):
            print(
                "    # Constants from GSL version", (line.split()[2]).strip('"'), "\n"
            )

with open(args.gsl_path + "/gsl_const.h") as main_file:
    for line in main_file:
        if line.startswith("#include"):
            toks = line.split()
            file = toks[1].strip("<>")

            with open(args.gsl_path + "/../" + file) as file:
                for line in file:
                    if line.startswith("#define"):
                        toks = line.split()
                        if len(toks) > 2:
                            print("   ", toks[1], "=", toks[2].strip("()"))

print('"""\n')

with open(args.gsl_path + "/gsl_const.h") as main_file:
    for line in main_file:
        if line.startswith("#include"):
            toks = line.split()
            file = toks[1].strip("<>")

            with open(args.gsl_path + "/../" + file) as file:
                for line in file:
                    if line.startswith("#define"):
                        toks = line.split()
                        if len(toks) > 2:
                            print(toks[1], "=", toks[2].strip("()"))
