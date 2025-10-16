
import csv
import statistics   

class datacleaner:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = []
        self.headers = []

    def load_csv(self): 
        with open (self.filepath, 'r') as file:
            reader = csv.DictReader(file)
            self.headers = list(reader.fieldnames)
            self.data = list(reader)

    def get_numeric_values (self, column_name):
        values = [] #Empty list
        for row in self.data:
                value = row[column_name] # get one value at a time
                try:
                    values.append(float(row[column_name ]))
                except:
                 continue
        return values
            
    def handle_missing_values ( self ,column_name, strategy = 'drop', fill_value = None):
        if strategy == 'drop':
            self.data = [row for row in self.data if row [column_name] != '' and row[column_name] is not None]
        elif strategy == 'fill':
            for row in self.data:
                if row[column_name] in ['', None]:
                    row[column_name] = fill_value
        elif strategy == 'mean':
            values = self.get_numeric_values(column_name)
            mean_values = statistics.mean(values)
            for row in self.data:
                if row[column_name] in ['', None]:
                    row[column_name] = mean_values

    def remove_duplicates (self):
        unique_data = []

        for row in self.data:
            if row not in unique_data:
                unique_data.append(row)


        self.data = unique_data # this is after the loop

    def fix_data_types(self, column_name, target_type):
        if target_type == 'int':
            for row in self.data:
                try:
                    row[column_name] = int(row[column_name])
                except:
                    continue
        
        elif target_type == 'float':
            for row in self.data:
                try:
                    row[column_name] = float(row[column_name])
                except:
                    continue
        elif target_type == 'str':
            for row in self.data:
                    row[column_name] = str(row[column_name])


    def normalise_values ( self, column_name):
            values = self.get_numeric_values(column_name)
            min_val = min(values)
            max_val = max(values)
            for row in self.data:
                try:
                    original = float(row[column_name])
                    normalized = (original - min_val) / (max_val - min_val)
                    row [column_name] = normalized

                except:
                    continue
    
    def standardize_column(self, column_name):
            values = self.get_numeric_values(column_name)
            mean_val = statistics.mean(values)
            std_val = statistics.stdev(values)
        
            for row in self.data:
                try:    
                    original = float(row[column_name])
                    standardized = (original - mean_val) / std_val
                    row[column_name] = standardized
                except:
                    continue
    
    def detect_ouliers (self, column_name, threshold = 2 ):
            values = self.get_numeric_values(column_name) 
            mean_val = statistics.mean(values)
            std_val = statistics.stdev(values)

            outliers = []
            for value in values: # check for each value in the values
                if abs (value-mean_val) > threshold * std_val:
                    outliers.append(value)

            return outliers 
    
    def export_cleaned_Data ( self, output_filename):
        with open (output_filename, 'w') as file:
            writer = csv.DictWriter ( file, fieldnames= self.headers)
            writer.writeheader()
            writer.writerows(self.data)






dataguy = datacleaner("Test.csv")

dataguy.load_csv ()

dataguy.handle_missing_values('ads_listened_per_week', strategy= 'fill', fill_value='123')

dataguy.export_cleaned_Data('cleaned_output.csv')
    