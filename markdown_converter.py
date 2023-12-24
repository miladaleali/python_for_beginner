# Import the nbformat module, which provides tools for working with Jupyter notebook files
import nbformat as nbf

# Define a function that takes a markdown file name as an argument and returns a notebook object
def md_to_nb(md_file):
    # Create a new notebook object with the default version and metadata
    nb = nbf.v4.new_notebook()
    # Open the markdown file and read its content
    with open(md_file, "r") as f:
        md_content = f.read()
    # Split the markdown content by the triple backticks ``` that indicate code blocks
    md_parts = md_content.split("```")
    # Loop through the markdown parts and add them to the notebook cells
    for i, part in enumerate(md_parts):
        # If the index is even, the part is markdown text
        if i % 2 == 0:
            # Create a new markdown cell with the part as the source
            cell = nbf.v4.new_markdown_cell(part)
            # Append the cell to the notebook cells
            nb.cells.append(cell)
        # If the index is odd, the part is code
        else:
            # Split the part by the newline character \n
            part_lines = part.split("\n")
            # The first line is the language of the code, e.g. python
            language = part_lines[0]
            # The rest of the lines are the code itself
            code = "\n".join(part_lines[1:])
            # Create a new code cell with the code as the source and the language as the metadata
            cell = nbf.v4.new_code_cell(code, metadata={"language": language})
            # Append the cell to the notebook cells
            nb.cells.append(cell)
    # Return the notebook object
    return nb

# Define a function that takes a notebook object and a file name as arguments and writes the notebook to the file
def nb_to_file(nb, nb_file):
    # Open the file in write mode
    with open(nb_file, "w") as f:
        # Write the notebook object to the file using the nbformat module
        nbf.write(nb, f)

# Define the markdown file name and the notebook file name
md_file = "example.md"
nb_file = "example.ipynb"

# Convert the markdown file to a notebook object
nb = md_to_nb(md_file)

# Write the notebook object to a file
nb_to_file(nb, nb_file)

# Print a message to indicate the conversion is done
print(f"Converted {md_file} to {nb_file}")
