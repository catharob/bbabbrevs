# Blue Book Abbreviations

A little program to look up Bluebook abbreviations for legal citations.

### What does this program do?

This program allows the user to input a long title of something that has a designated Bluebook abbreviation, and the program returns the abbreviation. It saves the user from having to search or scroll through tables of abbreviations.

### Where do the abbreviations come from?

From [The Bluebook](https://www.legalbluebook.com/).

It's a widely used system of formatting and citation for legal writing. **These citations come from the Bluebook's _20th edition_, and are subject to change.**

### What can and can't it do?

It **can** look up abbreviations, if the exact phrase you input is listed in the Bluebook's citation dictionary. 

It **can't** concatonate together phrases from different lines of the dictionary. For instance, "Economic" and "Advocacy" both have specific abbreviations. Enter either word by itself, and the program will return the abbrev. But "Economic advocacy" does not have its own entry in the dictionary, and the program will not know to abbreviate them as one unit.

### But that would be so cool...

I know. It's coming in Version 2!

### So how do I run it?

1. Download this whole folder using the "Download ZIP" at the top of the page. 
2. Save somewhere easily accessible, like Desktop or Documents. Unzip!
3. Open Terminal and `[cd](https://help.ubuntu.com/community/UsingTheTerminal#File_.26_Directory_Commands)` into the directory where you just saved the `abbrevs` zip.
4. `cd` into abbrevs.
5. Type `python bbabbrevs.py` and hit return.
6. Enter your information as the program prompts!

### Why did you make this?

A dear friend is in law school and serves on law review as an editor. Among many other things, she's tasked with ensuring all citations align with Bluebook standards. I mainly made this because **it's a repetetive task that basically begs to be automated**.

### This helps, but citation is still such a pain in the ass.

I know. You can do it!

![](http://media.giphy.com/media/3oEdv1TySA9eVxp2Ew/giphy.gif)