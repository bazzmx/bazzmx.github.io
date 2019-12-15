#!/usr/bin/perl -w

#El siguiente script toma datos de entrada por un usuario desde un navegador
#Lectura del texto de entrada

local ($buffer, @pairs, $pair, $name, $value, %FORM);
$ENV{'REQUEST_METHOD'} =~ tr/a-z/A-Z/;

if ($ENV{'REQUEST_METHOD'} eq "POST") {
  read(STDIN, $buffer, $ENV{'CONTENT_LENGHT'});
} else {
  $buffer = $ENV{'QUERY_STRING'};
}
#Separación de la informaciónd e entrada en pares nombre/valor
@pairs = split(/&/, $buffer);

foreach $pair (@pairs) {
  ($name, $value) = split(/=/, $pair);
  $value =~ tr/+/ /;
  $value =~ s/%(...)/pack("C", hex($1))/eg;
  $FORM{$name} = $value;
}

$first_name = $FORM{first_name};
$last_name = $FORM{last_name};

print "Content-Type:text/html; charset=UTF-8\n\n";
print "<html>";
print "<head>";
print "<title> Segundo programa CGI</title>";
print "</head>";
print "<body>";
print "<h2>Hola, $first_name $last_name - esto es una entrada de datos</h2>";
print "<h2>Y esta una prueba de codificación: ñá¡</h2>";
print "</body>";
print "</html>";

1;
