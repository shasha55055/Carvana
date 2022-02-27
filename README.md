# Carvana Coding Challenge

# Objective 
Create a python program that is executable from the command line or standard input device. Program must read one or more .txt files and return a list of the 100 most common three word sequences.

# Install and Run Program

## Prerequesites
Have some version of python3 installed
To check current python version run the following comman

```
python --version
```

## Clone project from this repository
run this command to clone

```
git clone https://github.com/shasha55055/Carvana.git
```

## Run with Command prompt

```
# to enter multiple files enter a space fallowed by the file path of the next file
./Main.py show_most_three <filepath>
```

Example input

```
./Main.py show_most_three sample1.txt sample2.txt
```

## Run with stdin 

```
#run program
./Main.py

# to enter multiple files enter a comma and space fallowed by the file path of the next file
Enter Selected files: <filepath>
```

Example input

```
./Main.py
Enter Selected files: sample1.txt, sample2.txt
```

## Example output
```
List of most common 3 word sequences in sample.txt
oh captain deal - 9
captain deal oh - 9
deal oh captain - 6
woah ohoh ohoh - 6
ohoh ohoh woah - 6
ohoh woah ohoh - 6
captain oh captain - 5
the things that - 5
in a bottle - 3
oh captain lets - 3
captain lets make - 3
lets make a - 3
make a deal - 3
a deal where - 3
deal where we - 3
where we both - 3
we both say - 3
both say the - 3
say the things - 3
things that we - 3
that we both - 3
we both really - 3
both really feel - 3
really feel i - 3
feel i feel - 3
i feel scared - 3
feel scared and - 3
scared and im - 3
and im starting - 3
im starting to - 3
starting to sink - 3
to sink and - 3
sink and i - 3
and i only - 3
i only sink - 3
only sink deeper - 3
sink deeper the - 3
deeper the deeper - 3
the deeper i - 3
deeper i think - 3
i think oh - 3
think oh captain - 3
oh captain oh - 3
deal oh woah - 3
woah woah ohoh - 3
woah ohoh ohohoh - 3
ohoh ohohoh woah - 3
sailing on a - 2
on a ship - 2
a ship in - 2
ship in a - 2
you set sail - 2
set sail alone - 2
sail alone there - 2
alone there is - 2
there is no - 2
is no crew - 2
no crew no - 2
crew no one - 2
no one on - 2
one on the - 2
on the deck - 2
the deck who - 2
deck who can - 2
who can help - 2
can help you - 2
help you this - 2
you this is - 2
this is all - 2
is all your - 2
all your own - 2
your own battle - 2
own battle to - 2
battle to win - 2
to win this - 2
win this is - 2
this is your - 2
is your ship - 2
your ship and - 2
ship and you - 2
and you are - 2
you are the - 2
are the captain - 2
the captain oh - 2
oh captain make - 2
captain make up - 2
make up your - 2
up your mind - 2
your mind before - 2
mind before the - 2
before the salt - 2
the salt burns - 2
salt burns your - 2
burns your eyes - 2
your eyes and - 2
eyes and you - 2
and you run - 2
you run out - 2
run out of - 2
out of time - 2


List of most common 3 word sequences in mobydick.txt
the sperm whale - 39
the white whale - 38
of the whale - 37
a sort of - 33
one of the - 32
of the sea - 30
out of the - 29
part of the - 24
of the ship - 22
of the boat - 20
it is a - 18
of the sperm - 18
there was a - 18
it was a - 16
in order to - 15
it was the - 15
to be the - 15
of the pequod - 15
the townhos story - 14
it was not - 14
the bottom of - 14
by no means - 14
of the white - 14
that he was - 13
but it was - 13
there is no - 13
the right whale - 13
as if it - 12
to be sure - 12
i do not - 12
that in the - 12
must have been - 12
one of those - 12
at the time - 12
as well as - 11
in his own - 11
it is not - 11
to be a - 11
he s a - 11
the head of - 11
it is the - 11
it was that - 11
that it was - 11
for the time - 11
and all the - 11
now and then - 11
bottom of the - 11
the sea and - 11
for a moment - 11
queequeg said i - 11
what s that - 11
the greenland whale - 11
in the sea - 10
in the world - 10
in the air - 10
and as for - 10
down into the - 10
at the same - 10
and in the - 10
up to the - 10
down to the - 10
that s the - 10
one of them - 10
not to be - 10
with the same - 10
and with a - 10
him in the - 10
the ship and - 10
of the world - 9
was one of - 9
of a whale - 9
by a whale - 9
whale in the - 9
i thought i - 9
out of sight - 9
what do you - 9
the act of - 9
of the great - 9
it was only - 9
it s a - 9
and at last - 9
that sort of - 9
i could not - 9
i began to - 9
seemed to be - 9
not at all - 9
in the fishery - 9
it is that - 9
to the other - 9
into the cabin - 9
the sea the - 9
on board the - 9
some of the - 9
it would be - 9
whiteness of the - 8
the first lowering - 8
on the sea - 8
the whale is - 8
the whale in - 8
of the same - 8
```
# Docker Container
This program can be run in a docker container through the docker image created by the docker file.
Ensure that all relavant .txt files are included in the repository
To run this program in a docker container, docker must be installed.
Check docker version using the following.
```
docker --version
```

To build the docker image, locate the repository and run the following.
```
docker build .
```

check the built image using

```
docker images
```

which should return 
```
REPOSITORY                                        TAG           IMAGE ID       CREATED          SIZE
<none>                                            <none>        ec24f3925a54   10 minutes ago   860MB
```
To run the program in the container:
```
docker run -it <image ID> 
```

# Problems To Fix If Given More Time
* Unicode - Program is capable of interpreting unicode characters such as ü and ß. However, the program heavily relies on the use of spaces in a written language. As a result, languages, such as chinese and japanese, that do not use spaces are incompatible with this program. Furthermore, this program does not remove punctuations not used in standard english such as ¿ and 。

* Effeciency - This program reads each word in each .txt file one by one twice and processes them through two dictionaries before returning an output. This results in a high runtime for larger files. This can be reduced by processing multiple files at once or formatting the data with a different algorithm.


