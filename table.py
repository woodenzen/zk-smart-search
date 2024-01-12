import os

print(os.environ["KMVAR_Local_targetSentences"])
target_sentences = os.environ.get("KMVAR_Local_targetSentences")

# Create the table
table = []
for sentence in target_sentences:
    table.append(sentence.split(","))

# Print the table
for row in table:
    print(row)
