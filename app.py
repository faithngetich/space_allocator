
"""
Usage:
    amity create_room (O|L) <room_name>...
    amity delete_rooms(args['<room_name>'])
    amity add_person <first_name> <last_name> (F | S) [--wants_accomodation=value]
    amity delete_employee(int(args['<person_id>']))
    amity print_allocations [-output=<filename>]
    amity reallocate_person <person_id> <new_room>
    amity print_room <room_name>
    amity print_unallocated [-output=<filename>]
    amity load_people <filename>
    amity delete_rooms(args['<room_name>'])
    amity save_state (--database=<sqlite_database>)
    amity load_state
    amity (-i | --interactive)
    amity (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    -a, --wants_accomodation=<opt>  Person wants accomodation [default: N]
    -d, --database=<sqlite_database>  Save state to specified database [default: amity_db]
"""
import cmd, os, sys
from docopt import docopt, DocoptExit
from pyfiglet import figlet_format
from termcolor import cprint
from views import Amity


amity = Amity()

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__,arg)
        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.
            return
        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

def intro():
    cprint(figlet_format('Space Allocator', font='slant'),
           'blue', attrs=['bold'])
    print("Welcome to Amity! Here is a list of commands to get you started." +
          " Type 'help' anytime to access documented commands")
    print("\n\n")
    cprint(__doc__, 'magenta')


class AmitySystem(cmd.Cmd):
    prompt = '(Amity) '
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room (O|L) <room_name>..."""
        room_type = None
        if args["O"].upper() == 'O':
            room_type = "O"
        else:
            room_type = "L"
        amity.create_room(room_type, args["<room_name>"])
       
        
    @docopt_cmd
    def do_add_person(self, args):
        """
        Usage: add_person <first_name> <last_name> (F | S) [--wants_accomodation=value]
        """
        if args["F"].upper() == 'F':
            category = "F"
        else:
            category = "S"
        first_name = args["<first_name>"]
        last_name = args["<last_name>"]
        amity.add_person(first_name, last_name, category, args["--wants_accomodation"])
        
    @docopt_cmd
    def do_reallocate_person(self, args):
        """Usage: reallocate_person <person_id> <new_room>"""
        if args["<person_id>"].isalpha():
            print("person id cannot be string")
            return
        else:
            (amity.reallocate_person(int(args['<person_id>']),
                                     args['<new_room>']))

    @docopt_cmd
    def do_save_state(self, args):
        """Persists app data into the given db
        Usage: save_state (--db_name=sqlite_db)
        """
        db = args['--db_name']
        amity.save_state(db)
       
    @docopt_cmd
    def do_print_unallocated(self, args):
        """Usage: print_unallocated [--file=text_file]"""
        amity.print_unallocated(args['--file'])

    @docopt_cmd
    def do_print_allocations(self, args):
        """
        Prints all rooms and the people in them.
        Usage: print_allocations [--o=filename]
        """
        filename = args["--o"] or ""
        amity.print_allocations(filename)

    @docopt_cmd
    def do_delete_employee(self, args):
        """Usage: delete_employee <person_id>"""
        if args["<person_id>"].isalpha():
            print("person id cannot be string")
            return
        else:
            (amity.delete_employee(int(args['<person_id>'])))

    @docopt_cmd
    def do_delete_rooms(self, args):
        """Usage: delete_room <room_name>"""
        amity.delete_rooms(args['<room_name>'])


    @docopt_cmd
    def do_load_state(self, arg):
        """
        Loads data from the specified db into the app.
        Usage: load_state <filename>
        """
        amity.load_state(arg["<filename>"])

    @docopt_cmd
    def do_load_people(self, args):
        """Usage: load_state <text_file>"""
        amity.load_people(args["<text_file>"])
    
    
    @docopt_cmd
    def do_print_room(self, args):
        """Usage: print_room <room_name>"""

        room_name = args["<room_name>"]
        amity.print_room(room_name)
    @docopt_cmd
    def do_clear(self, arg):
        """Clears screen"""

        os.system('clear')

    @docopt_cmd
    def do_load_people(self, args):
        """Usage: load_state <text_file>"""
        amity.load_people(args["<text_file>"])



    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Thank you for using Amity. Adios!')
        exit()

   
opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    os.system('clear')
    intro()
    AmitySystem().cmdloop()

print(opt)


