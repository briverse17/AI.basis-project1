# Path finding algorithms

Requirements:

- Python 3.7

## Run without Docker

Installation (better with a [venv](https://docs.python.org/3/library/venv.html))

```bash
pip install -r requirements.txt
```

Usage

```bash
python3 main.py <algo> <input> (*)
```

`<algo>` options:

- `BFS`
- `DFS`
- `UCS`
- `Greedy`
- `AStar`
- `AStarNPoint`

`<input>` options:

- `input{1..6}.txt`

For example, if you want to run AStar on input 5, then the command is:

```bash
python3 main.py AStar input5.txt
```

## Run with Docker (recommended)

Requirements

- Docker >= 26.0.0
- Docker Compose >= v2.25.0

Installation

```bash
docker compose build
```

Usage

```bash
docker compose up -d
docker exec python3 /bin/bash -c "<same as in (*)>"
```

For example, if you want to run DFS on input 6, then the command is:

```bash
docker exec python3 /bin/bash -c "python3 main.py DFS input6.txt""
```

Or, if you want to run an interactive shell to play around:

```bash
docker exec -it python3 /bin/bash
```

You should get something like this:

```bash
root@bb6c80ec8792:/app$ python3 -V
Python 3.7.17
root@bb6c80ec8792:/app$ 
```
