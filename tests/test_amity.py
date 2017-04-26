import os
import unittest
from .context import Amity
from ..views import Amity
from ..models.rooms import Office
from ..models.rooms import LivingSpace

class Amitytest(unittest.TestCase):
    
    def setUp(self):
        """To set up test variables."""
        self.amity = Amity()
        self.db_name = "faha"

    def tearDown(self):
        """To free variables for fresh use in other tests."""
        if os.path.exists(self.db_name + ".db"):
            os.remove(self.db_name + ".db")
        del self.amity
        
    def test_create_room_adds_room_succesfully(self):
        """To test if create_room adds office(s) successfully."""
        self.amity.create_room('O', ['Krypton'])
        self.assertIn('KRYPTON', [room.room_name.upper() for room in self.amity.all_rooms])
        

    def test_add_person_adds_fellow_to_list(self):
        """To test if fellow is added to fellow list"""
        all_fellows = len(self.amity.all_fellows) + 1
        self.amity.add_person('dede','faith','F','N')
        self.assertEqual(len(self.amity.all_fellows), all_fellows, msg = "fellow not added")

    def test_add_person_adds_staff_to_list(self):
        """To test if staff is added to staff list"""
        all_staff = len(self.amity.all_staff) + 1
        self.amity.add_person('ded','fai','S','N')
        self.assertEqual(len(self.amity.all_staff), all_staff, msg = "staff not added")

    def test_staff_not_in_accomodation_list(self):
        """test that fellow is not entitled to living space"""
        self.amity.create_room('L', ['bonivile'])
        new_staff = len(self.amity.living_space_allocations['bonivile']) + 1
        self.amity.add_person('ded','fai','S','Y')
        self.assertNotEqual(len(self.amity.living_space_allocations['bonivile']), new_staff, msg = "staff cannot be allocated to living space")


    def test_office_is_created_successfully(self):
        """Tests offices are created"""
        self.amity.create_room('O', ['Krypto'])
        self.assertTrue('Krypto' in self.amity.office_allocations.keys())
        
    def test_living_space_is_created_successfully(self):
        """Tests living space are created"""
        self.amity.create_room('L', ['Krpto'])
        self.assertTrue('Krpto' in self.amity.living_space_allocations.keys())
        

    def test_reallocate_person_to_office(self):
        """Test if person reallocated succesfully to office"""
        self.amity.create_room('O', ['oculus'])
        self.amity.create_room('O', ['Krypto'])
        self.amity.reallocate_person('','krypto')
        self.assertFalse('dede' in self.amity.office_allocations['oculus'], msg = "person not reallocated succesfully to office")

    
    def test_if_person_is_added_to_livingspace(self):
        """ Test if person has been added to a living space"""
        living_spaces = len(self.amity.living_space_allocations) + 1
        self.amity.create_room('L', ['ruby'])
        self.amity.add_person('dedS','gath','F', 'Y')
        self.assertEqual(len(self.amity.living_space_allocations), living_spaces, msg = "livingroom is not added succesfully")

    def test_if_person_is_added_to_livingspace(self):
        """ Test if person has been added to a living space"""
        living_spaces = len(self.amity.living_space_allocations) + 1
        self.amity.create_room('L', ['ruby'])
        self.amity.add_person('dedS','gath','F', 'Y')
        self.assertEqual(len(self.amity.living_space_allocations), living_spaces, msg = "livingroom is not added succesfully")


    def test_fellow_does_not_want_accomodation(self):
        """To test if fellow does not want accomodation"""
        self.amity.add_person('dedeh', 'fagh', 'F', 'N')
        self.assertFalse('dedeh' in self.amity.living_space_allocations, msg = 'fellow does not want accomodation')

    def test_add_person_adds_people_to_waiting_list_if_office_is_full(self):
        """To test if add_person caters for excess people.
        Adds fellow/staff to office waiting list when offices are full.
        """
        self.amity.add_person("Daniel", "Maina","F", "N")
        self.amity.add_person("Dan", "Wachira", "F")
        self.amity.add_person("Larry", "W", "F", "N")
        self.amity.add_person("David", "White", "S", "N")
        self.amity.add_person("Xie", "Yuen", "S", "N")
        self.amity.add_person("Stella", "Storl", "S", "N")
        self.assertFalse('stella' in self.amity.office_allocations, msg = "person not reallocated succesfully to office")

    def test_add_person_adds_fellows_to_living_space_waiting_list(self):
        """To test if add_person caters for excess people.
        Adds fellow to living space waiting list when offices are full.
        """
        self.amity.add_person("Daniel", "Maina","F", "Y")
        self.amity.add_person("Dan", "Wachira", "F","Y")
        self.amity.add_person("Larry", "W", "F", "Y")
        self.amity.add_person("David", "White", "Y", "Y")
        self.amity.add_person("Xie", "Yuen", "S", "Y")
        # self.amity.add_person("Stella", "Storl", "S", "Y")
        self.assertFalse('stella' in self.amity.living_space_allocations, msg = "person not reallocated succesfully to living space")

    def test_print_room_does_not_print_inexistent_room(self):
        """To test if method prints rooms and occupants successfully."""
        room_name = "I don't exist!!!"
        self.assertEqual(self.amity.print_room(room_name),None)
    
    def test_print_unallocated_returns_all_not_in_accomodation_list(self):
        """"To test print unallocated works"""
        self.amity.print_unallocated('')
        self.assertFalse('Dan' in self.amity.office_allocations, msg = "person not in accomodation list")


    def test_print_allocations_prints_successfully_to_screen(self):
        """To test if method prints allocations to screen."""
        self.amity.create_room("O", ["Narnia"])
        self.amity.create_room("living_space", ["Python"])
        # create people
        self.amity.add_person("Fell", "Dl", "S", "Y")
        self.amity.add_person("Fell", "Dl", "S", "Y")
        self.amity.add_person("Fello", "Dl", "S", "Y")

        self.assertEqual(self.amity.print_allocations(),"office allocations printed successfully")
    
    def test_save_state(self):
        """ Test that save state , saves people successfully"""
        self.amity.create_room("O", ["Narnia"])
        self.amity.create_room("L", ["Python"])
        self.amity.add_person("Fell", "Dl", "S", "Y")
        self.amity.add_person("Fell", "Dl", "S", "Y")
        self.assertEqual(self.amity.save_state(self.db_name), "successfully saved people")

    def test_load_state(self):
        """ Test that the method loads people to the app succesfully"""
        self.amity.create_room("O", ["Narnia"])
        self.amity.create_room("L", ["Python"])
        self.amity.add_person("Fell", "Dl", "S", "Y")
        self.amity.add_person("Fell", "Dl", "S", "Y")
        self.amity.save_state(self.db_name)
        self.assertEqual(self.amity.load_state(self.db_name), "Successfully loaded people to the app")


if __name__ == '__main__':
    unittest.main()