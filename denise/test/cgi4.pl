#!/usr/bin/perl -w

# Este script genera la descarga de un archivo en blanco con el nombre Filename
# HTTP Header

print "Content-Type:application/octect-stream; name\"FileName\"\r\n";
print "Content-Disposition: attachment; filename=\"Filename\"\r\n\n";

# Actual file content will go hear, here?

open( FILE, "<FileName" );
while(read(FILE, $buffer, 100)) {
  print("$buffer");
}
