# dirstate
> Save the state of a directory and return to it when ever you want.

## Usage
### Saving the state
> To save the state:

    $ dirstate save

> This will save the current state with an ID and a timestamp.

### Listing states
> To list saved states of the current directory:

    $ dirstate log

> This will output a list of states, something like this:

    {
        "date": "2018-08-17 09:44:19", 
        "directory": "/home/ianertson/workspace/HCV", 
        "timestamp": "1534491859"
    }
    {
        "date": "2018-08-17 09:45:03", 
        "directory": "/home/ianertson/workspace/HCV", 
        "timestamp": "1534491903"
    }
    {
        "date": "2018-08-17 09:45:44", 
        "directory": "/home/ianertson/workspace/HCV", 
        "timestamp": "1534491944"
    }

### Going back to a previous state
> Want to return to a previous state of your directory?, this will do it:

    $ dirstate set <timestamp>

> This command takes a `timestamp` as an argument.

## Installing
> To install `dirstate`; clone down the repository and run:

    $ python setup.py install

## Where are the states stored?
> The states are stored in  `$HOME/.dirstate` , every state is a compressed `.tar.gz` file.
>
> The filename of every state contains information about it; such as:
>
> * directory name
> * timestamp
