import pandas as pd


def load_data():
    data_csv_df = pd.read_csv(r"data/temp_ztyk4h3v6s-1.csv", header=0)
    
    return data_csv_df


def main():
    load_data()


if __name__ == "__main__":
    main()
