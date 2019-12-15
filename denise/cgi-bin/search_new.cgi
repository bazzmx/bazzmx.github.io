#!/usr/bin/perl -wT

########
# Pragma
########

use strict;
use warnings;
#use CGI qw(-utf8);			# Bug con el header
#use utf8;					# Solo se necesita entrada en utf8
binmode (STDIN, ":utf8");
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);


####################
# Array y encabezado
####################

print header(-charset => 'utf-8');
print start_html("Datos recibidos");
my %form;

################
# Error handling
################

if (param("query_text") eq "" && param("query") eq "") {
	&dienice ("Introduce un término o texto para analizar.");
}

if (param("query_text") ne "" && param("query") ne "") {
	&dienice ("Introduce solo un término o texto para analizar.");
}

if (param("lang") eq ""){
	&dienice("Selecciona una lengua de trabajo");
}

if (param("query_text") ne "" || param("query") eq "") {
	print h2("Entrada de texto")
}

if (param("query") ne "" || param("query_text") eq "") {
	print h2("Entrada de término")
}

#################
# Datos recibidos
#################

foreach my $parametro (param()) {
	$form{$parametro} = param($parametro);
	if ($form{$parametro} ne "") {
		print "$parametro = $form{$parametro}<br>\n";
	}
}

###################
# Mensajes de error
###################

sub dienice {
    my($errorMsg) = @_;
    print h2("Error");
    print p("¡Ahí va qué erroraco!");
    print p($errorMsg);
    exit;
}

##################
# Fin del programa
##################

print end_html;