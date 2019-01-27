
This code will enable to compare any 2 valid JSON files based on the linear mapping of the data elements. The mapping file will look like:
field1.field2=ffield2.ffield1

The '.' notation is used to differentiate levels.

To compare to a constant value use 'R' notation (Check examples in config files).

The typical use case is while verifying the data transfer between 2 systems or in a pipeline, this code can be used to verify the data 
elements that may be following different names and structure as per the system design and behavior but carrying same values (same source). 

