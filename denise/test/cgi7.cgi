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

$lengua = $FORM{lengua};

print "Content-Type:text/html\n\n";
print "<html>";
print "<head>";
print "<title>Radio con CGI</title>";
print "</head>";
print "<body>";
print "<h2>La lengua selccionada es: $lengua</h2>";
print "</body>";
print "</html>";

1;
