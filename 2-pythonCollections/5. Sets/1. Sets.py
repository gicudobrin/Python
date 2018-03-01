# One of the most common ways you'll see sets being used is to make some other iterable unique. For example, say you have a list of page numbers where terms appear in a book. Since some pages could contain multiple terms, you're likely to get repeats. In that case, you'll see people doing code like this:

# pages = list(set(pages))

# my_set = set(1,3,5)
# print(my_set)
# asd={1,2,3}
# print(asd)

liste = {1,2,3,4}
print(liste)
liste.add(13)
print(liste)
liste.add(1)
print(liste)

liste.update
liste.remove

songs = {"A", "a", "s"}
songs.add("Treehouse Hula")
songs.update({"Python Two-Step", "Ruby Rhumba"},{"My PDF Files"})


# Sets let us easily compare and contrast them.

# The docs about sets are pretty good and I suggest you check them out. Here's yet another brief explanation of the common set operations:

# | or .union(*others) - all of the items from all of the sets
# & or .intersection(*others) - all of the common items between all of the sets
# - or .difference(*others) - all of the items in the first set that are not in the other sets
# ^ or .symmetric_difference(other) - all of the items that are not shared by the two sets
# (also: notice how those are using *others? That's a tuple of other sets. See, I told you that pattern was everywhere!)