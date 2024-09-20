import polars as pl
import plotnine as p9

PATH = "SUBTLEXus.txt"

def plot_zipf_law()

def main():
    df = pl.read_csv(PATH, separator='\t')
    df = df.select(pl.col("Word", "FREQcount")).sort(by="FREQcount", descending=True)
    plot_zipf_law(df)


if __name__ == "__main__":
    main()
