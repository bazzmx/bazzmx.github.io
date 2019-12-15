#!/usr/bin/perl -w

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

print "Content-type:text/html\n\n";
print "<html>";
print "<head>";
print "<title>Menú desplegable con CGI</title>";
print "</head>";
print "<body>";
print "<h2>La temática seleccionada es: $subject</h2>";
print "</body>";
print "</hrml>";

1;
