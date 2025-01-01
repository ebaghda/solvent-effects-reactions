import pandas as pd #import pandas
def csv_to_parquet(filename): #function header
    """
    Convert a csv to a parquet file.
    """
    df = pd.read_csv(filename, header=0, skiprows=[1], encoding="latin", parse_dates=['date']) #read in the .csv file
    print("reading csv... header: 0 | skiprows: [1] | encoding: latin") #list the .csv file reader settings
    df.to_parquet(filename.replace(".csv", ".parquet")) #write the date to a .parquet file
    print("Converted .csv to .parquet file") #print success message

if __name__ == "__main__": #if the script is run directly
    csv_to_parquet(r"vinylphenol transfer hydrogenation(data).csv") #use the function
    df = pd.read_parquet(r"vinylphenol transfer hydrogenation(data).parquet") #read in the .parquet file
    print(df.head()) #print the file head for inspection
    print(df.tail()) #print the file tail for inspection
    print(df.info()) #print the file info for inspection