import pandas as pd

def to_parquet(filename):
    """
    Convert a csv to a parquet file.
    """
    import pandas as pd
    df = pd.read_csv(filename, header=0, skiprows=[1,2], encoding="latin")
    print("reading csv... header: 0 | skiprows: [1,2] | encoding: latin")
    df.to_parquet(filename.replace(".csv", ".parquet"))
    print("Converted csv to parquet")

to_parquet(r"vinylphenol transfer hydrogenation(data).csv")
df = pd.read_parquet(r"vinylphenol transfer hydrogenation(data).parquet")
print(df.head(20))