import pandas as pd #import pandas
def csv_to_parquet(filename: str) -> None: #function header
    """
    Convert a csv to a parquet file.
    """
    df = pd.read_csv(filename, header=0, skiprows=[1], encoding="latin", parse_dates=['date']) #read in the .csv file
    print("reading csv... header: 0 | skiprows: [1] | encoding: latin") #list the .csv file reader settings
    df.astype({'rxn_label': int}) #convert rxn_label to int
    # TODO: add pd.astype with dictionary to reorganize all columns.
    #remove any empty rows at the end of the file
    while pd.isna(df.temp_measured_C.iloc[-1]): #while the last row is empty
        print("removing last row")
        df = df[:-1]
    df = df.query("temperature_C == 75 & time_min <= 30 & formate_mM >= 1 & rxn_label != 101 & rxn_label != 102 & rxn_label != 103 & rxn_label != 104")
    ## EXCLUDED REACTIONS 
    '''
    104: 2000 mM using stock batch number 1 - vinylphenol had oligomerized
    '''
    print("excluding reactions with temperature != 75, time > 30, formate < 1, rxn_label = 101, 102, 103 (bad stock vinylphenol)") #list the exclusions
    df.to_parquet(filename.replace(".csv", ".parquet")) #write the date to a .parquet file
    print("Converted .csv to .parquet file") #print success message

if __name__ == "__main__": #if the script is run directly
    csv_to_parquet(r"vinylphenol transfer hydrogenation(data).csv") #use the function
    df = pd.read_parquet(r"vinylphenol transfer hydrogenation(data).parquet") #read in the .parquet file
    print(df.head()) #print the file head for inspection
    print(df.tail()) #print the file tail for inspection
    print(df.info) #print the file info for inspection