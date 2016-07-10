import sys
import itertools

class TypingSection(object):

  def __init__(self, start, end, title, display_fn):
    self.str_start = start
    self.str_end = end
    self.title = title
    self.display_fn = display_fn

  # Use the strings passed in as start and finish
  # to track down the indices of the beginning and
  # end of the section
  def set_start_end(self, f):
    f.seek(0)
    for i, line in enumerate(f):
      if line.strip() == self.str_start:
        self.start_index = i
      if line.strip() == self.str_end:
        self.end_index = i

  def display(self, f):
    self.set_start_end(f)
    f.seek(0)
    print("\n## {}".format(self.title))
    for i, line in enumerate(itertools.islice(f, self.start_index, self.end_index + 1)):
      self.display_fn(i, line.strip())

def qa_display_line(i, line):
  if i % 4 == 0:
    print("\n**{}**\n".format(line))
  else:
    print("* {}".format(line))

def quick_qa_display_line(i, line):
  questions = [ "What's bigger than a bread box",
  "Find the important car part",
  "Something you can do naked",
  "A kind of water",
  "Something that'll make a cat happy",
  "A kid's fort would be made of",
  "Name the girlie thing",
  "Something adults have to do",
  "Something to do before you go to bed",
  "Something not to tell her folks",
  "You can drive here from Texas",
  "Find the Constellation",
  "You eat this with your hands" ]
  
  if line in questions or (line[-1] == "?" and line != "Why not?"):
    print("\n**{}**\n".format(line))
  else:
    print("* {}".format(line))
    
def display_line(i, line):
  # In the jokes section there's a weird
  # display of only 3 lines that starts with
  # "I ate too much pizza, but it's okay,"
  # and it throws off our index
  
  if i % 4 == (3 if i > 468 else 0):
    print("\n")
  print("* {}".format(line))

def similar_display_line(i, line):
  # chicken one only has 9
  # Chicken cacciatore is last one
  if i % 10 == (9 if i >= 128 else 0):
    print("\n")
  print("* {}".format(line))

sections = [
  {
    'title': "Thoughtful questions",
    'start': "What does valentine's day mean to you?",
    'end': "Being a judge for a swimsuit competition",
    'display_fn': qa_display_line
  },
  {
    'title': 'Jokes',
    'start': 'The quick brown fox jumped over the',
    'end': 'Quit mime school after the first day.',
    'display_fn': display_line
  },
  {
    'title': "Quick questions",
    'start': "Which is a State in the US?",
    'end': "Wet concrete",
    'display_fn': quick_qa_display_line
  },
  {
    'title': "Similar things",
    'start': 'Molly',
    'end': 'OUTTRIGGER',
    'display_fn': similar_display_line
  }
]

with open(sys.argv[1]) as f:
  for section in sections:
    section = TypingSection(**section)
    section.display(f)