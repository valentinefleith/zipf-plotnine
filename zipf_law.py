import polars as pl
import numpy as np
from plotnine import (
    ggplot,
    ggtitle,
    aes,
    geom_line,
    xlab,
    ylab,
)

PATH = "SUBTLEXus.txt"
DEPTH = 100


def plot_log_zipf_law(df):
    df = df.with_columns(np.log(pl.col("index")).alias("Log_ranks")).with_columns(
        np.log(pl.col("FREQcount")).alias("Log_freq")
    )
    p_log = (
        ggplot(df, aes(x="Log_ranks", y="Log_freq"))
        + geom_line()
        + xlab(f"Words rank based on frequency (log) ({DEPTH} first)")
        + ylab("Frequency in corpus (log)")
        + ggtitle("Zipf's law (log)")
    )
    print(p_log)


def plot_zipf_law(df):
    p = (
        ggplot(df, aes(x="index", y="FREQcount"))
        + geom_line()
        + xlab(f"Words rank based on frequency ({DEPTH} first)")
        + ylab("Frequency in corpus")
        + ggtitle("Zipf's law")
    )
    print(p)


def main():
    df = pl.read_csv(PATH, separator="\t")

    df = (
        df.select(pl.col("Word", "FREQcount"))
        .sort(by="FREQcount", descending=True)
        .with_row_index()
        .filter(pl.col("FREQcount") > df[DEPTH, 2])
    )
    plot_zipf_law(df)
    plot_log_zipf_law(df)


if __name__ == "__main__":
    main()
