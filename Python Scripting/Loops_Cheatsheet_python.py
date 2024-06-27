1    
2    # BASIC
3    
4    numsloop = [1, 2, 3, 4, 5]
5    
6    for num in numsloop:
7        print(num)
8    
9    # Output:
10   # 1
11   # 2
12   # 3
13   # 4
14   # 5
15   
16   
17   ### With BREAK ###
18   # used for STOPPING a loop when meeting a certain condition
19   
20   numsloop = [1, 2, 3, 4, 5]
21   
22   for num in numsloop:
23       if num == 3:
24           print('Found!')
25           break
26       print(num)
27   
28   # Output:
29   # 1
30   # 2
31   # Found!
32   
33   
34   
35   # With CONTINUE #
36   # use for SKIPPING a number
37   
38   numsloop = [1, 2, 3, 4, 5]
39   
40   for num in numsloop:
41       if num == 3:
42           print('Found!')
43           continue
44       print(num)
45   
46   # Output:
47   # 1
48   # 2
49   # Found!
50   # 4
51   # 5
52   
53   
54   # Iterating through loops #
55   # this example gives you EVERY combination of those numbers and letters
56   
57   numsloop = [1, 2, 3, 4, 5]
58   
59   for num in numsloop:
60       for letter in 'abc':
61           print(num, letter)
62   
63   # Output:
64   
65   # 1 a
66   # 1 b
67   # 1 c
68   # 2 a
69   # 2 b
70   # 2 c
71   # 3 a
72   # 3 b
73   # 3 c
74   # 4 a
75   # 4 b
76   # 4 c
77   # 5 a
78   # 5 b
79   # 5 c
80   
81   
82   # For Loops with range()
83   
84   six_steps = range(6)
85   
86   # # six_steps is now a collection with 6 elements:
87   # # 0, 1, 2, 3, 4, 5
88   
89   # #We can then use the range directly in our for loops as the collection to perform a six-step iteration:
90   
91   for temp in range(6):
92     print("Learning Loops!")
93   
94   
95   # Would output:
96   
97   # Learning Loops!
98   # Learning Loops!
99   # Learning Loops!
100  # Learning Loops!
101  # Learning Loops!
102  # Learning Loops!
103  
104  
105  
106  
107  # Something to note is we are not using temp anywhere inside of the loop body.
108  # If we are curious about which loop iteration (step) we are on, we can use temp to track it.
109  # Since our range starts at 0, we will add + 1 to our temp to represent how many iterations (steps) our loop takes more accurately.
110  
111  for temp in range(6):
112    print("Loop is on iteration number " + str(temp + 1))
113  
114  # Would output:
115  
116  # Loop is on iteration number 1
117  # Loop is on iteration number 2
118  # Loop is on iteration number 3
119  # Loop is on iteration number 4
120  # Loop is on iteration number 5
121  # Loop is on iteration number 6
122  
123  
124  
125  
126  # # Use the range() function in a for loop to print() out the provided promise variable five times.
127  #
128  promise = "I will finish the python loops module!"
129  
130  for temp in range(5):
131    print(promise)
132  
133  # Output:
134  # I will finish the python loops module!
135  # I will finish the python loops module!
136  # I will finish the python loops module!
137  # I will finish the python loops module!
138  # I will finish the python loops module!
139  
140  
141  
142  
143  
144  # # While Loop Walkthrough # #
145  
146  count = 0
147  print("Starting While Loop")
148  while count <= 3:
149    Loop Body
150    # Print if the condition is still true
151    print("Loop Iteration - count <= 3 is still true")
152    # Print the current value of count
153    print("Count is currently " + str(count))
154    # Increment count
155    count += 1
156    print(" ----- ")
157  print("While Loop ended")
158  
159  
160  # Output:
161  # Starting While Loop
162  # Loop Iteration - count <= 3 is still true
163  # Count is currently 0
164  #  -----
165  # Loop Iteration - count <= 3 is still true
166  # Count is currently 1
167  #  -----
168  # Loop Iteration - count <= 3 is still true
169  # Count is currently 2
170  #  -----
171  # Loop Iteration - count <= 3 is still true
172  # Count is currently 3
173  #  -----
174  # While Loop ended
175  
176  
177  
178  # # To quickly comment out the code, use your cursor or mouse to highlight all the code
179  # # and press command ⌘ + / on a Mac or CTRL + / on a Windows machine.
180  
181  
182  # # Your code below:
183  # # Create a variable named countdown and set the value to 10.
184  countdown = 10
185  
186  # # Define a while loop that will run while our countdown variable is greater than or equal to zero.
187  
188  # # On each iteration:
189  # # We should print() the value of the countdown variable.
190  # # We should decrease the value of the countdown variable by 1
191  
192  while countdown >= 0:
193    print(countdown)
194    countdown -= 1
195  
196  # # Now that we have built our loop, let’s commemorate our success by printing "We have liftoff!" after the while loop.
197  # print("We have liftoff!")
198  
199  # Output:
200  # 10
201  # 9
202  # 8
203  # 7
204  # 6
205  # 5
206  # 4
207  # 3
208  # 2
209  # 1
210  # 0
211  # We have liftoff!
212  
213  
214  
215  
216  #######################
217  python_topics = ["variables", "control flow", "loops", "modules", "classes"]
218  # #Your code below:
219  # # We are going to write a while loop to iterate over the provided list python_topics.
220  
221  # # First, we will need a variable to represent the length of the list.
222  # # This will help us know how many times our while loop needs to iterate.
223  
224  # # Create a variable length and set its value to be the length of the list of python_topics.
225  length = len(python_topics)
226  
227  
228  # # Next, we will require a variable to compare to our length variable to make sure we are able
229  # # to implement a condition that eventually allows the loop to stop.
230  #
231  # # Create a variable called index and initialize the value to be 0.
232  index = 0
233  
234  
235  # # Let’s now build our loop.
236  # # We want our loop to iterate over the list of python_topics and
237  # # on each iteration print "I am learning about <element from python_topics>".
238  # #
239  # # For this loop we will need the following components:
240  
241  # # A condition for our while loop
242  # # A statement in the loop body to print from our condition
243  # # A statement in the loop body to increment our index forward.
244  # # The end result should output:
245  
246  # # I am learning about variables
247  # # I am learning about control flow
248  # # I am learning about loops
249  # # I am learning about modules
250  # # I am learning about classes
251  # # If you notice the Run button spinning continuously or a “Lost connection to Codecademy” message in an exercise,
252  # # you may have an infinite loop!
253  
254  # # If the stop condition for our loop is never met,
255  # # we will create an infinite loop which stops our program from running anything else.
256  # # To exit out of an infinite loop in an exercise, refresh the page — then fix the code for your loop.
257  
258  while index < length:
259      print("I am learning about " + python_topics[index])
260  index += 1
261  
262  
263  # Output:
264  # I am learning about variables
265  # I am learning about variables
266  # I am learning about variables
267  # I am learning about variables
268  # I am learning about variables
269  # I am learning about variables
270  # I am learning about variables
271  # I am learning about variables
272  # And it will KEEP going infinitely
273  
274  
275  
276  
277    # Loop Control: Break
278    # Loops in Python are very versatile.
279    # Python provides a set of control statements that we can use to get even more control out of our loops.
280  
281    # Let’s take a look at a common scenario that we may encounter to see a use case for loop control statements.
282  
283    # Take the following list items_on_sale as our example:
284  
285    # items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
286  
287    # It’s often the case that we want to search a list to check if a specific value exists.
288    # What does our loop look like if we want to search for the value of "knit dress" and print out "Found it" if it did exist?
289  
290  # It would look something like this:
291  
292    for item in items_on_sale:
293      if item == "knit dress":
294        print("Found it")
295  
296    # This code goes through each item in items_on_sale and checks for a match.
297    # This is all fine and dandy but what’s the downside?
298    #
299    # Once "knit_dress" is found in the list items_on_sale, we don’t need to go through the rest of the items_on_sale list.
300    # Unfortunately, our loop will keep running until we reach the end of the list.
301    #
302    # Since it’s only 5 elements long, iterating through the entire list is not a big deal in this case but
303    # what if items_on_sale had 1000 items?
304    # What if it had 100,000 items? This would be a huge waste of time for our program!
305    #
306    # Thankfully you can stop iteration from inside the loop by using break loop control statement.
307    #
308    # When the program hits a break statement it immediately terminates a loop. For example:
309  
310    # items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
311    #
312    # print("Checking the sale list!")
313  
314    for item in items_on_sale:
315        print(item)
316        if item == "knit dress":
317            break
318  
319    print("End of search!")
320  
321  #   # This would produce the output:
322  #   #
323  #   # Checking the sale list!
324  #   # blue shirt
325  #   # striped socks
326  #   # knit dress
327  #   # End of search!
328  #
329  #   # When the loop entered the if statement and saw the break it immediately ended the loop.
330  #   # We didn’t need to check the elements of "red headband" or "dinosaur onesie" at all.
331  #
332  #   # Example:
333  #
334  #   # You have a list of dog breeds you can adopt, dog_breeds_available_for_adoption.
335  #
336  dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
337  dog_breed_I_want = "dalmatian"
338  #
339  #   # Using a for loop, iterate through the dog_breeds_available_for_adoption list and print() out each dog breed.
340  #
341  #   # Use the <temporary variable> name of dog_breed in your loop decleration.
342  #
343  for dog_breed in dog_breeds_available_for_adoption:
344  print(dog_breed)
345  #
346  #   # Inside your for loop, after you print each dog breed,
347  #   # check if the current element inside dog_breed is equal to dog_breed_I_want. If so, print "They have the dog I want!"
348  #
349    for dog_breed in dog_breeds_available_for_adoption:
350      print(dog_breed)
351      if dog_breed == dog_breed_I_want:
352        print("They have the dog I want!")
353  #
354  #   # Add a break statement when your loop has found dog_breed_I_want
355  #   # so that the rest of the list does not need to be checked once we have found our breed.
356  #
357  for dog_breed in dog_breeds_available_for_adoption:
358      print(dog_breed)
359      if dog_breed == dog_breed_I_want:
360          print("They have the dog I want!")
361          break
362  
363  # Output:
364  # french_bulldog
365  # dalmatian
366  # They have the dog I want!
367  
368  
369  
370  
371  # # Loop Control: Continue # #
372  #
373  # # What if we only want to skip the current iteration of the loop?
374  #
375  # # Let’s take this list of integers as our example:
376  #
377  big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]
378  # # What if we want to print out all of the numbers in a list, but only if they are positive integers. We can use another common loop control statement called continue.
379  #
380  for i in big_number_list:
381    if i <= 0:
382      continue
383    print(i)
384  #
385  # # This would produce the output:
386  # # 1
387  # # 2
388  # # 4
389  # # 5
390  # # 2
391  #
392  # # Notice a few things:
393  #
394  # # Similar to when we were using the break control statement,
395  # # our continue control statement is usually paired with some form of a conditional (if/elif/else).
396  # # When our loop first encountered an element (-1) that met the conditions of the if statement,
397  # # it checked the code inside the block and saw the continue. When the loop then encounters a continue statement
398  # # it immediately skips the current iteration and moves onto the next element in the list (4).
399  # # The output of the list only printed positive integers in the list because every time our loop entered the if statement
400  # # and saw the continue statement it simply moved to the next iteration of the list and thus never reached the print statement.
401  #
402  #
403  ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
404  #
405  # # Your computer is the doorman at a bar in a country where the drinking age is 21.
406  #
407  # # Loop through the ages list. If an entry is less than 21, skip it and move to the next entry. Otherwise, print() the age.
408  #
409  for i in ages:
410    if i < 21:
411      continue
412    print(i)
413  #
414  # Output:
415  # 38
416  # 34
417  # 26
418  # 21
419  # 67
420  # 41
421  #
422  #
423  #
424  #
425  # # Nested Loops
426  # # Loops can be nested in Python, as they can with other programming languages. We will find certain situations that require nested loops.
427  # #
428  # # Suppose we are in charge of a science class, that is split into three project teams:
429  #
430  project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
431  #
432  # # Using a for or while loop can be useful here to get each team:
433  #
434  for team in project_teams:
435    print(team)
436  #
437  # # Would output:
438  # #
439  # # ["Ava", "Samantha", "James"]
440  # # ["Lucille", "Zed"]
441  # # ["Edgar", "Gabriel"]
442  
443  
444  # # But what if we wanted to print each individual student?
445  # # In this case we would actually need to nest our loops to be able loop through each sub-list.
446  # # Here is what it would look like:
447  
448  # # Loop through each sublist
449  
450  project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]
451  
452  for team in project_teams:
453  #   # Loop elements in each sublist
454    for student in team:
455      print(student)
456  #
457  # # This would output:
458  #
459  # # Ava
460  # # Samantha
461  # # James
462  # # Lucille
463  # # Zed
464  # # Edgar
465  # # Gabriel
466  
467  
468  # # Let’s practice wiriting a nested loop!
469  #
470  # # We have provided the list sales_data that shows the
471  # # numbers of different flavors of ice cream sold at
472  # # three different locations: Scoopcademy, Gilberts Creamery, and Manny’s Scoop Shop.
473  
474  # # We want to sum up the total number of scoops sold.
475  # # Start by defining a variable scoops_sold and set it to zero.
476  
477  
478  sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
479  
480  scoops_sold = 0
481  
482  # # Loop through the sales_data list using the following guidelines:
483  
484  # # 1) For our temporary variable of the for loop, call it location.
485  # # 2) print() out each location list.
486  
487  
488  # # Within our sales_data loop,
489  # # nest a secondary loop to go through each location sublist element and add the element value to scoops_sold.
490  
491  # # By the end, you should have the sum of every number in the sales_data nested list.
492  
493  # # Print out the value of scoops_sold outside of the nested loop.
494  
495  for location in sales_data:
496      print(location)
497      for element in location:
498          scoops_sold += element
499  
500  print(scoops_sold)
501  #
502  #
503  # Output:
504  # [12, 17, 22]
505  # [2, 10, 3]
506  # [5, 12, 13]
507  # 96
508  
509  
510  # # Let’s write our own list comprehensions with conditionals!
511  
512  
513  heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
514  
515  can_ride_coaster = []
516  
517  
518  for num in heights:
519      if num > 161:
520          can_ride_coaster.append(num)
521  
522  print(can_ride_coaster)
523  
524  
525  # # I just settled on the "Traditional Way" of writing for loops.
526  # # Don't overcomplicate!
527  
528  
529  
530  
531  # # Review
532  
533  # # Directions
534  #
535  # # 1. Create a list called single_digits that consists of the numbers 0-9 (inclusive).
536  # # 2. Create a for loop that goes through single_digits and prints out each one.
537  # # 3. Before the loop, create a list called squares. Assign it to be an empty list to begin with.
538  # # 4. Inside the loop that iterates through single_digits,
539  # # append the squared value of each element of single_digits to the list squares.
540  # # You can do this before or after printing the element.
541  # # 5. After the for loop, print out squares.
542  
543  single_digits = range(0, 10)
544  
545  squares = []
546  
547  for num in single_digits:
548    squares.append(num**2)
549  
550  print(squares)
551  
552  
553  # # 6. Create the list cubes using a list comprehension on the single_digits list.
554  # # Each element of cubes should be an element of single_digits taken to the third power.
555  # # 7. Print cubes
556  
557  cubes = [num**3 for num in single_digits]
558  print(cubes)
559  
560  
561  # Output:
562  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
563  # [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
