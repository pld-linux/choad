%include	/usr/lib/rpm/macros.perl
Summary:	Automatic mp3 ripper
Summary(pl):	Automatyczny ripper mp3
Name:		choad
Version:	0.82
Release:	1
License:	Artistic
Group:		Applications/Sound
Source0:	http://www.ftso.org/choad/%{name}.tgz
Patch0:		%{name}-perldir.patch
URL:		http://www.ftso.org/choad/
BuildRequires:	perl-CDDB
BuildRequires:	rpm-perlprov
Requires:	cdparanoia-III
Requires:	lame
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
Choad is a flexible, Perl-based command-line frontend to the CDDB
database (via CDDB.pl), the cdparanoia CD ripper, and the LAME MP3
encoder.

%description -l pl
choad to elastyczny, oparty na Perlu, dzia³aj±cy z linii poleceñ
frontend do bazy danych CDDB, rippera CD cdparanoia i kodera MP3 LAME.

%prep
%setup -q -n %{name}-%{version}2
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install choad $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/choad
%doc README
