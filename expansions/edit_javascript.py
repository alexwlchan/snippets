from javascript_data_files import read_js

value = read_js("filename.js", varname="varname")

write_js("filename.js", varname="varname", value=value)