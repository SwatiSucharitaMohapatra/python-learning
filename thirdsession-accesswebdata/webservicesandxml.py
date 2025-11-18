import xml.etree.ElementTree as ET

# Simple XML Data
data = ''' <person>
    <name>Swati</name>
    <phone type="intl">+1234567</phone>
    <email hide="yes"/>
  </person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Phone:', tree.find('phone').text)
print('Email Attr:', tree.find('email').get('hide')) 



# Read Nested XML data 
data2 = '''<stuff>
    <users>
        <user num='2'>
            <id>1234</id>
            <name>ABCD</name>
        </user>
        <user num='5'>
            <id>12345</id>
            <name>MNOP</name>
        </user>
    </users>
</stuff>'''  

tree = ET.fromstring(data2)
userlist = tree.findall('users/user')
print('user count:', len(userlist))
for user in userlist :
    print('Name:', user.find('name').text)
    print('ID:', user.find('id').text)
    print('User Number(Attribute Value of User Tag):', user.get('num'))
