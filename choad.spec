Summary:	Automatic MP3 ripper
Summary(pl.UTF-8):	Automatyczny ripper MP3
Name:		choad
Version:	0.822
Release:	1
License:	Artistic
Group:		Applications/Sound
Source0:	http://www.ftso.org/choad/%{name}.tgz
# Source0-md5:	62512e3e688f98ae20fd043e8ff2194e
Patch0:		%{name}-perldir.patch
URL:		http://www.ftso.org/choad/
BuildRequires:	perl-CDDB
BuildRequires:	rpm-perlprov
Requires:	cdparanoia-III
Requires:	lame
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Choad is a flexible, Perl-based command-line frontend to the CDDB
database (via CDDB.pl), the cdparanoia CD ripper, and the LAME MP3
encoder.

%description -l pl.UTF-8
choad to elastyczny, oparty na Perlu, działający z linii poleceń
frontend do bazy danych CDDB, rippera CD cdparanoia i kodera MP3 LAME.

%prep
%setup -q
%patch -P0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install choad $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.1ST README.2ND
%attr(755,root,root) %{_bindir}/choad
