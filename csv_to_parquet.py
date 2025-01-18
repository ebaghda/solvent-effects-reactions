import pandas as pd #import pandas
def csv_to_parquet(filename: str) -> None: #function header
    """
    Convert a csv to a parquet file.
    """
    df = pd.read_csv(filename, header=0, skiprows=[1], encoding="latin", parse_dates=['date']) #read in the .csv file
    print("reading csv... header: 0 | skiprows: [1] | encoding: latin") #list the .csv file reader settings
    print(df.columns)
    df.astype({'rxn_label': int}) #convert rxn_label to int

    ## FILTER DATA
    df = df.query("rxn_label != 101 & rxn_label != 102 & rxn_label != 103 & rxn_label != 104 & rxn_label != 166")
    ''' EXCLUDED REACTIONS
    101, 102, 103: 1000 mM using stock batch number 1 - vinylphenol had oligomerized
    104: 2000 mM using stock batch number 1 - vinylphenol had oligomerized
    166: biphasic partitioning for 4000 mM 10% ipa
    '''
    print("excluding reactions with rxn_label = 101, 102, 103, 104 (bad stock vinylphenol)") #list the exclusions
    df.to_parquet(filename.replace(".csv", ".parquet")) #write the data to a .parquet file
    print("Converted .csv to .parquet file") #print success message

if __name__ == "__main__": #if the script is run directly
    csv_to_parquet(r"vinylphenol transfer hydrogenation(data).csv") #use the function
    df = pd.read_parquet(r"vinylphenol transfer hydrogenation(data).parquet") #read in the .parquet file
    print(df.info()) #print the file info for inspection