%include	/usr/lib/rpm/macros.perl
Summary:	Automatic mp3 ripper
Name:		choad
Version:	0.82
Release:	1
License:	Artistic
Group:		Applications/Console
Group(de):	Applikationen/Konsole
Group(pl):	Aplikacje/Konsola
Source0:	http://www.ftso.org/choad/%{name}.tgz
Patch0:		%{name}-perldir.patch
Requires:	perl-CDDB
Requires:	cdparanoia-III
Requires:	lame
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
URL:		http://www.ftso.org/choad/

%description
Choad is a flexible, Perl-based command-line frontend to the CDDB
database (via CDDB.pl), the cdparanoia CD ripper, and the LAME MP3
encoder.

%prep
%setup -q
%patch0 -p1

%build
gzip -9nf README 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install choad $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/choad
%doc README.gz
