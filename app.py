import os

# Assuming the list is stored in a variable called 'list'
list_var = os.environ["KMVAR_targetSentences"];

# Split the list into individual items
items_var = list.split(',');

// Create a table element
table = document.createElement('table');

# Iterate over the items and create table rows

items.forEach(item => {
  const row = document.createElement('tr');
  const cell = document.createElement('td');
  cell.textContent = item;
  row.appendChild(cell);
  table.appendChild(row);
});

# Append the table to the document body
document.body.appendChild(table);
