# socmd
> Socket command line framework

## What is it used for?
> You can create commands on your server using python files and then they
> can be executed through socket connections in a command line interface.

## Installing
> To install, clone down the repository and run:

    python setup.py install

## Running the server
> To run the server:

    socmd-server --port 5000 --commands where.commands.should.be.imported.from

> Example:

    socmd-server --port 5000 --commands myapplication.commands


## Running the client
> To start the client

    socmd-server --port 5000 --host 127.0.0.1

> You will now get access to an interactive command line interface where you
> can execute commands.

> For example, if I run the command:

    helloworld 20 30

> The server will look for a python module called `helloworld` in the commands
> directory that you specified an it will pass the arguments `20` and `30` to
> it.

## Writing commands
> Writing commands is simple, all you need to do is to create a python file
> with the method `run` exposed in it.

> Example:

    def run():
        return 'Hello World'

> Whatever the run method returns will be sent to the user who executed the
> command.
