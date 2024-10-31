import cProfile
import unittest
def integerToHexa(integer):
    output = ["0", "0", "0"] #place holder because 1024 at max will only have 3 digits in hex
    hexlist = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
    hexa = ""
    while (integer > 0 ):
        hexa = hexlist[(integer & 0xF)]+ hexa
        integer >>=4;       
    return("0x"+hexa)

class Tests(unittest.TestCase):
    def test(self):
        self.assertEqual(integerToHexa(256), hex(256))

if __name__ == '__main__':
    cProfile.run('integerToHexa(1024)')
    unittest.main()
    
'''
for i in range(0, 1025):
    print(integerToHexa(i))
'''
