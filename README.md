# de-columnizing
Often, column-style writing will put images and features to the left or right of the body of text, for example:
24
This is an example piece of text. This is an exam-
ple piece of text. This is an example piece of
text. This is an example
piece of text. This is a +-----------------------+
sample for a challenge.  |                       |
Lorum ipsum dolor sit a- |       top class       |
met and other words. The |        feature        |
proper word for a layout |                       |
like this would be type- +-----------------------+
setting, or so I would
imagine, but for now let's carry on calling it an
example piece of text. Hold up - the end of the
                 paragraph is approaching - notice
+--------------+ the double line break for a para-
|              | graph.
|              |
|   feature    | And so begins the start of the
|   bonanza    | second paragraph but as you can
|              | see it's only marginally better
|              | than the other one so you've not
+--------------+ really gained much - sorry. I am
                 certainly not a budding author
as you can see from this example input. Perhaps I
need to work on my writing skills.
In order to fit into the column format, some words are hyphenated. For the purpose of the challenge, you may assume that any hyphens at the end of a line join a single un-hyphenated word together (for example, the exam- and ple in the above input form the word example and not exam-ple). However, hyphenated words that do not span multiple lines should retain their hyphens. Side features will only appear at the far left or right of the input, and will always be bordered by the +---+ style shown above. They will also never have 'holes' in them, like this:
+--------------------+
|                    |
| Inside the feature |
|                    |
| +----------------+ |
| |                | |
| |     Outside    | |
| |                | |
| +----------------+ |
|                    |
+--------------------+
Paragraphs in the input are separated by double line breaks, like Reddit markdown. Your task today is to extract just the paragraph text from the input, removing the feature-boxes.

Input Specification

You'll be given a number N on one line, followed by N further lines of input like the example in the description above.
Output Description

Output just the paragraph text, de-hyphenating words where appropriate (ie. a line of text ends with a hyphen).
