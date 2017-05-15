# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

> > `pwd`: show current directory  
> > `mkdir <name>`: make directory  
> > `rmdir <name>`: delete a directory  
> > `touch <name>`: create an empty file  
> > `rm <name>`: delete a file  
> > `mv <name1> <name2>`: rename a file  
> > `ls -a`: list hidden files  
> > `cp <file> <new directory>`: copy a file to new directory  
> > `cd`: change directory  
> > `cat <name>`: output contents to console  

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > `ls`: list contents of current directory  
> > `ls -a`: list all contents, including hidden files/directories, in current directory  
> > `ls -l`: list contents in long format, including more details such as file/directory sizes
> > `ls -lh`: list with sizes in a more readable format  
> > `ls -lah`: list all contents in long format with readable file sizes  
> > `ls -t`: list, sorting by time modified  
> > `ls -Glp`: prints contents in long format, without owner names, appending slashes to any directories

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > `ls -d`: list only directories  
> > `ls -R`: display subdirectories  
> > `ls -c`: display by timestamp
> > `ls -F`: flag filenames
> > `ls -m`: display contents as a comma-separated list

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > Certain shell commands won't accept arbitrarily long inputs, so xargs breaks an input into several smaller sub-inputs that are processed in parallel.  

> >ex: `find . -name "*.md" | xargs grep "linear"` finds markdown files then looks for the word 'linear'
