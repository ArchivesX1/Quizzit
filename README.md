# Quizzit
Quiz taking tool, run it like this: "python3 quiz.py &lt;questionbank.tsv>"


Prompt Used for Creating Question Banks:


I need you to generate a TSV (Tab-Separated Values) file with REAL tab characters, not spaces.

IMPORTANT RULES FOR OUTPUT:

You MUST output the TSV inside a single fenced code block (triple backticks), so the user can copy/paste it directly into a .tsv file.

Inside the code block, every column separator MUST be a literal ASCII TAB character (U+0009).

Do NOT use spaces instead of tabs.

Do NOT use the characters “\t”, “TAB”, or any placeholder—use the actual real TAB key.

No commentary inside the code block.

No line breaks inside fields—each question must be a single row.

TSV Schema (first line must be the header):
id<TAB>question<TAB>a<TAB>b<TAB>c<TAB>d<TAB>correct<TAB>exp_a<TAB>exp_b<TAB>exp_c<TAB>exp_d
(Replace <TAB> with actual REAL U+0009 tabs.)

Field rules:

id starts at 1 and increments.

correct is exactly A, B, C, or D.

Each exp_* explanation must be short Tutorials-Dojo style (explain why option is correct/incorrect).

Your job:
Generate [NUMBER OF QUESTIONS] questions about [TOPIC] in this TSV format.

OUTPUT FORMAT REQUIREMENTS:

Output ONLY the TSV inside a single code block.

NO commentary above or below.

NO markdown formatting inside the block except the code fence itself.

MUST use REAL U+0009 tabs.

Begin now.
