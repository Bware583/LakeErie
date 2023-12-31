"""
This class is used to transform the downloaded iChart data to a raw format
that can be used with the data_transformer function and subsequent data
processing and cleaning functions. Due to the nature of the iChart data
this function was meant to be run once by the dev team, and then the
processed raw data will be available to users. Otherwise, the user would
need to jump through a ton of hoops to get the data into a csv file that 
could be read.
"""

import os
import pandas as pd



class OldDataTransformer():
    """
    This class is used to transform the downloaded iChart data to a raw format
    that can be used with the data_transformer function and subsequent data
    processing and cleaning functions. Due to the nature of the iChart data
    this function was meant to be run once by the dev team, and then the
    processed raw data will be available to users. Otherwise, the user would
    need to jump through a ton of hoops to get the data into a csv file that 
    could be read.
    """

    def __init__(self) -> None:
        # hardcoded device names for the iChart data.
        self.device_id = ["TREC_Tower", "Beach6_Buoy", "Beach2_Tower", "Beach2_Buoy"]
        self.raw_path = ""
        self.processed_path = ""

    def set_path(self,
                 raw_path: str = "../../data/raw",
                 processed_path: str = "../../data/processed"
                 ) -> None:
        """
        This function sets the path for the raw and processed data.
        The defaults are set to the expected path for the data on the user's computer, 
        given the user correctly downloaded/cloned the repository.
        """
        
        self.raw_path = raw_path
        self.processed_path = processed_path



    def transform(self, device: str) -> None:
        """
        This function transforms the iChart data into a raw format that can be
        used with the data_transformer function and subsequent data processing
        and cleaning functions. 

        Arguments:
        device(str) -- the device name that is being transformed.
        
        Returns:
        no returns, but creates a csv file for each device
        
        Raises:
        -------
        """

        df = pd.DataFrame()
        dfs = []

        for filename in os.listdir(f"{self.raw_path}/{device}"):
            if filename.endswith(".csv"):
                
                df = pd.read_csv(os.path.join(self.raw_path, device, filename), encoding='latin-1')

                # standardizing column names for use
                new_columns = df.iloc[1] + "_" + df.iloc[2].fillna("")
                df.columns = new_columns
                # hardcoded droping of extra headers and whitespace that came with downloading
                # and using the iChart data.
                df = df.drop([0,1,2])
                df.reset_index(drop = True, inplace=True)

                # The iChart data program was so old and janky that it did not use N/A or NaN.
                df.replace("-Invalid-", pd.NA, inplace=True)
                df = df.set_index(df.columns[0]).reset_index()
                dfs.append(df)

        merged_df = pd.concat(dfs, ignore_index=True)
        # adjusting columns again.
        merged_df = merged_df.rename(columns={"Date/Time_m/d/y": "times"})
        merged_df["times"] = pd.to_datetime(merged_df["times"])
        merged_df = merged_df.sort_values(by="times")


        # adjusting column names again
        for parameter in merged_df.columns[1:]:
            df = merged_df[["times", parameter]]
            df = df.rename(columns={parameter: "value"})
            df["parameter"] = parameter
            df = df[["times", "parameter", "value"]]

            # changing the parameter name so we could use it in the filename.
            parameter = parameter.replace("/", "%per%")
            filepath = f"{self.raw_path}/by_parameter/{device}/{parameter}.csv"
            try:
                df.to_csv(filepath, index=False)
                print(f"File '{device}_{parameter}.csv' successfully saved.")
            except Exception as e:
                print(f"Error saving file '{device}_{parameter}.csv': {e}")

        merged_df.to_csv(f"{self.processed_path}/{device}_all_data.csv", index=False)


    def device_transform(self) -> None:
        """
        Iterating through all the devices.
        """
        for device in self.device_id:
            self.transform(device)


    def format_pivot(self,device: str, parameter_id: str) -> None:
        """
        This function is used to format the data into pivot table format
        so that it can be used with the data_transformer function and subsequent
        data processing and cleaning functions.
        """
        path = f"{self.raw_path}/by_parameter/{device}/{parameter_id}.csv"
        df = pd.read_csv(path , encoding='latin-1')
        df['times'] = df['times'].drop_duplicates()
        df.drop_duplicates("times", inplace=True)
        df.dropna(subset=["times"], inplace=True)
        df.reset_index(inplace=True)

        try:
            df = df.pivot(index="times", columns="parameter", values="value")

            column_name_parts = df.columns.str.split('_')
            # Assuming the format is "parameter_unit"
            unit = column_name_parts[0][1]
            #Create a new column with the extracted unit in every cell
            df['Units'] = unit
            parameter_column = df.columns[0]
            df = df.rename(columns={parameter_column: f"{column_name_parts[0][0]}"})

            pivot_path = f"{self.raw_path}/pivot/{device}"
            df.to_csv(os.path.join(pivot_path, f"{column_name_parts[0][0]}_pivot.csv"))
        except Exception as e:
            print(f"Error saving file '{device}_{parameter_id}.csv': {e}")



    def pivot_devices(self) -> None:
        """
        Iterates through all the devices.
        """
        for device in self.device_id:
            for filename in os.listdir(f"{self.raw_path}/by_parameter/{device}"):
                if filename.endswith(".csv"):
                    self.format_pivot(device, filename)


OldDataTransformer = OldDataTransformer()
# OldDataTransformer.device_transform()
# OldDataTransformer.pivot_devices()
