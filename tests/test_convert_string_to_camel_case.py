import unittest
from solutions.Convert_string_to_camel_case import to_camel_case

class TestConvertStringToCamelCase(unittest.TestCase):
    
    def test_to_camel_case(self):
        #Test for basic examples
        self.assertEqual(to_camel_case("the_stealth_samurai"), "theStealthSamurai")
        self.assertEqual(to_camel_case("The-Stealth-Samurai"), "TheStealthsamurai")
        self.assertEqual(to_camel_case("the-Stealth_Samurai"), "theStealthSamurai")
        
        #Test for Empty String 
        self.assertEqual(to_camel_case(""), "")
        
        #Test for string without special characters 
        self.assertEqual(to_camel_case("hello"), "hello")
        
        #Test for capitalized string 
        self.assertEqual(to_camel_case("Hello_world"), "HelloWorld")

if __name__ == "__main__":
    unittest.main()