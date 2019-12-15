#!/usr/bin/perl

local($buffer, @pairs, $pair, $name, $value, %FORM);
#Lectura del texto de entrada
$ENV{'REQUEST_METHOD'} =~tr/a-z/A-Z/;

if ($ENV{'REQUEST_METHOD'} eq "POST") {
  read(STDIN, $buffer, $ENV{'CONTENT_LENGHT'});
} else {
  $buffer = $ENV{'QUERY_STRING'};
}

#Dividir la información en pares de valor/nombre
@pairs = split(/&/, $buffer);

foreach $pair (@pairs) {
  ($name, $value) = split(/=/, $pair);
  $value =~tr/+/ /;
  $value =~s/%(..)/pack("C", hex($1))/eg;
  $FORM{$name} = $value;
}
$subject = $FORM{dropdown};
$lang = $FORM{lang};
$query = $FORM{query};

print "Content-type: text/html\n\n";
print "<html>";
print "<head>";
print "<title>DENISE: Detector de neologismos semánticos</title>";
print "</head>";
print "<body>";
print "<p>La temática seleccionada es: $subject</p>";
print "<p>La lengua de trabajo es: $lang</p>";
print "<p>El término a consultar es: $query</p><br>";
print "</body>";
print "</hrml>";

1;
