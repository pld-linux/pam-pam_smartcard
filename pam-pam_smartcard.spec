#
# Conditional build:
# _with_cyberflex	- support Cyberflex cards (instead of Cryptoflex)
#
Summary:	RSA PAM Authentication using smartcards
Summary(pl):	Uwierzytelnienie PAM RSA przy u¿yciu kart procesorowych
Name:		pam-pam_smartcard
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
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This PAM module performs a challenge response with the card to perform
authentication. To begin you must have a Schlumberger Cyberflex Access
or Schlumberger Cryptoflex card and an appropriate reader.

This module has been compiled for %{?_with_cyberflex:Cyberflex}%{!?_with_cyberflex:Cryptoflex} cards.

%description -l pl
Ten modu³ PAM komunikuje siê z kart± procesorow± w celu
uwierzytelnienia. Wymaga karty Schlumberger Cyberflex Access lub
Schlumberger Cryptoflex oraz odpowiedniego czytnika.

Ten modu³ zosta³ skompilowany dla kart %{?_with_cyberflex:Cyberflex}%{!?_with_cyberflex:Cryptoflex}.

%prep
%setup -q -n smarttools-rsa-%{version}

%build
%{__make} %{?_with_cyberflex:cyberflex}%{!?_with_cyberflex:cryptoflex} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fpic -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib/security,%{_bindir}}

install pam_smartcard.so $RPM_BUILD_ROOT/lib/security
install cschallenge cscrypt csdecrypt csgenkey $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ERRATA LICENSE README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) /lib/security/pam_smartcard.so
