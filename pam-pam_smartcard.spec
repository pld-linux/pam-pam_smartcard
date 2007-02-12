#
# Conditional build:
%bcond_with	cyberflex	# support Cyberflex cards (instead of Cryptoflex)
#
%define 	modulename pam_smartcard
Summary:	RSA PAM Authentication using smartcards
Summary(pl.UTF-8):   Uwierzytelnienie PAM RSA przy użyciu kart procesorowych
Name:		pam-%{modulename}
Version:	0.4.0
Release:	1
Epoch:		0
License:	GPL
Group:		Libraries
Source0:	http://www.musclecard.com/applications/files/smarttools-rsa-%{version}.tar.gz
# Source0-md5:	30eaab43b6c0714f394e439e54389b90
URL:		http://www.musclecard.com/apps.html
BuildRequires:	gmp-devel
BuildRequires:	pam-devel
BuildRequires:	pcsc-lite-devel
Obsoletes:	pam_smartcard
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This PAM module performs a challenge response with the card to perform
authentication. To begin you must have a Schlumberger Cyberflex Access
or Schlumberger Cryptoflex card and an appropriate reader.

This module has been compiled for %{?with_cyberflex:Cyberflex}%{!?with_cyberflex:Cryptoflex} cards.

%description -l pl.UTF-8
Ten moduł PAM komunikuje się z kartą procesorową w celu
uwierzytelnienia. Wymaga karty Schlumberger Cyberflex Access lub
Schlumberger Cryptoflex oraz odpowiedniego czytnika.

Ten moduł został skompilowany dla kart %{?with_cyberflex:Cyberflex}%{!?with_cyberflex:Cryptoflex}.

%prep
%setup -q -n smarttools-rsa-%{version}

%build
%{__make} %{?with_cyberflex:cyberflex}%{!?with_cyberflex:cryptoflex} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fpic -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/%{_lib}/security,%{_bindir}}

install pam_smartcard.so $RPM_BUILD_ROOT/%{_lib}/security
install cschallenge cscrypt csdecrypt csgenkey $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ERRATA LICENSE README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) /%{_lib}/security/pam_smartcard.so
