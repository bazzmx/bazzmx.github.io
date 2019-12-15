#!/usr/bin/perl -w

local ($buffer, @pairs, $pair, $name, $value, %FORM);
$ENV{'REQUEST_METHOD'} =~ tr/a-z/A-Z/;

if ($ENV{'REQUEST_METHOD'} eq "POST"){
  read(STDIN, $buffer, $ENV{'CONTENT_LENGHT'});
} else {
  $buffer = $ENV{'QUERY_STRING'};
}

#Separa la información en pares de nombres/valor
@pairs = split(/&/, $buffer);

foreach $pair (@pairs) {
  ($name, $value) = split(/=/, $pair);
  $value =~ tr/+/ /;
  $value =~ s/%(..)/pack("C", hex($1))/eg;
  $FORM{$name} = $value;
}

if ( $FORM{mate} ) {
  $mate_flag = "ON";
} else {
  $mate_flag = "OFF";
}

if ( $FORM{fisica} ) {
  $fisica_flag = "ON";
} else {
  $fisica_flag = "OFF";
}

print "Content-type:text/html\r\n\r\n";
print "<html>";
print "<head>";
print "<title>Checkbox con CGI</title>";
print "</head>";
print "<body>";
print "<h2> La checkbox Matemáticas está: $mate_flag</h2>";
print "<h2> La checkbox Física está: $fisica_flag</h2>";
print "</body>";
print "</html>";

1;
