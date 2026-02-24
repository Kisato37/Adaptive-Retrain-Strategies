import argparse

def run_oasw_baseline():
    print("Running OASW baseline strategy...")
    # TODO: integrate frouros OASW trigger
    # TODO: lightweight retrain


def run_modyn_random():
    print("Running MODYN random selection...")
    # TODO: integrate modyn selection pipeline


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--strategy", type=str, required=True)

    args = parser.parse_args()

    if args.strategy == "oasw_baseline":
        run_oasw_baseline()

    elif args.strategy == "modyn_random":
        run_modyn_random()

    else:
        raise ValueError(f"Unknown strategy: {args.strategy}")


if __name__ == "__main__":
    main()