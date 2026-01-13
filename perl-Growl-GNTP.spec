#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Growl
%define		pnam	GNTP
Summary:	Growl::GNTP - Perl implementation of GNTP Protocol (Client Part)
Name:		perl-Growl-GNTP
Version:	0.20
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Growl/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	482e242fc8d274d1138c361200e0b65d
URL:		http://search.cpan.org/dist/Growl-GNTP/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(IO::Socket::PortState)
BuildRequires:	perl-Crypt-CBC >= 2.29
BuildRequires:	perl-Data-UUID >= 0.149
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Growl::GNTP is Perl implementation of GNTP Protocol (Client Part)

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%dir %{perl_vendorlib}/Growl
%{perl_vendorlib}/Growl/GNTP.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
