<p align="center">🎵🆔</p>

<h1 align="center">Genre ID</h1>

<p align="center">
  <strong>CLI Script to get song genre from Beatport</strong>
</p>

## Usage


```python
usage: genre-id.py [-h] [-v] [-vv] query [query ...]

ID Genre from Beatport

positional arguments:
  query       Song Artist + Title query

optional arguments:
  -h, --help  show this help message and exit
  -v          Print first song name and genre
  -vv         Print all song names, artists, remixers, and genres
```


## Examples

`./genre-id.py Major7 Closer`

output:

```
Psy-Trance

```


`./genre-id.py -v Major7 Closer`

output:

```
Name         Genre
-----------  ----------
Closer       Psy-Trance
Bamboozled   Psy-Trance
Inequality   Psy-Trance
Moonlight    Psy-Trance
Psychotic    Psy-Trance
Glide        Psy-Trance
Look Around  Psy-Trance
```



`./genre-id.py -vv Major7 Closer`

output:

```
Name         Artist                 Remixers    Genre
-----------  ---------------------  ----------  ----------
Closer       Major7                             Psy-Trance
Bamboozled   Major7                             Psy-Trance
Inequality   Major7                             Psy-Trance
Moonlight    Major7, Rexalted                   Psy-Trance
Psychotic    Major7, D-Addiction                Psy-Trance
Glide        Major7, Invader Space              Psy-Trance
Look Around  Major7, Rexalted                   Psy-Trance
```


## Installation

install dependencies

```sh
python3 -m pip install requests bs4 tabulate
```

copy the script to your path, make it executable

```sh
curl https://raw.githubusercontent.com/theRemix/genre-id/master/genre-id.py > ~/.local/bin/genre-id.py
chmod +x ~/.local/bin/genre-id.py
```
