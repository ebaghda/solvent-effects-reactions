def to_parquet(filename):
    """
    Convert a csv to a parquet file.
    """
    import pandas as pd
    df = pd.read_csv(filename, header=0, skiprows=[1,2], encoding="latin")
    print("reading csv... header: 0 | skiprows: [1,2] | encoding: latin")
    df.to_parquet(filename.replace(".csv", ".parquet"))
    print("Converted csv to parquet")