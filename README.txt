You should provide a list with all the file paths of the articles and put it under the same directory of .py file.
Articles can be in some subdirectories once you clearly declare the relative paths between the list.

1. First, call BuildTable("[list_file_path]") to create the text-document matrix.
2. Use SearchDocument("[keyword]") to get a list of booleans determining which article contains the keyword.
3. Use RetrieveDocument([boolean list]) to get a list of the names of the articles marked as "true" in the list.
4. You can use logic computation methods below with the lists returned by SearchDocument("[keyword]") to perform cross-reference.
	NOT([list]); AND([list1],[list2]); OR([list1],[list2]); XOR([list1],[list2])