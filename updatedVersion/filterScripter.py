f = open("BTHOspam.xml", "w")

#areas of disreguard
paidStudy = True
sports = False
sga = True
studyAbroad = False
menOrgs = True
womanOrgs = True
internationalStudent = True
sorority = True
frats = True
preMed = True

print("""<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns='http://www.w3.org/2005/Atom' xmlns:apps='http://schemas.google.com/apps/2006'>
	<title>Mail Filters</title>
	<id>tag:mail.google.com,2008:filters:z0000001567917192580*0617137246005040398</id>
	<updated>2019-09-08T03:43:39Z</updated>
	<author>
		<name>Howdy Hack</name>
		<email>bthospam@gmail.com</email>
	</author>""",file = f)

if(paidStudy):
    print("""<entry>
		<category term='filter'></category>
		<title>Mail Filter</title>
		<id>tag:mail.google.com,2008:filter:z0000001567918049456*4234574684999581917</id>
		<updated>2019-09-08T04:47:35Z</updated>
		<content></content>
		<apps:property name='hasTheWord' value='list:listserv.tamu.edu &quot;paid AROUND 5 study&quot; OR &quot;participants AROUND 5 needed&quot;'/>
		<apps:property name='label' value='BTHO Spam'/>
		<apps:property name='shouldArchive' value='true'/>
		<apps:property name='sizeOperator' value='s_sl'/>
		<apps:property name='sizeUnit' value='s_smb'/>
	</entry>""",file = f)

if(sports):
    print("""<entry>
		<category term='filter'></category>
		<title>Mail Filter</title>
		<id>tag:mail.google.com,2008:filter:z0000001567916588556*4133876267288466267</id>
		<updated>2019-09-08T04:23:54Z</updated>
		<content></content>
		<apps:property name='hasTheWord' value='list:listserv.tamu.edu &quot;flag football&quot; OR soccer OR softball OR basketball OR volleyball OR fitness OR tryouts OR swim'/>
		<apps:property name='label' value='BTHO Spam'/>
		<apps:property name='shouldArchive' value='true'/>
		<apps:property name='sizeOperator' value='s_sl'/>
		<apps:property name='sizeUnit' value='s_smb'/>
	</entry>""",file = f)

if(sga):
    print("""<entry>
		<category term='filter'></category>
		<title>Mail Filter</title>
		<id>tag:mail.google.com,2008:filter:z0000001567917192580*0617137246005040398</id>
		<updated>2019-09-08T04:33:19Z</updated>
		<content></content>
		<apps:property name='hasTheWord' value='list:listserv.tamu.edu &quot;student government&quot; OR sga'/>
		<apps:property name='label' value='BTHO Spam'/>
		<apps:property name='shouldArchive' value='true'/>
		<apps:property name='sizeOperator' value='s_sl'/>
		<apps:property name='sizeUnit' value='s_smb'/>
	</entry>""",file = f)

if(studyAbroad):
    print("""<entry>
		<category term='filter'></category>
		<title>Mail Filter</title>
		<id>tag:mail.google.com,2008:filter:z0000001567917879904*1467880677483713220</id>
		<updated>2019-09-08T04:44:44Z</updated>
		<content></content>
		<apps:property name='hasTheWord' value='list:listserv.tamu.edu abroad OR &quot;education abroad&quot;'/>
		<apps:property name='label' value='BTHO Spam'/>
		<apps:property name='shouldArchive' value='true'/>
		<apps:property name='sizeOperator' value='s_sl'/>
		<apps:property name='sizeUnit' value='s_smb'/>
	</entry>""",file = f)

if(menOrgs):
    print("""<entry>
		<category term='filter'></category>
		<title>Mail Filter</title>
		<id>tag:mail.google.com,2008:filter:z0000001567915694914*8403489171388310768</id>
		<updated>2019-09-08T04:08:25Z</updated>
		<content></content>
		<apps:property name='hasTheWord' value='list:listserv.tamu.edu &quot;men&apos;s organization&quot; OR brotherhood OR &quot;men&apos;s org&quot; OR &quot;men&apos;s club&quot;'/>
		<apps:property name='label' value='BTHO Spam'/>
		<apps:property name='shouldArchive' value='true'/>
		<apps:property name='sizeOperator' value='s_sl'/>
		<apps:property name='sizeUnit' value='s_smb'/>
	</entry>""",file = f)

if(womanOrgs):
    print("""<entry>
		<category term='filter'></category>
		<title>Mail Filter</title>
		<id>tag:mail.google.com,2008:filter:z0000001567915852475*8708319040071074691</id>
		<updated>2019-09-08T04:10:58Z</updated>
		<content></content>
		<apps:property name='hasTheWord' value='list:listserv.tamu.edu sisterhood OR &quot;woman&apos;s org&quot; OR &quot;woman&apos;s organization&quot; OR &quot;woman&apos;s club&quot;'/>
		<apps:property name='label' value='BTHO Spam'/>
		<apps:property name='shouldArchive' value='true'/>
		<apps:property name='sizeOperator' value='s_sl'/>
		<apps:property name='sizeUnit' value='s_smb'/>
	</entry>""",file = f)

if(internationalStudent):
    print("""<entry>
		<category term='filter'></category>
		<title>Mail Filter</title>
		<id>tag:mail.google.com,2008:filter:z0000001567917755320*6893249877257584554</id>
		<updated>2019-09-08T04:42:39Z</updated>
		<content></content>
		<apps:property name='hasTheWord' value='list:listserv.tamu.edu ISA OR &quot;international graduate student&quot;'/>
		<apps:property name='label' value='BTHO Spam'/>
		<apps:property name='shouldArchive' value='true'/>
		<apps:property name='sizeOperator' value='s_sl'/>
		<apps:property name='sizeUnit' value='s_smb'/>
	</entry>""",file = f)

if(sorority):
    print("""<entry>
		<category term='filter'></category>
		<title>Mail Filter</title>
		<id>tag:mail.google.com,2008:filter:z0000001567914205434*5004510095906683057</id>
		<updated>2019-09-08T03:43:39Z</updated>
		<content></content>
		<apps:property name='hasTheWord' value='list:listserv.tamu.edu (alpha OR beta OR gamma OR delta OR epsilon OR zeta OR eta OR theta OR iota OR kappa OR lambda OR mu OR nu OR xi OR omikron OR pi OR rho OR sigma OR tau OR upsilon OR phi OR chi OR psi OR omega) AND sorority'/>
		<apps:property name='label' value='BTHO Spam'/>
		<apps:property name='shouldArchive' value='true'/>
		<apps:property name='sizeOperator' value='s_sl'/>
		<apps:property name='sizeUnit' value='s_smb'/>
	</entry>""",file = f)

if(frats):
    print("""<entry>
		<category term='filter'></category>
		<title>Mail Filter</title>
		<id>tag:mail.google.com,2008:filter:z0000001567912531823*5233737762649033417</id>
		<updated>2019-09-08T03:15:48Z</updated>
		<content></content>
		<apps:property name='hasTheWord' value='list:listserv.tamu.edu (alpha OR beta OR gamma OR delta OR epsilon OR zeta OR eta OR theta OR iota OR kappa OR lambda OR mu OR nu OR xi OR omikron OR pi OR rho OR sigma OR tau OR upsilon OR phi OR chi OR psi OR omega) AND fraternity'/>
		<apps:property name='label' value='BTHO Spam'/>
		<apps:property name='shouldArchive' value='true'/>
		<apps:property name='sizeOperator' value='s_sl'/>
		<apps:property name='sizeUnit' value='s_smb'/>
	</entry>""",file = f)

if(preMed):
    print("""<entry>
		<category term='filter'></category>
		<title>Mail Filter</title>
		<id>tag:mail.google.com,2008:filter:z0000001567917442483*1892543553781177173</id>
		<updated>2019-09-08T04:37:47Z</updated>
		<content></content>
		<apps:property name='hasTheWord' value='list:listserv.tamu.edu nurse OR doctor OR pre-med OR healthcare'/>
		<apps:property name='label' value='BTHO Spam'/>
		<apps:property name='shouldArchive' value='true'/>
		<apps:property name='sizeOperator' value='s_sl'/>
		<apps:property name='sizeUnit' value='s_smb'/>
	</entry>""",file = f)



print("""</feed>""",file = f)
f.close()